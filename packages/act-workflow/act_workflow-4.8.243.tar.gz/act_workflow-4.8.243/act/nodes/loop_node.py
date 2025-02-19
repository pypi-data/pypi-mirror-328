import logging
from typing import Dict, Any, Optional, List
from .base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import asyncio
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger(__name__)

class LoopNode(BaseNode):
    """Node for executing loop operations with configurable iteration handling."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='loop',
            version='1.0.0',
            description='Executes loop operations over a collection of items with configurable behavior',
            parameters=[
                NodeParameter(
                    name='items',
                    type=NodeParameterType.ARRAY,
                    description='Collection of items to iterate over',
                    required=True
                ),
                NodeParameter(
                    name='parallel',
                    type=NodeParameterType.BOOLEAN,
                    description='Whether to process items in parallel',
                    required=False,
                    default=False
                ),
                NodeParameter(
                    name='max_concurrent',
                    type=NodeParameterType.NUMBER,
                    description='Maximum number of concurrent operations when parallel is true',
                    required=False,
                    default=5
                ),
                NodeParameter(
                    name='batch_size',
                    type=NodeParameterType.NUMBER,
                    description='Number of items to process in each batch',
                    required=False,
                    default=1
                ),
                NodeParameter(
                    name='timeout',
                    type=NodeParameterType.NUMBER,
                    description='Timeout in seconds for each iteration',
                    required=False,
                    default=30
                ),
                NodeParameter(
                    name='error_handling',
                    type=NodeParameterType.STRING,
                    description='How to handle errors in iterations',
                    required=False,
                    default='continue',
                    enum=['continue', 'stop', 'skip']
                )
            ],
            outputs={
                'results': NodeParameterType.ARRAY,
                'successful_count': NodeParameterType.NUMBER,
                'failed_count': NodeParameterType.NUMBER,
                'errors': NodeParameterType.ARRAY
            }
        )

    async def process_item(self, item: Any, timeout: int) -> Dict[str, Any]:
        """Process a single item with timeout."""
        try:
            await asyncio.sleep(0.1)  # Simulate some processing delay
            return {
                'status': 'success',
                'item': item,
                'result': {'processed': True, 'value': item}
            }
        except Exception as e:
            logger.error(f"Error processing item {item}: {str(e)}")
            return {
                'status': 'error',
                'item': item,
                'error': str(e)
            }

    async def process_batch(self, batch: List[Any], timeout: int) -> List[Dict[str, Any]]:
        """Process a batch of items concurrently."""
        tasks = [self.process_item(item, timeout) for item in batch]
        return await asyncio.gather(*tasks, return_exceptions=True)

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)
            
            items = validated_data['items']
            parallel = validated_data.get('parallel', False)
            max_concurrent = validated_data.get('max_concurrent', 5)
            batch_size = validated_data.get('batch_size', 1)
            timeout = validated_data.get('timeout', 30)
            error_handling = validated_data.get('error_handling', 'continue')

            if not items:
                return {
                    'status': 'success',
                    'result': {
                        'results': [],
                        'successful_count': 0,
                        'failed_count': 0,
                        'errors': []
                    }
                }

            results = []
            errors = []
            successful_count = 0
            failed_count = 0

            for i in range(0, len(items), batch_size):
                batch = items[i:i + batch_size]
                
                if parallel:
                    batch_results = await self.process_batch(batch, timeout)
                else:
                    batch_results = []
                    for item in batch:
                        result = await self.process_item(item, timeout)
                        batch_results.append(result)

                for result in batch_results:
                    if isinstance(result, Exception):
                        failed_count += 1
                        errors.append(str(result))
                        if error_handling == 'stop':
                            raise result
                        continue

                    if result['status'] == 'success':
                        successful_count += 1
                        results.append(result['result'])
                    else:
                        failed_count += 1
                        errors.append(result.get('error', 'Unknown error'))
                        if error_handling == 'stop':
                            raise Exception(result.get('error', 'Unknown error'))

            return {
                'status': 'success',
                'result': {
                    'results': results,
                    'successful_count': successful_count,
                    'failed_count': failed_count,
                    'errors': errors
                }
            }

        except Exception as e:
            logger.error(f"Error in LoopNode execution: {str(e)}")
            return self.handle_error(e, context='LoopNode execution')

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Enhanced error handling for loop operations."""
        return {
            'status': 'error',
            'result': {
                'results': [],
                'successful_count': 0,
                'failed_count': 1,
                'errors': [f"{context}: {str(error)}"]
            }
        }

if __name__ == "__main__":
    import asyncio

    async def main():
        node = LoopNode()
        
        test_data = {
            'items': [1, 2, 3, 4, 5],
            'parallel': True,
            'max_concurrent': 3,
            'batch_size': 2,
            'timeout': 5,
            'error_handling': 'continue'
        }

        result = await node.execute(test_data)
        print(result)

    asyncio.run(main())