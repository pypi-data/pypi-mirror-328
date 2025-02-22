"""Flow management utilities for coordinating multiple agents"""

from typing import Dict, Any, List, Optional, Callable
import asyncio
import logging
from dataclasses import dataclass, field
from datetime import datetime
import streamlit as st
import json

@dataclass
class StepDescription:
    """Represents a workflow step's requirements and format"""
    objective: str
    requirements: List[str]
    format_instructions: Optional[str] = None
    expected_output: Optional[Dict[str, Any]] = None
    constraints: Optional[Dict[str, Any]] = None

@dataclass
class FlowStep:
    """Represents a single step in an agent workflow"""
    name: str
    agent: Any  # Agent instance
    process: Callable
    description: StepDescription
    requires: List[str] = field(default_factory=list)
    status: str = "pending"
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    metrics: Dict[str, Any] = field(default_factory=dict)

class FlowManager:
    """Manages execution of multi-agent workflows"""

    def __init__(self):
        self.steps: List[FlowStep] = []
        self.results: Dict[str, Dict[str, Any]] = {}
        self.status: str = "not_started"
        self.global_metrics: Dict[str, Any] = {}
        self.logger = logging.getLogger(__name__)

    def add_step(self, step: FlowStep) -> None:
        """Add a step to the workflow"""
        if any(s.name == step.name for s in self.steps):
            raise ValueError(f"Step with name '{step.name}' already exists")

        self.logger.info(f"Adding step: {step.name}")
        self.logger.info(f"Objective: {step.description.objective}")
        self.logger.info(f"Requirements: {step.description.requirements}")

        self.steps.append(step)

    async def execute(self, initial_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute the workflow with proper error handling and metrics"""
        try:
            self.status = "running"
            execution_start = datetime.now()
            self.results = {}

            completed_steps = set()
            while len(completed_steps) < len(self.steps):
                available_steps = [
                    step for step in self.steps
                    if step.name not in completed_steps and
                    all(req in completed_steps for req in step.requires)
                ]

                if not available_steps:
                    remaining = [s.name for s in self.steps if s.name not in completed_steps]
                    raise Exception(f"Workflow deadlock. Remaining steps: {remaining}")

                for step in available_steps:
                    try:
                        step.status = "running"
                        step.start_time = datetime.now()

                        st.info(f"Executing step: {step.name}")

                        # Get input and create context
                        step_input = {'input': initial_data.get('input', '')} if initial_data else {}
                        step_context = {
                            'step_name': step.name,
                            'objective': step.description.objective,
                            'requirements': step.description.requirements
                        }

                        # Execute step and get result
                        self.logger.info(f"Executing step {step.name} with context: {json.dumps(step_context)}")
                        result = await step.process(step_input, step_context)
                        self.logger.info(f"Step {step.name} raw result: {json.dumps(result, indent=2)}")

                        # Format result consistently
                        formatted_result = {
                            'output': result.get('output', ''),
                            'tool_calls': result.get('tool_calls', []),
                            'metadata': {
                                'step_name': step.name,
                                'agent_type': result.get('metadata', {}).get('agent_type', 'unknown'),
                                'description': step.description.objective,
                                'timestamp': datetime.now().isoformat()
                            }
                        }

                        # Store results
                        step.result = formatted_result
                        self.results[step.name] = formatted_result

                        # Log the formatted result
                        self.logger.info(f"Step {step.name} formatted result: {json.dumps(formatted_result, indent=2)}")

                        step.status = "completed"
                        step.end_time = datetime.now()
                        completed_steps.add(step.name)

                        st.success(f"Completed step: {step.name}")

                    except Exception as e:
                        step.status = "failed"
                        step.error = str(e)
                        step.end_time = datetime.now()
                        self.logger.error(f"Error in step {step.name}: {str(e)}")
                        st.error(f"Error in step {step.name}: {str(e)}")
                        raise

            execution_end = datetime.now()
            self.global_metrics = {
                'total_duration': (execution_end - execution_start).total_seconds(),
                'completed_steps': len(completed_steps),
                'total_steps': len(self.steps)
            }

            self.status = "completed"
            return self.results

        except Exception as e:
            self.status = "failed"
            self.logger.error(f"Workflow execution failed: {str(e)}")
            st.error(f"Workflow execution failed: {str(e)}")
            raise

    def reset(self) -> None:
        """Reset the workflow state"""
        for step in self.steps:
            step.status = "pending"
            step.start_time = None
            step.end_time = None
            step.result = None
            step.error = None
            step.metrics.clear()
        self.results.clear()
        self.global_metrics.clear()
        self.status = "not_started"

    def get_workflow_status(self) -> Dict[str, Any]:
        """Get the overall workflow status"""
        completed = sum(1 for s in self.steps if s.status == "completed")
        total = len(self.steps)

        return {
            'status': self.status,
            'progress': (completed / total) if total > 0 else 0,
            'completed_steps': completed,
            'total_steps': total,
            'steps': [self.get_step_status(s.name) for s in self.steps],
            'global_metrics': self.global_metrics
        }

    def get_step_status(self, step_name: str) -> Dict[str, Any]:
        """Get detailed status for a specific step"""
        step = next((s for s in self.steps if s.name == step_name), None)
        if not step:
            return {"error": "Step not found"}

        return {
            'name': step.name,
            'status': step.status,
            'start_time': step.start_time,
            'end_time': step.end_time,
            'result': step.result,
            'error': step.error,
            'description': {
                'objective': step.description.objective,
                'requirements': step.description.requirements
            },
            'tool_calls': step.result.get('tool_calls', []) if step.result else []
        }