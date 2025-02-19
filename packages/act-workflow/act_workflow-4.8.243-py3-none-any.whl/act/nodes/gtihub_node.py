import logging
from typing import Dict, Any, Optional
from base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import aiohttp
import asyncio
from urllib.parse import urljoin

logger = logging.getLogger(__name__)

class GithubNode(BaseNode):
    """Node for fetching all GitHub pull requests for a given repository."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='github_prs',
            version='1.0.0',
            description='Fetches all pull requests from a specified GitHub repository',
            parameters=[
                NodeParameter(
                    name='owner',
                    type=NodeParameterType.STRING,
                    description='GitHub repository owner (username or organization)',
                    required=True
                ),
                NodeParameter(
                    name='repo',
                    type=NodeParameterType.STRING,
                    description='GitHub repository name',
                    required=True
                ),
                NodeParameter(
                    name='state',
                    type=NodeParameterType.STRING,
                    description='State of the pull requests to fetch',
                    required=False,
                    default='open',
                    enum=['open', 'closed', 'all']
                ),
                NodeParameter(
                    name='per_page',
                    type=NodeParameterType.NUMBER,
                    description='Number of pull requests per page',
                    required=False,
                    default=30
                ),
                NodeParameter(
                    name='max_pages',
                    type=NodeParameterType.NUMBER,
                    description='Maximum number of pages to fetch',
                    required=False,
                    default=5
                ),
                NodeParameter(
                    name='github_token',
                    type=NodeParameterType.STRING,
                    description='GitHub personal access token for authentication',
                    required=True
                ),
            ],
            outputs={
                'pull_requests': NodeParameterType.ARRAY,
                'total_count': NodeParameterType.NUMBER,
                'error': NodeParameterType.STRING
            }
        )

    def build_github_url(self, owner: str, repo: str, state: str, per_page: int, page: int) -> str:
        """Construct the GitHub API URL for fetching pull requests."""
        base_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        return f"{base_url}?state={state}&per_page={per_page}&page={page}"

    async def fetch_pull_requests(self, session: aiohttp.ClientSession, url: str) -> Optional[Dict[str, Any]]:
        """Fetch pull requests from GitHub API."""
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logger.error(f"GitHub API request failed with status {response.status}")
                    return None
        except aiohttp.ClientError as e:
            logger.error(f"Error fetching GitHub pull requests: {str(e)}")
            return None

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)

            owner = validated_data['owner']
            repo = validated_data['repo']
            state = validated_data.get('state', 'open')
            per_page = validated_data.get('per_page', 30)
            max_pages = validated_data.get('max_pages', 5)
            github_token = validated_data['github_token']

            headers = {
                'Authorization': f'token {github_token}',
                'Accept': 'application/vnd.github.v3+json'
            }

            pull_requests = []
            async with aiohttp.ClientSession(headers=headers) as session:
                for page in range(1, max_pages + 1):
                    url = self.build_github_url(owner, repo, state, per_page, page)
                    prs = await self.fetch_pull_requests(session, url)
                    if prs is None:
                        break  # Stop on failure
                    pull_requests.extend(prs)
                    if len(prs) < per_page:
                        break  # No more pages

            return {
                'status': 'success',
                'result': {
                    'pull_requests': pull_requests,
                    'total_count': len(pull_requests),
                    'error': None
                }
            }
        except Exception as e:
            logger.error(f"Error in GithubNode execution: {str(e)}")
            return self.handle_error(e, context='GithubNode execution')

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Enhanced error handling for GitHub PR fetching."""
        return {
            'status': 'error',
            'result': {
                'pull_requests': [],
                'total_count': 0,
                'error': f"{context}: {str(error)}"
            }
        }

if __name__ == "__main__":
    import asyncio
    import json

    async def test_github_node():
        node = GithubNode()
        # Structure test data to match BaseNode.validate_schema expectations
        # The parameters need to be under a "params" key
        test_data = {
            "params": {
                "owner": "octocat",
                "repo": "Hello-World",
                "state": "open",
                "per_page": 10,
                "max_pages": 2,
                "github_token": "your_github_token_here"  # Replace with a valid token
            }
        }

        result = await node.execute(test_data)
        print(json.dumps(result, indent=2))

    asyncio.run(test_github_node())