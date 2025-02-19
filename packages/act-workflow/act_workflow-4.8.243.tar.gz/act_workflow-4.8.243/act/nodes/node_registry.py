from typing import Dict, Type, Optional
import importlib
import inspect
import logging
from pathlib import Path
import sys
import os

logger = logging.getLogger(__name__)

class NodeRegistry:
    """
    A centralized registry for managing node types and their implementations.
    """
    def __init__(self):
        self._nodes: Dict[str, Type] = {}
        self._base_node = None
        self._node_paths = {}

    def register(self, node_type: str, node_class: Type) -> None:
        """Register a node type with its implementing class."""
        if node_type in self._nodes:
            logger.warning(f"Overwriting existing node type: {node_type}")
        self._nodes[node_type] = node_class
        logger.info(f"Registered node type: {node_type}")

    def get_node(self, node_type: str) -> Optional[Type]:
        """Get the implementation class for a node type."""
        return self._nodes.get(node_type)

    def set_base_node(self, base_node_class: Type) -> None:
        """Set the base node class."""
        self._base_node = base_node_class

    def get_base_node(self) -> Optional[Type]:
        """Get the base node class."""
        return self._base_node

    def discover_nodes(self, nodes_dir: str) -> None:
        """
        Discover and register node implementations from a directory.
        """
        nodes_path = Path(nodes_dir)
        if not nodes_path.exists():
            logger.error(f"Nodes directory not found: {nodes_dir}")
            return

        # Add nodes directory to Python path if not already there
        nodes_dir_str = str(nodes_path.absolute())
        if nodes_dir_str not in sys.path:
            sys.path.append(nodes_dir_str)
            logger.info(f"Added {nodes_dir_str} to Python path")

        # Add parent directory to Python path for package imports
        parent_dir = str(nodes_path.parent.absolute())
        if parent_dir not in sys.path:
            sys.path.append(parent_dir)
            logger.info(f"Added {parent_dir} to Python path")

        # First, find and load the base node
        for file_path in nodes_path.glob("*.py"):
            if file_path.stem in ['base_node', 'base_node_prod']:
                self._load_base_node(file_path)
                break

        # Then load all other nodes
        for file_path in nodes_path.glob("*.py"):
            if file_path.stem not in ['__init__', 'base_node', 'base_node_prod', 'node_registry']:
                self._load_node_module(file_path)

    def _load_base_node(self, file_path: Path) -> None:
        """Load the base node class."""
        try:
            module_name = f"act.nodes.{file_path.stem}"
            try:
                module = importlib.import_module(module_name)
            except ImportError:
                # Try relative import
                module = importlib.import_module(f".{file_path.stem}", package="act.nodes")
                
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    (name.endswith('Node') or name == 'BaseNode')):
                    self.set_base_node(obj)
                    logger.info(f"Registered base node class: {name}")
                    return
        except Exception as e:
            logger.error(f"Error loading base node from {file_path}: {e}")

    def _load_node_module(self, file_path: Path) -> None:
        """Load a node module and register any node classes found."""
        try:
            module_name = f"act.nodes.{file_path.stem}"
            try:
                module = importlib.import_module(module_name)
            except ImportError:
                # Try relative import
                module = importlib.import_module(f".{file_path.stem}", package="act.nodes")

            # Look for node classes in the module
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    name.endswith('Node') and 
                    self._base_node and 
                    issubclass(obj, self._base_node) and 
                    obj != self._base_node):
                    
                    # Register with both full name and shortened version
                    node_type = name.replace('Node', '')
                    self.register(node_type, obj)
                    self.register(name, obj)
                    self._node_paths[node_type] = str(file_path)

        except Exception as e:
            logger.error(f"Error loading node module {file_path.stem}: {e}")

    def get_registered_nodes(self) -> Dict[str, Type]:
        """Get all registered nodes."""
        return self._nodes.copy()

    def get_node_path(self, node_type: str) -> Optional[str]:
        """Get the file path for a node type."""
        return self._node_paths.get(node_type)

# Create a global instance
node_registry = NodeRegistry()

def initialize_registry(nodes_dir: str) -> None:
    """Initialize the node registry."""
    node_registry.discover_nodes(nodes_dir)

def get_node_class(node_type: str) -> Optional[Type]:
    """Get a node class by its type identifier."""
    return node_registry.get_node(node_type)