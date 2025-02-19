import logging
import asyncio
import aiohttp
from typing import Dict, Any, Optional, List
from concurrent.futures import ThreadPoolExecutor
from base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import time

logger = logging.getLogger(__name__)

class FetchShopifyOrdersNode(BaseNode):
    """Node for fetching new orders from Shopify with robust error handling, pagination, and rate limiting."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='fetch_shopify_orders',
            version='1.0.0',
            description='Fetches all new orders from Shopify with pagination and rate limiting.',
            parameters=[
                NodeParameter(
                    name='shopify_store_url',
                    type=NodeParameterType.STRING,
                    description='The base URL of the Shopify store (e.g., https://yourstore.myshopify.com)',
                    required=True
                ),
                NodeParameter(
                    name='access_token',
                    type=NodeParameterType.STRING,
                    description='Shopify API access token',
                    required=True,
                    secure=True
                ),
                NodeParameter(
                    name='status',
                    type=NodeParameterType.STRING,
                    description='Filter orders by status (e.g., open, closed, cancelled)',
                    required=False,
                    default='open'
                ),
                NodeParameter(
                    name='limit',
                    type=NodeParameterType.NUMBER,
                    description='Number of orders to fetch per request (max 250)',
                    required=False,
                    default=50
                ),
                NodeParameter(
                    name='timeout',
                    type=NodeParameterType.NUMBER,
                    description='Request timeout in seconds',
                    required=False,
                    default=30
                ),
                NodeParameter(
                    name='max_retries',
                    type=NodeParameterType.NUMBER,
                    description='Maximum number of retries on failure',
                    required=False,
                    default=5
                )
            ],
            outputs={
                'orders': NodeParameterType.ARRAY,
                'total_orders_fetched': NodeParameterType.NUMBER,
                'error': NodeParameterType.STRING
            }
        )

    async def fetch_orders(self, session: aiohttp.ClientSession, url: str, headers: Dict[str, str], timeout: int, max_retries: int) -> List[Dict[str, Any]]:
        """Fetch orders from Shopify with pagination and exponential backoff."""
        orders = []
        retries = 0

        while url:
            try:
                async with session.get(url, headers=headers, timeout=timeout) as response:
                    if response.status == 429:  # Rate limit exceeded
                        retry_after = int(response.headers.get("Retry-After", 5))
                        logger.warning(f"Rate limit hit. Retrying after {retry_after} seconds.")
                        await asyncio.sleep(retry_after)
                        continue

                    if response.status >= 500:  # Server errors
                        if retries < max_retries:
                            wait_time = 2 ** retries
                            logger.warning(f"Server error {response.status}. Retrying in {wait_time} seconds.")
                            await asyncio.sleep(wait_time)
                            retries += 1
                            continue
                        else:
                            raise Exception(f"Max retries reached. Last response code: {response.status}")

                    response_data = await response.json()
                    orders.extend(response_data.get("orders", []))

                    # Check for pagination (Shopify uses Link headers)
                    next_url = None
                    link_header = response.headers.get("Link")
                    if link_header:
                        links = link_header.split(", ")
                        for link in links:
                            if 'rel="next"' in link:
                                next_url = link.split(";")[0].strip("<>")

                    url = next_url  # Continue fetching if there's a next page

            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                if retries < max_retries:
                    wait_time = 2 ** retries
                    logger.warning(f"Network error: {str(e)}. Retrying in {wait_time} seconds.")
                    await asyncio.sleep(wait_time)
                    retries += 1
                else:
                    logger.error(f"Max retries reached. Error: {str(e)}")
                    raise

        return orders

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)

            shopify_store_url = validated_data['shopify_store_url']
            access_token = validated_data['access_token']
            status = validated_data.get('status', 'open')
            limit = min(validated_data.get('limit', 50), 250)  # Shopify max limit is 250
            timeout = validated_data.get('timeout', 30)
            max_retries = validated_data.get('max_retries', 5)

            url = f"{shopify_store_url}/admin/api/2023-01/orders.json?status={status}&limit={limit}"
            headers = {
                "X-Shopify-Access-Token": access_token,
                "Content-Type": "application/json"
            }

            async with aiohttp.ClientSession() as session:
                orders = await self.fetch_orders(session, url, headers, timeout, max_retries)

            return {
                'status': 'success',
                'result': {
                    'orders': orders,
                    'total_orders_fetched': len(orders),
                    'error': None
                }
            }

        except Exception as e:
            logger.error(f"Error fetching Shopify orders: {str(e)}")
            return self.handle_error(e, context="FetchShopifyOrdersNode execution")

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Enhanced error handling for Shopify order fetching."""
        return {
            'status': 'error',
            'result': {
                'orders': [],
                'total_orders_fetched': 0,
                'error': f"{context}: {str(error)}"
            }
        }

# Example test cases
if __name__ == "__main__":
    import json

    async def test_fetch_shopify_orders():
        node = FetchShopifyOrdersNode()

        # Test case: Valid request (Replace with actual Shopify store URL and token)
        test_data_valid = {
            "params": {
                "shopify_store_url": "https://yourstore.myshopify.com",
                "access_token": "your_access_token",
                "status": "open",
                "limit": 10,
                "timeout": 10,
                "max_retries": 3
            }
        }

        # Test case: Invalid URL
        test_data_invalid_url = {
            "params": {
                "shopify_store_url": "invalid_url",
                "access_token": "your_access_token",
                "status": "open",
                "limit": 10,
                "timeout": 10,
                "max_retries": 3
            }
        }

        # Test case: Invalid token (simulate authentication failure)
        test_data_invalid_token = {
            "params": {
                "shopify_store_url": "https://yourstore.myshopify.com",
                "access_token": "invalid_token",
                "status": "open",
                "limit": 10,
                "timeout": 10,
                "max_retries": 3
            }
        }

        print("Running valid request test...")
        result_valid = await node.execute(test_data_valid)
        print(json.dumps(result_valid, indent=2))

        print("\nRunning invalid URL test...")
        result_invalid_url = await node.execute(test_data_invalid_url)
        print(json.dumps(result_invalid_url, indent=2))

        print("\nRunning invalid token test...")
        result_invalid_token = await node.execute(test_data_invalid_token)
        print(json.dumps(result_invalid_token, indent=2))

    asyncio.run(test_fetch_shopify_orders())