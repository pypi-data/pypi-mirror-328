import logging
import asyncio
from typing import Dict, Any
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import pdfplumber
from base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType

logger = logging.getLogger(__name__)

class ConverterNode(BaseNode):
    """Node for converting PDF files to TXT format."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='converter',
            version='1.0.0',
            description='Converts a PDF file to a TXT file',
            parameters=[
                NodeParameter(
                    name='input_pdf_path',
                    type=NodeParameterType.STRING,
                    description='Path to the input PDF file',
                    required=True
                ),
                NodeParameter(
                    name='output_txt_path',
                    type=NodeParameterType.STRING,
                    description='Path to save the output TXT file',
                    required=True
                ),
                NodeParameter(
                    name='timeout',
                    type=NodeParameterType.NUMBER,
                    description='Timeout in seconds for the conversion process',
                    required=False,
                    default=60
                )
            ],
            outputs={
                'status': NodeParameterType.STRING,
                'output_txt_path': NodeParameterType.STRING,
                'error': NodeParameterType.STRING
            }
        )

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """Executes the PDF to TXT conversion process asynchronously."""
        try:
            validated_data = self.validate_schema(node_data)

            input_pdf_path = validated_data['input_pdf_path']
            output_txt_path = validated_data['output_txt_path']
            timeout = validated_data.get('timeout', 60)

            if not Path(input_pdf_path).is_file():
                raise FileNotFoundError(f"Input PDF file not found: {input_pdf_path}")

            loop = asyncio.get_running_loop()
            with ThreadPoolExecutor() as pool:
                await loop.run_in_executor(pool, self.convert_pdf_to_txt, input_pdf_path, output_txt_path)

            return {
                'status': 'success',
                'output_txt_path': output_txt_path,
                'error': None
            }

        except FileNotFoundError as e:
            logger.error(f"File error: {str(e)}")
            return self.handle_error(e, context="FileNotFoundError")
        except TimeoutError as e:
            logger.error(f"Timeout error: {str(e)}")
            return self.handle_error(e, context="TimeoutError")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return self.handle_error(e, context="ConverterNode execution")

    def convert_pdf_to_txt(self, input_pdf_path: str, output_txt_path: str) -> None:
        """Performs the actual PDF to TXT conversion in a thread-safe manner."""
        try:
            with pdfplumber.open(input_pdf_path) as pdf:
                text = "\n".join([page.extract_text() or "" for page in pdf.pages])

            with open(output_txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(text)

        except Exception as e:
            logger.error(f"Error during PDF conversion: {str(e)}")
            raise

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Handles errors gracefully and categorizes them appropriately."""
        return {
            'status': 'error',
            'output_txt_path': None,
            'error': f"{context}: {str(error)}"
        }

# Example test cases
if __name__ == "__main__":
    import json

    async def test_converter_node():
        node = ConverterNode()

        # Test case 1: Valid PDF conversion
        test_data_valid = {
            "params": {
                "input_pdf_path": "/Users/tajnoah/Desktop/langmvp/act_workflow/act/nodes/sample.pdf",
                "output_txt_path": "output.txt",
                "timeout": 30
            }
        }
        
        result_valid = await node.execute(test_data_valid)
        print("Test Case 1 (Valid Conversion):")
        print(json.dumps(result_valid, indent=2))

        # Test case 2: Invalid PDF path
        test_data_invalid = {
            "params": {
                "input_pdf_path": "non_existent.pdf",
                "output_txt_path": "output.txt",
                "timeout": 30
            }
        }
        
        result_invalid = await node.execute(test_data_invalid)
        print("Test Case 2 (Invalid PDF Path):")
        print(json.dumps(result_invalid, indent=2))

    asyncio.run(test_converter_node())