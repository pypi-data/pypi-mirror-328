import logging
import asyncio
from typing import Dict, Any, List, Optional
from base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import aiohttp
import json
import time
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger(__name__)

class GmailboxNode(BaseNode):
    """Node for fetching Gmail inbox messages with proper authentication and pagination."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type="gmail_inbox",
            version="1.0.0",
            description="Fetches emails from the Gmail inbox using OAuth authentication.",
            parameters=[
                NodeParameter(
                    name="access_token",
                    type=NodeParameterType.STRING,
                    description="OAuth access token for Gmail API.",
                    required=True,
                ),
                NodeParameter(
                    name="max_results",
                    type=NodeParameterType.NUMBER,
                    description="Maximum number of emails to fetch.",
                    required=False,
                    default=10,
                ),
                NodeParameter(
                    name="query",
                    type=NodeParameterType.STRING,
                    description="Gmail search query to filter emails.",
                    required=False,
                    default="",
                ),
                NodeParameter(
                    name="include_spam_trash",
                    type=NodeParameterType.BOOLEAN,
                    description="Whether to include spam and trash messages.",
                    required=False,
                    default=False,
                ),
                NodeParameter(
                    name="timeout",
                    type=NodeParameterType.NUMBER,
                    description="Request timeout in seconds.",
                    required=False,
                    default=30,
                ),
            ],
            outputs={
                "emails": NodeParameterType.ARRAY,
                "total_fetched": NodeParameterType.NUMBER,
                "error": NodeParameterType.STRING,
            },
        )

    async def fetch_emails(self, session: aiohttp.ClientSession, access_token: str, max_results: int, query: str, include_spam_trash: bool, timeout: int) -> Dict[str, Any]:
        """Fetches emails from Gmail API with pagination and error handling."""
        base_url = "https://www.googleapis.com/gmail/v1/users/me/messages"
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {
            "maxResults": max_results,
            "q": query,
            "includeSpamTrash": str(include_spam_trash).lower(),
        }
        
        emails = []
        next_page_token = None
        attempt = 0

        while True:
            if next_page_token:
                params["pageToken"] = next_page_token

            try:
                async with session.get(base_url, headers=headers, params=params, timeout=timeout) as response:
                    if response.status == 401:
                        raise PermissionError("Invalid or expired access token.")
                    
                    if response.status == 403:
                        raise PermissionError("Access forbidden. Ensure necessary permissions are granted.")

                    if response.status == 429:
                        # Handle rate limiting with exponential backoff
                        wait_time = min(2 ** attempt, 60)
                        logger.warning(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                        await asyncio.sleep(wait_time)
                        attempt += 1
                        continue

                    if response.status >= 500:
                        raise ConnectionError(f"Server error {response.status}. Retrying...")

                    data = await response.json()
                    
                    if "messages" in data:
                        emails.extend(data["messages"])

                    next_page_token = data.get("nextPageToken")

                    if not next_page_token or len(emails) >= max_results:
                        break

            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                logger.error(f"Network error while fetching emails: {str(e)}")
                return {"emails": [], "total_fetched": 0, "error": f"Network error: {str(e)}"}

            except Exception as e:
                logger.error(f"Unexpected error while fetching emails: {str(e)}")
                return {"emails": [], "total_fetched": 0, "error": f"Unexpected error: {str(e)}"}

        return {"emails": emails[:max_results], "total_fetched": len(emails), "error": None}

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """Executes the Gmail inbox fetch operation."""
        try:
            validated_data = self.validate_schema(node_data)

            access_token = validated_data["access_token"]
            max_results = validated_data.get("max_results", 10)
            query = validated_data.get("query", "")
            include_spam_trash = validated_data.get("include_spam_trash", False)
            timeout = validated_data.get("timeout", 30)

            async with aiohttp.ClientSession() as session:
                result = await self.fetch_emails(session, access_token, max_results, query, include_spam_trash, timeout)

            return {
                "status": "success" if not result["error"] else "error",
                "result": result
            }

        except PermissionError as e:
            logger.error(f"Authentication error: {str(e)}")
            return {"status": "error", "result": {"emails": [], "total_fetched": 0, "error": str(e)}}

        except Exception as e:
            logger.error(f"Unexpected execution error: {str(e)}")
            return {"status": "error", "result": {"emails": [], "total_fetched": 0, "error": str(e)}}

# Example test cases
if __name__ == "__main__":
    import asyncio
    import json

    async def test_gmailbox_node():
        node = GmailboxNode()

        # Test Case 1: Valid request
        test_data_1 = {
            "params": {
                "access_token": "VALID_ACCESS_TOKEN",
                "max_results": 5,
                "query": "subject:test",
                "include_spam_trash": False,
                "timeout": 10
            }
        }
        
        result_1 = await node.execute(test_data_1)
        print("Test Case 1 - Valid Request:")
        print(json.dumps(result_1, indent=2))

        # Test Case 2: Invalid token
        test_data_2 = {
            "params": {
                "access_token": "INVALID_ACCESS_TOKEN",
                "max_results": 5,
                "query": "",
                "include_spam_trash": False,
                "timeout": 10
            }
        }
        
        result_2 = await node.execute(test_data_2)
        print("\nTest Case 2 - Invalid Token:")
        print(json.dumps(result_2, indent=2))

        # Test Case 3: Network failure simulation (e.g., timeout)
        test_data_3 = {
            "params": {
                "access_token": "VALID_ACCESS_TOKEN",
                "max_results": 5,
                "query": "",
                "include_spam_trash": False,
                "timeout": 1  # Simulating network timeout
            }
        }

        result_3 = await node.execute(test_data_3)
        print("\nTest Case 3 - Simulated Network Failure:")
        print(json.dumps(result_3, indent=2))

    asyncio.run(test_gmailbox_node())