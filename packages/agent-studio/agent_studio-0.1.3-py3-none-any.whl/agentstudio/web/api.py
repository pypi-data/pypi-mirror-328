"""
FastAPI backend for AgentStudio
"""
from fastapi import FastAPI, HTTPException
import asyncio
from typing import Dict, List, Any, Optional
import logging
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from agentstudio.utils.agent_manager import test_agent
from agentstudio.utils.flow_manager import FlowManager, FlowStep, StepDescription
from agentstudio.utils.database import db
import os
import socket

# Initialize FastAPI app
# Enhanced logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format=
    '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
)
logger = logging.getLogger(__name__)


def find_available_port(start_port: int = 8000, max_tries: int = 100) -> int:
    """Find an available port starting from start_port"""
    for port in range(start_port, start_port + max_tries):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', port))
                return port
        except OSError:
            continue
    raise RuntimeError(
        f"Could not find an available port after {max_tries} attempts")


# Enhanced logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG for detailed logs
    format=
    '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Workflow API",
              description="API for managing and executing workflows",
              version="1.0.0",
              debug=True)


class WorkflowRegistry:

    def __init__(self):
        self.workflows: Dict[str, FlowManager] = {}
        logger.debug("WorkflowRegistry initialized")

    async def initialize(self):
        try:
            logger.debug("Beginning WorkflowRegistry initialization")
            self.workflows.clear()
            return True
        except Exception as e:
            logger.error(f"Failed to initialize workflow registry: {str(e)}",
                         exc_info=True)
            return False

    def add_workflow(self, workflow_id: str, manager: FlowManager):
        logger.debug(f"Adding workflow {workflow_id} to registry")
        self.workflows[workflow_id] = manager

    def get_workflow(self, workflow_id: str) -> Optional[FlowManager]:
        return self.workflows.get(workflow_id)

    def list_workflows(self) -> List[str]:
        return list(self.workflows.keys())

    def clear(self):
        logger.debug("Clearing workflow registry")
        self.workflows.clear()


# Initialize workflow registry
workflow_registry = WorkflowRegistry()


@app.on_event("startup")
async def startup_event():
    """Initialize workflow manager on API startup"""
    try:
        logger.info("Starting API server initialization...")
        success = await workflow_registry.initialize()
        if success:
            logger.info("API server started successfully")
        else:
            logger.error("Failed to initialize workflow manager")
    except Exception as e:
        logger.error(f"API server startup error: {str(e)}", exc_info=True)
    logger.info("API startup completed")


@app.post("/api/deploy")
async def deploy_workflow(workflow_config: Dict[str, Any]):
    """Deploy a workflow configuration"""
    try:
        workflow_id = workflow_config.get('id')
        workflow_name = workflow_config.get('name', 'unnamed')
        logger.info(f"Deploying workflow: {workflow_name}")

        if not workflow_id:
            raise HTTPException(status_code=400,
                                detail="Workflow ID is required")
        if 'steps' not in workflow_config:
            raise HTTPException(status_code=400,
                                detail="Workflow must contain steps")

        deployment_data = {
            'id':
            workflow_id,
            'name':
            workflow_name,
            'description':
            workflow_config.get('description', ''),
            'steps':
            workflow_config['steps'],
            'deployed':
            True,
            'deployed_at':
            datetime.now().isoformat(),
            'created_at':
            workflow_config.get('created_at',
                                datetime.now().isoformat())
        }

        logger.info(f"Saving workflow {workflow_id} to database")
        db.save_workflow(deployment_data)

        current_manager = FlowManager()
        for step_config in workflow_config['steps']:
            logger.info(f"Initializing step: {step_config['name']}")
            step_desc = StepDescription(
                objective=step_config.get('description', ''),
                requirements=step_config.get('requirements', []),
                format_instructions=step_config.get('format_instructions'))

            async def process_step(input_data: Dict[str, Any],
                                   context: Dict[str, Any],
                                   step_cfg=step_config):
                requires = step_cfg.get('requires', [])
                if requires:
                    logger.debug(
                        f"Step '{step_cfg.get('name')}' waiting for dependencies: {requires}"
                    )
                    while not all(dep in context for dep in requires):
                        await asyncio.sleep(0.1)
                    dep = requires[0]
                    dep_output = context[dep].get('output', '')
                    input_data = {'input': dep_output}
                    logger.debug(
                        f"Step '{step_cfg.get('name')}' using output from '{dep}'"
                    )
                logger.info(f"Executing step {step_cfg.get('name')}")
                prompt = f"""
Purpose: {step_cfg.get('description', '')}
Input: {json.dumps(input_data, indent=2)}
Context: {json.dumps(context, indent=2)}
Requirements: {json.dumps(step_cfg.get('requirements', []), indent=2)}
Format Instructions: {step_cfg.get('format_instructions', 'Provide a clear and structured response.')}
"""
                result = await test_agent(step_cfg['agent'], prompt)
                if not isinstance(result, dict):
                    result = {'output': str(result)}
                if 'output' not in result:
                    result['output'] = result.get('result', '')
                result['timestamp'] = datetime.now().isoformat()
                result['metadata'] = {
                    'step_name': step_cfg.get('name'),
                    'agent_type': step_cfg['agent'].get('type', 'unknown'),
                    'description': step_cfg.get('description', '')
                }
                return result

            flow_step = FlowStep(name=step_config['name'],
                                 agent=step_config['agent'],
                                 process=process_step,
                                 description=step_desc,
                                 requires=step_config.get('requires', []))
            current_manager.add_step(flow_step)
            logger.info(f"Successfully added step: {step_config['name']}")

        workflow_registry.add_workflow(workflow_id, current_manager)
        return {
            "status": "success",
            "message": f"Workflow {workflow_name} deployed successfully",
            "workflow_id": workflow_id,
            "deployed_at": deployment_data['deployed_at']
        }
    except Exception as e:
        logger.error(f"Error deploying workflow: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/process/{workflow_id}")
async def process_workflow(workflow_id: str, input_data: Dict[str, Any]):
    """Process a specific workflow with given input data"""
    try:
        workflow_manager = workflow_registry.get_workflow(workflow_id)
        if not workflow_manager:
            raise HTTPException(
                status_code=404,
                detail=
                f"Workflow with ID {workflow_id} not found or not deployed")
        if not workflow_manager.steps:
            raise HTTPException(
                status_code=400,
                detail=f"Workflow {workflow_id} has no steps configured")
        logger.info(
            f"Processing workflow {workflow_id} with input: {input_data}")

        # Execute workflow
        async def execute_workflow(
                input_data: Dict[str, Any]) -> Dict[str, Any]:
            context = {}
            for flow_step in workflow_manager.steps:
                result = await flow_step.process(input_data, context)
                context[flow_step.name] = result
            return context

        results = await execute_workflow(input_data)
        return {
            "status": "success",
            "workflow_id": workflow_id,
            "results": results
        }
    except Exception as e:
        logger.error(f"Error processing workflow: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/workflows")
async def list_workflows():
    """List all deployed workflows"""
    try:
        workflows = db.get_all_workflows()
        logger.info(
            f"Retrieved {len(workflows)} total workflows from database")
        deployed_workflows = [{
            'id':
            w['id'],
            'name':
            w['name'],
            'description':
            w.get('description', ''),
            'steps':
            w['steps'],
            'deployed':
            True,
            'deployed_at':
            w.get('deployed_at',
                  datetime.now().isoformat()),
            'created_at':
            w.get('created_at',
                  datetime.now().isoformat())
        } for w in workflows if w.get('deployed', False)]
        logger.info(f"Found {len(deployed_workflows)} deployed workflows")
        return {"status": "success", "workflows": deployed_workflows}
    except Exception as e:
        logger.error(f"Error listing workflows: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    workflow_count = len(workflow_registry.workflows)
    logger.info(f"Health check - deployed workflows: {workflow_count}")
    return {
        "status": "healthy",
        "workflows_deployed": workflow_count,
        "workflow_ids": workflow_registry.list_workflows(),
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    import time

    # Try to start the server with dynamic port selection
    initial_port = int(os.getenv('API_PORT',
                                 '8000'))  # Changed default port to 8000
    try:
        # First try the specified port
        logger.info(
            f"Attempting to start FastAPI server on port {initial_port}")
        uvicorn.run(app, host="0.0.0.0", port=initial_port)
    except OSError as e:
        if "address already in use" in str(e).lower():
            try:
                # Find an available port starting from initial_port + 1
                new_port = find_available_port(initial_port + 1)
                logger.info(
                    f"Port {initial_port} was in use. Starting server on port {new_port}"
                )
                # Small delay to ensure proper socket cleanup
                time.sleep(1)
                uvicorn.run(app, host="0.0.0.0", port=new_port)
            except Exception as e:
                logger.error(
                    f"Failed to start server on alternative port: {e}")
                raise
        else:
            logger.error(f"Failed to start server: {e}")
            raise
