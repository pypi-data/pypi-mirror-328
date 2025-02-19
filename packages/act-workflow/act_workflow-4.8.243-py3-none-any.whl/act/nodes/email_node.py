import logging
from typing import Dict, Any, Optional, List
from .base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
import asyncio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

logger = logging.getLogger(__name__)

class EmailNode(BaseNode):
    """Node for sending emails with support for templates and attachments."""

    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type='email',
            version='1.0.0',
            description='Sends emails with support for templates and attachments',
            parameters=[
                NodeParameter(
                    name='smtp_server',
                    type=NodeParameterType.STRING,
                    description='SMTP server address',
                    required=True
                ),
                NodeParameter(
                    name='port',
                    type=NodeParameterType.NUMBER,
                    description='SMTP server port',
                    required=True
                ),
                NodeParameter(
                    name='sender_email',
                    type=NodeParameterType.STRING,
                    description='Sender email address',
                    required=True
                ),
                NodeParameter(
                    name='receiver_email',
                    type=NodeParameterType.STRING,
                    description='Receiver email address',
                    required=True
                ),
                NodeParameter(
                    name='subject',
                    type=NodeParameterType.STRING,
                    description='Email subject',
                    required=True
                ),
                NodeParameter(
                    name='message',
                    type=NodeParameterType.STRING,
                    description='Email message body',
                    required=True
                ),
                NodeParameter(
                    name='template_variables',
                    type=NodeParameterType.OBJECT,
                    description='Variables to substitute in the email message',
                    required=False
                ),
                NodeParameter(
                    name='attachments',
                    type=NodeParameterType.ARRAY,
                    description='List of file paths to attach',
                    required=False
                )
            ],
            outputs={
                'status': NodeParameterType.STRING,
                'message': NodeParameterType.STRING
            }
        )

    async def send_email(self, smtp_server: str, port: int, sender_email: str, receiver_email: str,
                         subject: str, message: str, template_variables: Optional[Dict[str, Any]] = None,
                         attachments: Optional[List[str]] = None) -> Dict[str, Any]:
        """Send an email with optional template variables and attachments."""
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            if template_variables:
                message = message.format(**template_variables)

            msg.attach(MIMEText(message, 'plain'))

            if attachments:
                for attachment in attachments:
                    attachment_part = MIMEBase('application', 'octet-stream')
                    with open(attachment, 'rb') as file:
                        attachment_part.set_payload(file.read())
                    encoders.encode_base64(attachment_part)
                    attachment_part.add_header('Content-Disposition', f'attachment; filename= {attachment}')
                    msg.attach(attachment_part)

            with smtplib.SMTP(smtp_server, port) as server:
                server.send_message(msg)

            return {
                'status': 'success',
                'message': 'Email sent successfully'
            }

        except Exception as e:
            logger.error(f"Error sending email: {str(e)}")
            return {
                'status': 'error',
                'message': str(e)
            }

    async def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validated_data = self.validate_schema(node_data)

            smtp_server = validated_data['smtp_server']
            port = validated_data['port']
            sender_email = validated_data['sender_email']
            receiver_email = validated_data['receiver_email']
            subject = validated_data['subject']
            message = validated_data['message']
            template_variables = validated_data.get('template_variables', {})
            attachments = validated_data.get('attachments', [])

            email_result = await self.send_email(smtp_server, port, sender_email, receiver_email,
                                                 subject, message, template_variables, attachments)

            return email_result

        except Exception as e:
            logger.error(f"Error in EmailNode execution: {str(e)}")
            return self.handle_error(e, context='EmailNode execution')

    def handle_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Enhanced error handling for email operations."""
        return {
            'status': 'error',
            'message': f"{context}: {str(error)}"
        }

if __name__ == "__main__":
    # Test code
    logging.basicConfig(level=logging.INFO)

    node = EmailNode()
    test_data = {
        'smtp_server': 'smtp.example.com',
        'port': 587,
        'sender_email': 'sender@example.com',
        'receiver_email': 'receiver@example.com',
        'subject': 'Test Email',
        'message': 'Hello, this is a test email.',
        'template_variables': {'name': 'John'},
        'attachments': ['attachment1.txt', 'attachment2.pdf']
    }

    asyncio.run(node.execute(test_data))