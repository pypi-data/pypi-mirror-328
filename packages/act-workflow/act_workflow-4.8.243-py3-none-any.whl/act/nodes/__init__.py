from pathlib import Path
from .node_registry import initialize_registry, node_registry

# Initialize the node registry with the current directory
current_dir = Path(__file__).parent
initialize_registry(str(current_dir))

# Export the registry instance
__all__ = ['node_registry']