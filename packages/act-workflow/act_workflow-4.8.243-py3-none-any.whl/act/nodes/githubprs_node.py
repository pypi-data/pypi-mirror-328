import logging
import aiohttp
import asyncio
from typing import Dict, Any, List, Optional
from base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
from concurrent.futures import ThreadPoolExecutor
import time

logger = logging.getLogger(__name__)

class GithubprsNode(BaseNode):
    """Node for fetching all GitHub pull requests from a repository with proper error handling, pagination, and rate limiting."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='github_prs',
            version='1.0.0',
            description='Fetches all pull requests from a GitHub repository with pagination and rate limiting.',
            parameters=[
                NodeParameter(
                    name='repo_owner',
                    type=NodeParameterType.STRING,
                    description='Owner of the GitHub repository',
                    required=True
                ),
                NodeParameter(
                    name='repo_name',
                    type=NodeParameterType.STRING,
                    description='Name of the GitHub repository',
                    required=True
                ),
                NodeParameter(
                    name='state',
                    type=NodeParameterType.STRING,
                    description='State of the PRs to fetch (open, closed, all)',
                    required=False,
                    default='open',
                    enum=['open', 'closed', 'all']
                ),
                NodeParameter(
                    name='per_page',
                    type=NodeParameterType.NUMBER,
                    description='Number of PRs per page (max 100)',
                    required=False,
                    default=30
                ),
                NodeParameter(
                    name='max_pages',
                    type=NodeParameterType.NUMBER,
                    description='Maximum number of pages to fetch',
                    required=False,
                    default=10
                ),
                NodeParameter(
                    name='github_token',
                    type=NodeParameterType.STRING,
                    description='GitHub personal access token for authentication',
                    required=True,
                    secure=True
                )
            ],
            outputs={
                'pull_requests': NodeParameterType.ARRAY,
                'total_count': NodeParameterType.NUMBER,
                'error': NodeParameterType.STRING
            }
        )

    async def fetch_prs(self, session: aiohttp.ClientSession, url: str, headers: Dict[str, str]) -> Optional[List[Dict[str, Any]]]:
        """Fetch PRs from GitHub API with retries and exponential backoff."""
        retries = 5
        backoff_factor = 2

        for attempt in range(retries):
            try:
                async with session.get(url, headers=headers, timeout=30) as response:
                    if response.status == 200:
                        return await response.json()
                    
                    elif response.status == 403 and "X-RateLimit-Remaining" in response.headers:
                        # Handle rate limiting
                        reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60))
                        wait_time = max(reset_time - time.time(), 1)
                        logger.warning(f"Rate limit exceeded. Retrying after {wait_time} seconds.")
                        await asyncio.sleep(wait_time)
                    
                    elif response.status in {500, 502, 503, 504}:
                        logger.warning(f"Server error {response.status}. Retrying in {backoff_factor ** attempt} seconds.")
                        await asyncio.sleep(backoff_factor ** attempt)
                    
                    else:
                        logger.error(f"Failed to fetch PRs: {response.status} - {await response.text()}")
                        return None

            except aiohttp.ClientError as e:
                logger.error(f"Network error while fetching PRs: {str(e)}")
                await asyncio.sleep(backoff_factor ** attempt)

        return None

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the node to fetch GitHub PRs."""
        try:
            validated_data = self.validate_schema(node_data)

            repo_owner = validated_data['repo_owner']
            repo_name = validated_data['repo_name']
            state = validated_data.get('state', 'open')
            per_page = min(validated_data.get('per_page', 30), 100)
            max_pages = validated_data.get('max_pages', 10)
            github_token = validated_data['github_token']

            headers = {
                "Authorization": f"token {github_token}",
                "Accept": "application/vnd.github.v3+json"
            }

            base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
            prs = []
            async with aiohttp.ClientSession() as session:
                for page in range(1, max_pages + 1):
                    url = f"{base_url}?state={state}&per_page={per_page}&page={page}"
                    data = await self.fetch_prs(session, url, headers)

                    if data is None:
                        return self.handle_error("Failed to fetch PRs after retries.")

                    if not data:
                        break  # No more PRs to fetch

                    prs.extend(data)

            return {
                'status': 'success',
                'result': {
                    'pull_requests': prs,
                    'total_count': len(prs),
                    'error': None
                }
            }

        except Exception as e:
            logger.error(f"Error in GithubprsNode execution: {str(e)}")
            return self.handle_error(str(e))

    def handle_error(self, error_message: str) -> Dict[str, Any]:
        """Handle errors gracefully."""
        return {
            'status': 'error',
            'result': {
                'pull_requests': [],
                'total_count': 0,
                'error': error_message
            }
        }

# Example test cases
if __name__ == "__main__":
    import json

    async def test_github_prs():
        node = GithubprsNode()

        # Successful case
        test_data_success = {
            "params": {
                "repo_owner": "tajalagawani",
                "repo_name": "next-js-saas-starterm",
                "state": "open",
                "per_page": 5,
                "max_pages": 2,
                "github_token": "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"
            }
        }

        # Invalid repo case
        test_data_invalid_repo = {
            "params": {
                "repo_owner": "invalid_owner",
                "repo_name": "invalid_repo",
                "state": "open",
                "per_page": 5,
                "max_pages": 2,
                "github_token": "your_valid_github_token_here"
            }
        }

        # Rate limit exceeded case (simulate by using an invalid token)
        test_data_rate_limit = {
            "params": {
                "repo_owner": "octocat",
                "repo_name": "Hello-World",
                "state": "open",
                "per_page": 5,
                "max_pages": 2,
                "github_token": "invalid_token"
            }
        }

        print("Testing successful case...")
        result_success = await node.execute(test_data_success)
        print(json.dumps(result_success, indent=2))

        print("\nTesting invalid repo case...")
        result_invalid_repo = await node.execute(test_data_invalid_repo)
        print(json.dumps(result_invalid_repo, indent=2))

        print("\nTesting rate limit exceeded case...")
        result_rate_limit = await node.execute(test_data_rate_limit)
        print(json.dumps(result_rate_limit, indent=2))

    asyncio.run(test_github_prs())