import logging
from typing import Dict, Any, Optional, List
from .base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import aiohttp
import asyncio
import json

logger = logging.getLogger(__name__)

class DiscordNode(BaseNode):
    """Node for sending messages to Discord channels, supporting text, embeds, and file attachments."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='discord_message',
            version='1.0.0',
            description='Sends messages to Discord channels with optional embeds and file attachments',
            parameters=[
                NodeParameter(
                    name='webhook_url',
                    type=NodeParameterType.STRING,
                    description='The Discord webhook URL to send the message to',
                    required=True
                ),
                NodeParameter(
                    name='content',
                    type=NodeParameterType.STRING,
                    description='The text content of the message',
                    required=False,
                    default=''
                ),
                NodeParameter(
                    name='embeds',
                    type=NodeParameterType.ARRAY,
                    description='List of embed objects to include in the message',
                    required=False,
                    default=[]
                ),
                NodeParameter(
                    name='files',
                    type=NodeParameterType.ARRAY,
                    description='List of file URLs to attach',
                    required=False,
                    default=[]
                ),
                NodeParameter(
                    name='timeout',
                    type=NodeParameterType.NUMBER,
                    description='Timeout in seconds for the request',
                    required=False,
                    default=30
                )
            ],
            outputs={
                'status': NodeParameterType.STRING,
                'response': NodeParameterType.OBJECT,
                'error': NodeParameterType.STRING
            }
        )

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)

            webhook_url = validated_data['webhook_url']
            content = validated_data.get('content', '')
            embeds = validated_data.get('embeds', [])
            files = validated_data.get('files', [])
            timeout = validated_data.get('timeout', 30)

            payload = {'content': content, 'embeds': embeds}
            
            # Remove empty values
            payload = {k: v for k, v in payload.items() if v}

            headers = {'Content-Type': 'application/json'}
            timeout_obj = aiohttp.ClientTimeout(total=timeout)

            async with aiohttp.ClientSession(timeout=timeout_obj) as session:
                form_data = aiohttp.FormData()

                # Add JSON payload
                form_data.add_field('payload_json', json.dumps(payload), content_type='application/json')

                # Attach files if provided
                for index, file_url in enumerate(files):
                    async with session.get(file_url) as file_response:
                        if file_response.status == 200:
                            file_data = await file_response.read()
                            filename = file_url.split('/')[-1]
                            form_data.add_field(f'file{index}', file_data, filename=filename)
                        else:
                            logger.warning(f"Failed to fetch file {file_url}, skipping.")

                async with session.post(webhook_url, data=form_data, headers=headers) as response:
                    response_text = await response.text()
                    response_json = None
                    try:
                        response_json = json.loads(response_text)
                    except json.JSONDecodeError:
                        pass  # Not a JSON response

                    if response.status in [200, 204]:
                        return {
                            'status': 'success',
                            'result': {
                                'response': response_json or response_text,
                                'error': None
                            }
                        }
                    else:
                        raise ValueError(f"Discord API responded with status {response.status}: {response_text}")

        except aiohttp.ClientError as e:
            return self.handle_error(e, context='Discord API request failed')
        except Exception as e:
            return self.handle_error(e, context='DiscordNode execution')

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Enhanced error handling for Discord message operations."""
        logger.error(f"{context}: {str(error)}")
        return {
            'status': 'error',
            'result': {
                'response': None,
                'error': f"{context}: {str(error)}"
            }
        }


if __name__ == "__main__":
    async def test_discord_node():
        node = DiscordNode()
        test_data = {
            "webhook_url": "https://discord.com/api/webhooks/your_webhook_url",
            "content": "Hello from the DiscordNode!",
            "embeds": [
                {
                    "title": "Test Embed",
                    "description": "This is a test embed message",
                    "color": 16711680
                }
            ],
            "files": [],
            "timeout": 10
        }

        result = await node.execute(test_data)
        print(json.dumps(result, indent=4))

    asyncio.run(test_discord_node())