"""
Custom tools module for AgentStudio
"""
import os
import logging

logger = logging.getLogger(__name__)

# Create custom_tools directory if it doesn't exist
CUSTOM_TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(CUSTOM_TOOLS_DIR):
    try:
        os.makedirs(CUSTOM_TOOLS_DIR)
        logger.info(f"Created custom tools directory: {CUSTOM_TOOLS_DIR}")
    except Exception as e:
        logger.error(f"Error creating custom tools directory: {str(e)}")