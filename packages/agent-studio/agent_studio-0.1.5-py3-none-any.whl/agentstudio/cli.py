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

def cleanup(streamlit_process=None, fastapi_process=None):
    """Cleanup function to terminate processes"""
    logger.info("Shutting down AgentStudio...")
    if streamlit_process:
        streamlit_process.terminate()
        streamlit_process.wait()
    if fastapi_process:
        fastapi_process.terminate()
        fastapi_process.join()
    logger.info("Goodbye!")
    sys.exit(0)

def run_streamlit():
    """Run the Streamlit application"""
    try:
        logger.info("Starting Streamlit...")
        # Get the absolute path to main.py
        package_dir = os.path.dirname(os.path.abspath(__file__))
        main_path = os.path.join(package_dir, "web", "main.py")
        logger.debug(f"Streamlit main path: {main_path}")

        # Ensure the file exists
        if not os.path.exists(main_path):
            raise FileNotFoundError(f"Could not find main.py at {main_path}")

        # Use subprocess to run streamlit directly
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run",
            main_path,
            "--server.port", "5000",
            "--server.address", "0.0.0.0",
            "--server.headless", "true"
        ], env=os.environ.copy())

        logger.info(f"Streamlit process started with PID: {process.pid}")
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

    streamlit_process = None
    fastapi_process = None

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
        time.sleep(5)

        # Check if processes are running
        if streamlit_process.poll() is not None:
            logger.error("Streamlit process failed to start")
            cleanup(streamlit_process, fastapi_process)
            sys.exit(1)

        if not fastapi_process.is_alive():
            logger.error("FastAPI process failed to start")
            cleanup(streamlit_process, fastapi_process)
            sys.exit(1)

        logger.info("Both servers started successfully")

        # Register signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, lambda s, f: cleanup(streamlit_process, fastapi_process))
        signal.signal(signal.SIGTERM, lambda s, f: cleanup(streamlit_process, fastapi_process))

        # Keep the main process running
        streamlit_process.wait()
        fastapi_process.join()

    except KeyboardInterrupt:
        cleanup(streamlit_process, fastapi_process)
    except Exception as e:
        logger.error(f"Error starting AgentStudio: {str(e)}", exc_info=True)
        cleanup(streamlit_process, fastapi_process)
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