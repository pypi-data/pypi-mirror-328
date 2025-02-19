import logging
from typing import Dict, Any, Callable, List, Optional
from base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType

import asyncio
import json

logger = logging.getLogger(__name__)

class ArrayTransformNode(BaseNode):
    """Node for performing transformations on arrays including map, reduce, filter, and custom operations."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='array_transform',
            version='1.0.0',
            description='Applies transformations such as map, filter, and reduce to an array',
            parameters=[
                NodeParameter(
                    name='array',
                    type=NodeParameterType.ARRAY,
                    description='The input array to transform',
                    required=True
                ),
                NodeParameter(
                    name='operation',
                    type=NodeParameterType.STRING,
                    description='The transformation operation to apply',
                    required=True,
                    enum=['map', 'filter', 'reduce', 'custom']
                ),
                NodeParameter(
                    name='function',
                    type=NodeParameterType.STRING,
                    description='A Python function (as a string) to apply to array elements',
                    required=True
                ),
                NodeParameter(
                    name='initial_value',
                    type=NodeParameterType.ANY,
                    description='Initial value for reduce operation',
                    required=False
                ),
                NodeParameter(
                    name='parallel',
                    type=NodeParameterType.BOOLEAN,
                    description='Whether to process items in parallel',
                    required=False,
                    default=False
                ),
                NodeParameter(
                    name='timeout',
                    type=NodeParameterType.NUMBER,
                    description='Timeout in seconds for each transformation',
                    required=False,
                    default=10
                )
            ],
            outputs={
                'result': NodeParameterType.ARRAY,
                'error': NodeParameterType.STRING
            }
        )

    def compile_function(self, function_str: str) -> Callable:
        """Compiles the provided function string into a Python function."""
        try:
            exec_globals = {}
            exec(f"def user_function(x, acc=None): return {function_str}", {}, exec_globals)
            return exec_globals['user_function']
        except Exception as e:
            raise ValueError(f"Invalid function definition: {str(e)}")

    async def apply_function(self, func: Callable, item: Any, acc: Optional[Any] = None) -> Any:
        """Applies the transformation function asynchronously."""
        try:
            if acc is not None:
                return func(item, acc)
            return func(item)
        except Exception as e:
            logger.error(f"Error applying function to {item}: {str(e)}")
            return None

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)

            array: List[Any] = validated_data['array']
            operation: str = validated_data['operation']
            function_str: str = validated_data['function']
            initial_value = validated_data.get('initial_value')
            parallel: bool = validated_data.get('parallel', False)
            timeout: int = validated_data.get('timeout', 10)

            if not array:
                return {'status': 'success', 'result': {'result': [], 'error': None}}

            func = self.compile_function(function_str)

            if operation == 'map':
                if parallel:
                    tasks = [self.apply_function(func, item) for item in array]
                    result = await asyncio.gather(*tasks, return_exceptions=True)
                else:
                    result = [func(item) for item in array]

            elif operation == 'filter':
                if parallel:
                    tasks = [self.apply_function(func, item) for item in array]
                    result = [item for item, keep in zip(array, await asyncio.gather(*tasks)) if keep]
                else:
                    result = [item for item in array if func(item)]

            elif operation == 'reduce':
                if initial_value is None:
                    raise ValueError("initial_value is required for reduce operation")

                accumulator = initial_value
                for item in array:
                    accumulator = await self.apply_function(func, item, accumulator)
                result = accumulator

            elif operation == 'custom':
                result = func(array)
            else:
                raise ValueError(f"Unsupported operation: {operation}")

            return {'status': 'success', 'result': {'result': result, 'error': None}}

        except Exception as e:
            logger.error(f"Error in ArrayTransformNode execution: {str(e)}")
            return {'status': 'error', 'result': {'result': None, 'error': str(e)}}
def validate_schema(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates the incoming node data against the schema.
    Returns validated data or raises exceptions for validation errors.
    """
    schema = self.get_schema()
    # Extract parameters from node_data (handle both direct and nested formats)
    params = node_data.get('parameters', node_data)
    
    validated = {}
    
    # Check all required parameters are present
    for param in schema.parameters:
        if param.required and param.name not in params:
            raise ValueError(f"Schema validation error: Missing required parameter: {param.name}")
        
        if param.name in params:
            # Type validation could go here
            validated[param.name] = params[param.name]
        elif param.default is not None:
            validated[param.name] = param.default
            
    return validated

if __name__ == "__main__":
    import asyncio
    import json

    test_node = ArrayTransformNode()

    # Structure the data correctly to match BaseNode.validate_schema expectations
    # The validate_schema method expects data in {"params": {...}} format
    test_data = {
        "params": {
            "array": [1, 2, 3, 4, 5],
            "operation": "map",
            "function": "x * 2",
            "parallel": False
        }
    }

    async def main():
        result = await test_node.execute(test_data)
        print(json.dumps(result, indent=2))

    # Use modern asyncio pattern
    asyncio.run(main())