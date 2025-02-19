import logging
from typing import Dict, Any, Callable, Optional
from .base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import asyncio
import json

logger = logging.getLogger(__name__)

class TransformNode(BaseNode):
    """Node for transforming input data using custom functions with validation."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='transform',
            version='1.0.0',
            description='Applies a transformation function to input data with validation support',
            parameters=[
                NodeParameter(
                    name='data',
                    type=NodeParameterType.ANY,
                    description='Input data to be transformed',
                    required=True
                ),
                NodeParameter(
                    name='transform_function',
                    type=NodeParameterType.STRING,
                    description='The name of the transformation function to apply',
                    required=True
                ),
                NodeParameter(
                    name='validation_function',
                    type=NodeParameterType.STRING,
                    description='Optional validation function to check input data before transformation',
                    required=False
                ),
                NodeParameter(
                    name='error_handling',
                    type=NodeParameterType.STRING,
                    description='Defines how errors should be handled',
                    required=False,
                    default='continue',
                    enum=['continue', 'stop']
                )
            ],
            outputs={
                'transformed_data': NodeParameterType.ANY,
                'error': NodeParameterType.STRING
            }
        )

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)
            
            data = validated_data['data']
            transform_function_name = validated_data['transform_function']
            validation_function_name = validated_data.get('validation_function')
            error_handling = validated_data.get('error_handling', 'continue')

            # Retrieve and validate transformation function
            transform_function = self.get_function(transform_function_name)
            if not callable(transform_function):
                raise ValueError(f"Invalid transformation function: {transform_function_name}")

            # Retrieve and execute validation function if provided
            if validation_function_name:
                validation_function = self.get_function(validation_function_name)
                if not callable(validation_function):
                    raise ValueError(f"Invalid validation function: {validation_function_name}")

                if not validation_function(data):
                    raise ValueError("Validation failed for input data")

            # Apply transformation function
            transformed_data = await self.apply_transformation(transform_function, data)

            return {
                'status': 'success',
                'result': {
                    'transformed_data': transformed_data,
                    'error': None
                }
            }

        except Exception as e:
            logger.error(f"Error in TransformNode execution: {str(e)}")
            if error_handling == 'stop':
                raise
            return self.handle_error(e, context='TransformNode execution')

    async def apply_transformation(self, transform_function: Callable, data: Any) -> Any:
        """Applies the transformation function asynchronously if needed."""
        if asyncio.iscoroutinefunction(transform_function):
            return await transform_function(data)
        return transform_function(data)

    def get_function(self, function_name: str) -> Optional[Callable]:
        """Retrieves a function by name from the global scope."""
        return globals().get(function_name)

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Enhanced error handling for transformations."""
        return {
            'status': 'error',
            'result': {
                'transformed_data': None,
                'error': f"{context}: {str(error)}"
            }
        }


# Example transformation and validation functions
def sample_transform(data):
    """Sample transformation function: converts input to uppercase if string."""
    if isinstance(data, str):
        return data.upper()
    return data

def sample_validation(data):
    """Sample validation function: checks if input is a string."""
    return isinstance(data, str)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # Register functions in global scope for dynamic retrieval
    globals()["sample_transform"] = sample_transform
    globals()["sample_validation"] = sample_validation

    node = TransformNode()

    # Test case 1: Successful transformation
    test_input_1 = {
        "data": "hello world",
        "transform_function": "sample_transform",
        "validation_function": "sample_validation"
    }

    result_1 = asyncio.run(node.execute(test_input_1))
    print(json.dumps(result_1, indent=2))

    # Test case 2: Failed validation
    test_input_2 = {
        "data": 123,
        "transform_function": "sample_transform",
        "validation_function": "sample_validation"
    }

    result_2 = asyncio.run(node.execute(test_input_2))
    print(json.dumps(result_2, indent=2))

    # Test case 3: Invalid transformation function
    test_input_3 = {
        "data": "hello world",
        "transform_function": "non_existent_function"
    }

    result_3 = asyncio.run(node.execute(test_input_3))
    print(json.dumps(result_3, indent=2))