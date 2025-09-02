import os
import docker
import tempfile
import tarfile
from langchain_tavily import TavilySearch
from typing import List, Optional
from langchain.tools import tool
from agent.utils.docker import docker_client

@tool
def install_dependencies(dependencies: List[str], container_name: str) -> str:
    """
    Install Python dependencies in a Docker container. 
    The container must already be running and accessible by name.
    
    Args:
        dependencies: List of Python package names to install
        container_name: Name of the existing Docker container
    
    Returns:
        String indicating success or failure of installation
    """
    try:
        # Get the existing container
        container = docker_client.containers.get(container_name)
        
        # Install each dependency
        results = []
        for dependency in dependencies:
            exit_code, output = container.exec_run(
                f"pip install --no-cache-dir {dependency}",
                workdir="/workspace"
            )
            if exit_code == 0:
                results.append(f"✓ Successfully installed {dependency}")
            else:
                results.append(f"✗ Failed to install {dependency}: {output.decode()}")
        
        return "\n".join(results)
        
    except docker.errors.NotFound:
        return f"Error: Container '{container_name}' not found. Please ensure it's running."
    except docker.errors.APIError as e:
        return f"Docker API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

@tool
def execute_python_code(code: str, container_name: str, filename: Optional[str] = None) -> str:
    """
    Execute Python code in a Docker container.
    The container must already be running and accessible by name.
    
    Args:
        code: Python code to execute
        container_name: Name of the existing Docker container
        filename: Optional filename to use in the container (defaults to timestamp-based name)
    
    Returns:
        Output from executing the code or error message
    """
    try:
        # Get the existing container
        container = docker_client.containers.get(container_name)
        
        # Generate filename if not provided
        if not filename:
            import time
            filename = f"code_{int(time.time())}.py"
        
        # Create temporary code file
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode='w') as temp_code_file:
            temp_code_file.write(code)
            temp_code_filename = temp_code_file.name
        
        # Create tar archive
        tar_filename = temp_code_filename + '.tar'
        with tarfile.open(tar_filename, mode='w') as tar:
            tar.add(temp_code_filename, arcname=filename)
        
        # Copy to container and execute
        with open(tar_filename, 'rb') as tar_file:
            container.put_archive('/workspace', tar_file)
        
        # Execute the code
        exit_code, output = container.exec_run(
            f"python {filename}",
            workdir="/workspace"
        )
        
        response = output.decode('utf-8')
        if exit_code != 0:
            response = f"Execution Error (exit code {exit_code}): {response}"
            
    except docker.errors.NotFound:
        response = f"Error: Container '{container_name}' not found. Please ensure it's running."
    except docker.errors.APIError as e:
        response = f"Docker API Error: {str(e)}"
    except Exception as e:
        response = f"Unexpected error: {str(e)}"
    finally:
        # Cleanup temporary files
        try:
            os.unlink(temp_code_filename)
            os.unlink(tar_filename)
        except:
            pass
    
    return response

@tool
def search_tool(search_query: str) -> str:
    """
    Performs real-time web searches to fetch current information, code examples, or documentation.

    Use this tool only when:
    1. An error occurs that cannot be resolved through normal reasoning and iterative fixes.
    2. Additional context is required about a framework, library, or programming language 
       to generate accurate and reliable code.
    3. Debugging requires checking error messages or searching for recent solutions.
    4. Researching unknown concepts, APIs, or topics mentioned in user queries.
    5. Finding implementation examples, best practices, or up-to-date references.

    Args:
        search_query (str): A concise query describing the error message, 
                            unknown concept, or missing context.

    Returns:
        str: Search results containing relevant information, explanations, 
             or code examples from external sources.
    """
    tavily_search_tool = TavilySearch(
        max_results=5,
        topic="general",
        include_answer=True
    )
    return tavily_search_tool.invoke(search_query)



