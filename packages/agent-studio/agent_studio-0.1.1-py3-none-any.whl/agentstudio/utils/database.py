"""JSON-based file storage system for workflow management"""

import json
import os
import threading
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
import logging
from filelock import FileLock

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class DatabaseError(Exception):
    """Custom exception for database operations"""
    pass

class Database:
    """Thread-safe JSON file-based database manager"""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, base_path: str = None):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Database, cls).__new__(cls)
                    # Use current working directory if base_path is not provided
                    cls._instance.base_path = base_path or os.getcwd()
                    cls._instance.agents_file = os.path.join(cls._instance.base_path, 'agents.json')
                    cls._instance.workflows_file = os.path.join(cls._instance.base_path, 'workflows.json')
                    cls._instance.agents_lock = FileLock(os.path.join(cls._instance.base_path, 'agents.json.lock'))
                    cls._instance.workflows_lock = FileLock(os.path.join(cls._instance.base_path, 'workflows.json.lock'))
                    cls._instance.init_db()
                    logger.info(f"Initialized database in directory: {cls._instance.base_path}")
        return cls._instance

    def init_db(self) -> None:
        """Initialize database files"""
        try:
            # Create initial files if they don't exist
            for file_path in [self.agents_file, self.workflows_file]:
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        json.dump({}, f)
                    logger.info(f"Created database file: {file_path}")
            logger.info("Database files initialized successfully")
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")
            raise DatabaseError(f"Database initialization failed: {e}")

    def _read_json_file(self, file_path: str, lock: FileLock) -> Dict:
        """Read JSON file with proper locking"""
        try:
            with lock:
                with open(file_path, 'r') as f:
                    return json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {file_path}: {e}")
            return {}
        except Exception as e:
            logger.error(f"Error reading {file_path}: {e}")
            return {}

    def _write_json_file(self, file_path: str, lock: FileLock, data: Dict) -> bool:
        """Write JSON file with proper locking"""
        try:
            with lock:
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error writing to {file_path}: {e}")
            return False

    def save_agent(self, agent_data: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
        """Save or update agent"""
        if not isinstance(agent_data, dict):
            raise ValueError("Agent data must be a dictionary")

        if not agent_data.get('name'):
            raise ValueError("Agent name is required")

        if not agent_data.get('type'):
            raise ValueError("Agent type is required")

        try:
            agent_id = agent_data.get('id') or str(uuid.uuid4())
            now = datetime.now().isoformat()

            # Prepare agent data
            agent = {
                'id': agent_id,
                'name': agent_data['name'],
                'description': agent_data.get('description', ''),
                'type': agent_data['type'],
                'config': agent_data.get('config', {}),
                'updated_at': now
            }

            # Read existing agents
            agents = self._read_json_file(self.agents_file, self.agents_lock)

            if agent_id in agents:
                agent['created_at'] = agents[agent_id].get('created_at', now)
                logger.info(f"Updating existing agent: {agent_id}")
            else:
                agent['created_at'] = now
                logger.info(f"Creating new agent: {agent_id}")

            # Save agent
            agents[agent_id] = agent
            if self._write_json_file(self.agents_file, self.agents_lock, agents):
                logger.info(f"Successfully saved agent: {agent_id}")
                return agent_id, agent
            else:
                logger.error(f"Failed to save agent: {agent_id}")
                return agent_id, {}

        except Exception as e:
            logger.error(f"Error saving agent: {e}")
            return str(uuid.uuid4()), {}

    def get_agent(self, agent_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve an agent by ID"""
        try:
            agents = self._read_json_file(self.agents_file, self.agents_lock)
            return agents.get(agent_id)
        except Exception as e:
            logger.error(f"Error retrieving agent {agent_id}: {e}")
            return None

    def get_all_agents(self) -> List[Dict[str, Any]]:
        """Retrieve all agents"""
        try:
            agents = self._read_json_file(self.agents_file, self.agents_lock)
            return sorted(
                agents.values(),
                key=lambda x: x.get('created_at', ''),
                reverse=True
            )
        except Exception as e:
            logger.error(f"Error retrieving agents: {e}")
            return []

    def delete_agent(self, agent_id: str) -> bool:
        """Delete an agent by ID"""
        try:
            agents = self._read_json_file(self.agents_file, self.agents_lock)
            if agent_id in agents:
                del agents[agent_id]
                if self._write_json_file(self.agents_file, self.agents_lock, agents):
                    logger.info(f"Successfully deleted agent: {agent_id}")
                    return True
            return False
        except Exception as e:
            logger.error(f"Error deleting agent {agent_id}: {e}")
            return False

    def save_workflow(self, workflow_data: Dict[str, Any]) -> str:
        """Save or update workflow"""
        if not isinstance(workflow_data, dict):
            raise ValueError("Workflow data must be a dictionary")

        if not workflow_data.get('name'):
            raise ValueError("Workflow name is required")

        try:
            workflow_id = workflow_data.get('id') or str(uuid.uuid4())
            now = datetime.now().isoformat()

            # Prepare workflow data
            workflow = {
                'id': workflow_id,
                'name': workflow_data['name'],
                'description': workflow_data.get('description', ''),
                'steps': workflow_data.get('steps', []),
                'deployed': workflow_data.get('deployed', False),
                'deployed_at': workflow_data.get('deployed_at'),
                'created_at': workflow_data.get('created_at', now),
                'updated_at': now
            }

            logger.info(f"Preparing to save workflow: {workflow_id}")
            logger.info(f"Workflow deployment status: {workflow['deployed']}")
            logger.info(f"Workflow data: {json.dumps(workflow, indent=2)}")

            # Read existing workflows
            workflows = self._read_json_file(self.workflows_file, self.workflows_lock)

            if workflow_id in workflows:
                # Preserve existing timestamps if updating
                workflow['created_at'] = workflows[workflow_id].get('created_at', now)
                logger.info(f"Updating existing workflow: {workflow_id}")
            else:
                workflow['created_at'] = now
                logger.info(f"Creating new workflow: {workflow_id}")

            # Save workflow
            workflows[workflow_id] = workflow
            if self._write_json_file(self.workflows_file, self.workflows_lock, workflows):
                logger.info(f"Successfully saved workflow: {workflow_id}")
                return workflow_id
            else:
                raise DatabaseError(f"Failed to save workflow: {workflow_id}")

        except Exception as e:
            logger.error(f"Error saving workflow: {e}")
            raise DatabaseError(f"Failed to save workflow: {str(e)}")

    def get_workflow(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve workflow by ID"""
        try:
            workflows = self._read_json_file(self.workflows_file, self.workflows_lock)
            return workflows.get(workflow_id)
        except Exception as e:
            logger.error(f"Error retrieving workflow {workflow_id}: {e}")
            return None

    def get_all_workflows(self) -> List[Dict[str, Any]]:
        """Retrieve all workflows"""
        try:
            workflows = self._read_json_file(self.workflows_file, self.workflows_lock)
            return sorted(
                workflows.values(),
                key=lambda x: x.get('created_at', ''),
                reverse=True
            )
        except Exception as e:
            logger.error(f"Error retrieving workflows: {e}")
            return []

    def delete_workflow(self, workflow_id: str) -> bool:
        """Delete a workflow by ID"""
        try:
            workflows = self._read_json_file(self.workflows_file, self.workflows_lock)
            if workflow_id in workflows:
                del workflows[workflow_id]
                if self._write_json_file(self.workflows_file, self.workflows_lock, workflows):
                    logger.info(f"Successfully deleted workflow: {workflow_id}")
                    return True
            return False
        except Exception as e:
            logger.error(f"Error deleting workflow {workflow_id}: {e}")
            return False

# Create global database instance
db = Database()