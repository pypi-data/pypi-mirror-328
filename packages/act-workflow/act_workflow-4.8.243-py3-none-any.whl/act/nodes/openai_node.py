import logging
from typing import Dict, Any
from .base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import asyncio
import openai
import os

logger = logging.getLogger(__name__)

class OpenaiNode(BaseNode):
    """Node for interfacing with OpenAI's GPT models to generate or process text."""

    def __init__(self):
        super().__init__()
        # Assume OPENAI_API_KEY is set in your environment for security reasons
        openai.api_key = os.getenv('OPENAI_API_KEY')
        if not openai.api_key:
            raise ValueError("OpenAI API key must be set as an environment variable 'OPENAI_API_KEY'")

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='openai',
            version='1.0.0',
            description='Interacts with OpenAI GPT models to generate or process text',
            parameters=[
                NodeParameter(
                    name='model',
                    type=NodeParameterType.STRING,
                    description='The OpenAI model to use',
                    required=True
                ),
                NodeParameter(
                    name='prompt',
                    type=NodeParameterType.STRING,
                    description='Text prompt to generate or process text from',
                    required=True
                ),
                NodeParameter(
                    name='max_tokens',
                    type=NodeParameterType.NUMBER,
                    description='Maximum number of tokens to generate',
                    required=False,
                    default=100
                ),
                NodeParameter(
                    name='temperature',
                    type=NodeParameterType.NUMBER,
                    description='Sampling temperature',
                    required=False,
                    default=1.0
                ),
            ],
            outputs={
                'response': NodeParameterType.OBJECT,
            }
        )

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)

            model = validated_data['model']
            prompt = validated_data['prompt']
            max_tokens = validated_data['max_tokens']
            temperature = validated_data['temperature']

            response = await self.call_openai_async(model, prompt, max_tokens, temperature)

            return {
                'status': 'success',
                'result': {
                    'response': response
                }
            }

        except Exception as e:
            logger.error(f"Error in OpenaiNode execution: {str(e)}")
            return self.handle_error(e, context='OpenaiNode execution')

    async def call_openai_async(self, model: str, prompt: str, max_tokens: int, temperature: float) -> Dict[str, Any]:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: openai.Completion.create(
                model=model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )
        )
        return response

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Enhanced error handling for OpenAI operations."""
        return {
            'status': 'error',
            'result': {
                'response': {},
                'error': f"{context}: {str(error)}"
            }
        }

if __name__ == "__main__":
    # Example usage
    logging.basicConfig(level=logging.INFO)
    node = OpenaiNode()

    async def test_node():
        test_data = {
            "model": "text-davinci-003",
            "prompt": "Tell me a joke",
            "max_tokens": 50,
            "temperature": 0.5
        }
        result = await node.execute(test_data)
        print(json.dumps(result, indent=2))

    asyncio.run(test_node())