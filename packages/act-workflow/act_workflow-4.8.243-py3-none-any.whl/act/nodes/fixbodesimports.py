import os
from pathlib import Path

# Standard import template
IMPORT_TEMPLATE = """from .base_node import BaseNode, NodeSchema, NodeParameter, NodeParameterType
"""

def fix_node_imports():
    # Get current directory where this script is running
    current_dir = Path.cwd()
    
    # Files to skip
    skip_files = {
        'base_node.py',
        '__init__.py',
        'node_registry.py',
        'default_page.tsx',
        'fixbodesimports.py',
        'requirements.txt',
        'workflow_parser.log'
    }
    
    # Process each .py file
    for file_path in current_dir.glob('*.py'):
        if file_path.name in skip_files:
            continue
            
        try:
            # Read current content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if it already has the correct import
            if 'from .base_node import BaseNode' in content:
                print(f"✓ {file_path.name} already has correct imports")
                continue
                
            # Remove any existing base_node imports
            lines = content.split('\n')
            new_lines = []
            for line in lines:
                if not any(x in line.lower() for x in ['base_node_prod', 'base_node']):
                    new_lines.append(line)
            
            # Add new import at the top, after any module docstrings
            final_content = []
            added_import = False
            
            for line in new_lines:
                if not added_import and not line.startswith('"""'):
                    final_content.append(IMPORT_TEMPLATE)
                    added_import = True
                final_content.append(line)
            
            # Write back the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(final_content))
                
            print(f"✓ Updated imports in {file_path.name}")
            
        except Exception as e:
            print(f"✗ Error processing {file_path.name}: {str(e)}")

if __name__ == "__main__":
    print("\n=== Starting Node Import Fixer ===\n")
    fix_node_imports()
    print("\n=== Completed Node Import Fixer ===\n")