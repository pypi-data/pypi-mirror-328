import logging
import asyncio
from typing import Dict, Any, List, Optional
from base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import aiohttp
from concurrent.futures import ThreadPoolExecutor
import time

logger = logging.getLogger(__name__)

class JiraNode(BaseNode):
    """Node for fetching all Jira issues from a given project."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type="jira_fetch_issues",
            version="1.0.0",
            description="Fetches all Jira issues from a specified project",
            parameters=[
                NodeParameter(
                    name="jira_url",
                    type=NodeParameterType.STRING,
                    description="Base URL of the Jira instance",
                    required=True
                ),
                NodeParameter(
                    name="project_key",
                    type=NodeParameterType.STRING,
                    description="Jira project key to fetch issues from",
                    required=True
                ),
                NodeParameter(
                    name="auth_token",
                    type=NodeParameterType.STRING,
                    description="Authentication token for Jira API",
                    required=True,
                    secure=True  # Ensure sensitive data is handled properly
                ),
                NodeParameter(
                    name="max_results",
                    type=NodeParameterType.NUMBER,
                    description="Maximum number of results per API call (pagination)",
                    required=False,
                    default=50
                ),
                NodeParameter(
                    name="timeout",
                    type=NodeParameterType.NUMBER,
                    description="Timeout in seconds for API requests",
                    required=False,
                    default=30
                ),
            ],
            outputs={
                "issues": NodeParameterType.ARRAY,
                "total_count": NodeParameterType.NUMBER,
                "error": NodeParameterType.STRING
            }
        )

    async def fetch_issues(self, session: aiohttp.ClientSession, jira_url: str, project_key: str, auth_token: str, max_results: int, timeout: int) -> List[Dict[str, Any]]:
        """Fetch all Jira issues with pagination and exponential backoff for rate limiting."""
        issues = []
        start_at = 0
        retries = 3
        backoff_factor = 2

        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Accept": "application/json"
        }

        while True:
            url = f"{jira_url}/rest/api/2/search?jql=project={project_key}&startAt={start_at}&maxResults={max_results}"
            attempt = 0

            while attempt < retries:
                try:
                    async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
                        if response.status == 401:
                            raise PermissionError("Authentication failed. Check your Jira token.")
                        elif response.status == 429:
                            logger.warning("Rate limit exceeded. Retrying with exponential backoff.")
                            await asyncio.sleep(backoff_factor ** attempt)
                            attempt += 1
                            continue
                        elif response.status >= 400:
                            raise ConnectionError(f"Failed to fetch issues: HTTP {response.status}")

                        data = await response.json()
                        issues.extend(data.get("issues", []))

                        if start_at + max_results >= data.get("total", 0):
                            return issues

                        start_at += max_results
                        break  # Exit retry loop on success

                except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                    logger.error(f"Network error fetching Jira issues: {str(e)}")
                    if attempt == retries - 1:
                        raise
                    await asyncio.sleep(backoff_factor ** attempt)
                    attempt += 1

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the Jira issue fetch operation."""
        try:
            validated_data = self.validate_schema(node_data)

            jira_url = validated_data["jira_url"]
            project_key = validated_data["project_key"]
            auth_token = validated_data["auth_token"]
            max_results = validated_data.get("max_results", 50)
            timeout = validated_data.get("timeout", 30)

            async with aiohttp.ClientSession() as session:
                issues = await self.fetch_issues(session, jira_url, project_key, auth_token, max_results, timeout)

            return {
                "status": "success",
                "result": {
                    "issues": issues,
                    "total_count": len(issues),
                    "error": None
                }
            }

        except PermissionError as e:
            logger.error(f"Authentication error: {str(e)}")
            return self.handle_error(e, context="Jira authentication error")

        except ConnectionError as e:
            logger.error(f"API connection error: {str(e)}")
            return self.handle_error(e, context="Jira API request error")

        except Exception as e:
            logger.error(f"Unexpected error in JiraNode execution: {str(e)}")
            return self.handle_error(e, context="JiraNode execution")

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Enhanced error handling for Jira API operations."""
        return {
            "status": "error",
            "result": {
                "issues": [],
                "total_count": 0,
                "error": f"{context}: {str(error)}"
            }
        }

# Example test with correct parameter structure
if __name__ == "__main__":
    import json

    async def test_jira_node():
        node = JiraNode()
        
        test_data_success = {
            "params": {
                "jira_url": "https://your-jira-instance.atlassian.net",
                "project_key": "TEST",
                "auth_token": "your_api_token_here",
                "max_results": 10,
                "timeout": 10
            }
        }

        test_data_invalid_auth = {
            "params": {
                "jira_url": "https://your-jira-instance.atlassian.net",
                "project_key": "TEST",
                "auth_token": "invalid_token",
                "max_results": 10,
                "timeout": 10
            }
        }

        test_data_invalid_url = {
            "params": {
                "jira_url": "https://invalid-jira-instance.com",
                "project_key": "TEST",
                "auth_token": "your_api_token_here",
                "max_results": 10,
                "timeout": 10
            }
        }

        # Test success case
        print("Testing successful fetch...")
        result_success = await node.execute(test_data_success)
        print(json.dumps(result_success, indent=2))

        # Test invalid authentication
        print("\nTesting invalid authentication...")
        result_invalid_auth = await node.execute(test_data_invalid_auth)
        print(json.dumps(result_invalid_auth, indent=2))

        # Test invalid URL or unreachable server
        print("\nTesting invalid Jira URL...")
        result_invalid_url = await node.execute(test_data_invalid_url)
        print(json.dumps(result_invalid_url, indent=2))

    asyncio.run(test_jira_node())