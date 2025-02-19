import logging
from typing import Dict, Any, Optional
from .base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import aiohttp
import asyncio
import json

logger = logging.getLogger(__name__)

class SlackmsgNode(BaseNode):
    """Node for sending messages to Slack channels with support for attachments and blocks."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='slack_message',
            version='1.0.0',
            description='Sends messages to Slack channels with optional attachments and blocks',
            parameters=[
                NodeParameter(
                    name='webhook_url',
                    type=NodeParameterType.STRING,
                    description='Slack Incoming Webhook URL',
                    required=True
                ),
                NodeParameter(
                    name='text',
                    type=NodeParameterType.STRING,
                    description='Message text to send',
                    required=True
                ),
                NodeParameter(
                    name='attachments',
                    type=NodeParameterType.ARRAY,
                    description='Optional Slack message attachments',
                    required=False,
                    default=[]
                ),
                NodeParameter(
                    name='blocks',
                    type=NodeParameterType.ARRAY,
                    description='Optional Slack message blocks',
                    required=False,
                    default=[]
                ),
                NodeParameter(
                    name='timeout',
                    type=NodeParameterType.NUMBER,
                    description='Timeout in seconds for the Slack API request',
                    required=False,
                    default=10
                )
            ],
            outputs={
                'status_code': NodeParameterType.NUMBER,
                'response_body': NodeParameterType.OBJECT,
                'error': NodeParameterType.STRING
            }
        )

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Validate input data against schema
            validated_data = self.validate_schema(node_data)

            webhook_url = validated_data['webhook_url']
            text = validated_data['text']
            attachments = validated_data.get('attachments', [])
            blocks = validated_data.get('blocks', [])
            timeout = validated_data.get('timeout', 10)

            payload = {
                "text": text,
                "attachments": attachments if attachments else None,
                "blocks": blocks if blocks else None
            }

            # Remove None values from payload
            payload = {key: value for key, value in payload.items() if value is not None}

            timeout_obj = aiohttp.ClientTimeout(total=timeout)

            async with aiohttp.ClientSession(timeout=timeout_obj) as session:
                async with session.post(
                    url=webhook_url,
                    json=payload
                ) as response:
                    try:
                        response_body = await response.json()
                    except (json.JSONDecodeError, aiohttp.ContentTypeError):
                        response_body = await response.text()

                    return {
                        'status': 'success',
                        'result': {
                            'status_code': response.status,
                            'response_body': response_body,
                            'error': None
                        }
                    }

        except aiohttp.ClientError as e:
            return self.handle_error(
                e,
                context=f'Slack API request failed: {str(e)}',
                status_code=getattr(e, 'status', 500)
            )
        except Exception as e:
            return self.handle_error(e, context='SlackmsgNode execution')

    def handle_error(self, error: Exception, context: str, status_code: int = 500) -> Dict[str, Any]:
        """Enhanced error handling for Slack message operations."""
        logger.error(f"{context}: {str(error)}")
        return {
            'status': 'error',
            'result': {
                'status_code': status_code,
                'response_body': None,
                'error': f"{context}: {str(error)}"
            }
        }

if __name__ == "__main__":
    import asyncio

    async def test_slack_message():
        node = SlackmsgNode()
        test_data = {
            "webhook_url": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
            "text": "Hello from SlackmsgNode!",
            "attachments": [{"text": "This is an attachment"}],
            "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "This is a block"}}],
            "timeout": 10
        }

        result = await node.execute(test_data)
        print(json.dumps(result, indent=2))

    asyncio.run(test_slack_message())