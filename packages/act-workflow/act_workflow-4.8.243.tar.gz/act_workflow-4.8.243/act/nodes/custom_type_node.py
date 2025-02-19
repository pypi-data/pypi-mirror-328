import logging
from typing import Dict, Any, Optional
from .base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import json

logger = logging.getLogger(__name__)

class CustomTypeNode(BaseNode):
    """Node for processing and converting custom data types based on configurable parameters."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='custom_type',
            version='1.0.0',
            description='Processes and converts custom data types based on provided configurations.',
            parameters=[
                NodeParameter(
                    name='input_data',
                    type=NodeParameterType.ANY,
                    description='The input data to process',
                    required=True
                ),
                NodeParameter(
                    name='target_type',
                    type=NodeParameterType.STRING,
                    description='The target type to convert the input data to',
                    required=True,
                    enum=['string', 'integer', 'float', 'boolean', 'json']
                ),
                NodeParameter(
                    name='default_value',
                    type=NodeParameterType.ANY,
                    description='Default value to return if conversion fails',
                    required=False,
                    default=None
                ),
                NodeParameter(
                    name='strict_mode',
                    type=NodeParameterType.BOOLEAN,
                    description='Whether to raise an error on failure or return the default value',
                    required=False,
                    default=False
                )
            ],
            outputs={
                'converted_value': NodeParameterType.ANY,
                'success': NodeParameterType.BOOLEAN,
                'error': NodeParameterType.STRING
            }
        )

    def convert_value(self, value: Any, target_type: str) -> Any:
        """Converts the input value to the specified target type."""
        try:
            if target_type == 'string':
                return str(value)
            elif target_type == 'integer':
                return int(value)
            elif target_type == 'float':
                return float(value)
            elif target_type == 'boolean':
                return bool(value)
            elif target_type == 'json':
                return json.loads(value) if isinstance(value, str) else json.dumps(value)
            else:
                raise ValueError(f"Unsupported target type: {target_type}")
        except (ValueError, TypeError, json.JSONDecodeError) as e:
            logger.error(f"Conversion error: {str(e)}")
            raise

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)

            input_data = validated_data['input_data']
            target_type = validated_data['target_type']
            default_value = validated_data.get('default_value', None)
            strict_mode = validated_data.get('strict_mode', False)

            try:
                converted_value = self.convert_value(input_data, target_type)
                return {
                    'status': 'success',
                    'result': {
                        'converted_value': converted_value,
                        'success': True,
                        'error': None
                    }
                }
            except Exception as e:
                if strict_mode:
                    raise e
                return {
                    'status': 'success',
                    'result': {
                        'converted_value': default_value,
                        'success': False,
                        'error': str(e)
                    }
                }

        except Exception as e:
            logger.error(f"Error in CustomTypeNode execution: {str(e)}")
            return self.handle_error(e, context='CustomTypeNode execution')

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Handles errors occurring during execution."""
        return {
            'status': 'error',
            'result': {
                'converted_value': None,
                'success': False,
                'error': f"{context}: {str(error)}"
            }
        }


if __name__ == "__main__":
    import asyncio

    node = CustomTypeNode()

    test_cases = [
        {'input_data': '123', 'target_type': 'integer', 'strict_mode': False},
        {'input_data': 'abc', 'target_type': 'integer', 'strict_mode': False, 'default_value': 0},
        {'input_data': '{"key": "value"}', 'target_type': 'json'},
        {'input_data': 'invalid_json', 'target_type': 'json', 'strict_mode': True},
        {'input_data': 1, 'target_type': 'boolean'},
        {'input_data': 3.14, 'target_type': 'string'}
    ]

    async def run_tests():
        for i, test_case in enumerate(test_cases):
            print(f"Test {i+1}: {test_case}")
            result = await node.execute(test_case)
            print(f"Result: {result}\n")

    asyncio.run(run_tests())