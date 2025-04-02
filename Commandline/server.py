from mcp.server.fastmcp import FastMCP  
import subprocess  
import logging  
from typing import Optional  
  
# Configure basic logging  
logging.basicConfig(level=logging.INFO, filename='commandline_tool.log')  
logger = logging.getLogger("commandline_tool")  
  
mcp_server = FastMCP("Commandline")  
  
@mcp_server.tool()  
def commandline_tool(command: str, timeout: Optional[int] = 60, working_dir: Optional[str] = None) -> str:  
    """A command line tool that runs a command and returns the output.(Windows)"""  
    """Adds timeout and working directory support for better safety and flexibility."""  
    logger.info(f"Running command: {command}")  
    try:  
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout, cwd=working_dir)  
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"  
    except Exception as e:  
        return f"Error: {str(e)}"  
  
if __name__ == "__main__":  
    # Initialize and run the server  
    mcp_server.run(transport='stdio') 
