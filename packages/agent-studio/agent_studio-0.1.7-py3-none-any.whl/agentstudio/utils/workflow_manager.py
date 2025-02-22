import json
import uuid
from typing import Dict, Any
from datetime import datetime

def create_workflow_from_graph(workflow_data: Dict[str, Any]) -> None:
    """Convert visual flow graph to workflow configuration"""
    try:
        flow_data = workflow_data['flow_data']
        nodes = flow_data['nodes']
        edges = flow_data['edges']

        # Create workflow structure
        workflow = {
            'id': str(uuid.uuid4()),
            'name': workflow_data['name'],
            'description': f"Workflow created using visual builder at {workflow_data.get('created_at')}",
            'steps': [],
            'edges': []
        }

        # Convert nodes to steps
        for node in nodes:
            step = {
                'id': node['id'],
                'name': node.get('data', {}).get('label', 'Unnamed Step'),
                'type': node.get('type', 'default'),
                'config': node.get('data', {}),
                'position': {
                    'x': node.get('position', {}).get('x', 0),
                    'y': node.get('position', {}).get('y', 0)
                }
            }
            workflow['steps'].append(step)

        # Convert edges to workflow connections
        for edge in edges:
            connection = {
                'from': edge['source'],
                'to': edge['target'],
                'config': edge.get('data', {})
            }
            workflow['edges'].append(connection)

        # Save workflow configuration
        with open('workflows.json', 'r+') as f:
            try:
                workflows = json.load(f)
            except json.JSONDecodeError:
                workflows = []

            # Add or update workflow
            workflow_exists = False
            for i, w in enumerate(workflows):
                if w['name'] == workflow_data['name']:
                    workflows[i] = workflow
                    workflow_exists = True
                    break

            if not workflow_exists:
                workflows.append(workflow)

            # Write back to file
            f.seek(0)
            json.dump(workflows, f, indent=2)
            f.truncate()

    except Exception as e:
        raise Exception(f"Error creating workflow from graph: {str(e)}")