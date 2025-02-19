"""
Command-line interface for AgentStudio
"""
import click
import uvicorn
from multiprocessing import Process
import subprocess
import os
import signal
import sys
import logging
import time

# Configure logging with more detail
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def run_streamlit():
    """Run the Streamlit application"""
    try:
        logger.info("Starting Streamlit...")
        # Get the package directory path
        package_dir = os.path.dirname(os.path.abspath(__file__))
        main_path = os.path.join(package_dir, "web", "main.py")

        # Use subprocess to run streamlit directly
        process = subprocess.Popen([
            "streamlit", "run",
            main_path,
            "--server.port", "8501",
            "--server.address", "0.0.0.0",
            "--server.headless", "true"
        ])

        return process

    except Exception as e:
        logger.error(f"Failed to start Streamlit: {str(e)}", exc_info=True)
        raise

def run_fastapi():
    """Run the FastAPI server"""
    try:
        logger.info("Starting FastAPI server...")
        uvicorn.run(
            "agentstudio.web.api:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="debug"
        )
    except Exception as e:
        logger.error(f"Failed to start FastAPI server: {str(e)}", exc_info=True)
        raise

@click.group()
def cli():
    """AgentStudio CLI - Manage your AI agents"""
    pass

@cli.command()
def start():
    """Start both Streamlit and FastAPI servers"""
    logger.info("Starting AgentStudio...")

    try:
        # Start Streamlit process
        streamlit_process = run_streamlit()
        if streamlit_process is None:
            logger.error("Failed to start Streamlit process")
            sys.exit(1)
        logger.debug(f"Started Streamlit process with PID: {streamlit_process.pid}")

        # Start FastAPI in a separate process
        fastapi_process = Process(target=run_fastapi)
        fastapi_process.start()
        logger.debug(f"Started FastAPI process with PID: {fastapi_process.pid}")

        # Wait a moment for the servers to start
        time.sleep(3)

        # Check if processes are running
        if not fastapi_process.is_alive():
            logger.error("FastAPI process failed to start")
            streamlit_process.terminate()
            sys.exit(1)

        def cleanup(signum=None, frame=None):
            logger.info("Shutting down AgentStudio...")
            streamlit_process.terminate()
            fastapi_process.terminate()
            streamlit_process.wait()
            fastapi_process.join()
            logger.info("Goodbye!")
            sys.exit(0)

        # Register signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, cleanup)
        signal.signal(signal.SIGTERM, cleanup)

        # Keep the main process running
        streamlit_process.wait()
        fastapi_process.join()

    except KeyboardInterrupt:
        cleanup()
    except Exception as e:
        logger.error(f"Error starting AgentStudio: {str(e)}", exc_info=True)
        sys.exit(1)

@cli.command()
def version():
    """Show AgentStudio version"""
    from agentstudio import __version__
    click.echo(f"AgentStudio version {__version__}")

def main():
    """Main entry point for the CLI"""
    cli()

if __name__ == "__main__":
    main()