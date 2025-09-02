import docker

docker_client = docker.from_env()

def create_user_container(user_id: str) -> str:
    """
    Create a Docker container for a specific user.
    This should be called when a user logs in.
    
    Args:
        user_id: Unique identifier for the user
    
    Returns:
        Name of the created container
    """
    container_name = f"user_{user_id}_container"
    
    try:
        # Check if container already exists
        existing_container = docker_client.containers.get(container_name)
        return f"Container {container_name} already exists"
    except docker.errors.NotFound:
        pass
    
    # Create new container
    container = docker_client.containers.run(
        "python:3.9-slim",
        command=["tail", "-f", "/dev/null"],
        detach=True,
        name=container_name,
        volumes={'/tmp': {'bind': '/workspace', 'mode': 'rw'}},
        working_dir='/workspace',
        mem_limit='512m',
        remove=False,
        tty=True
    )
    
    return f"Created container {container_name}"

def remove_user_container(user_id: str) -> str:
    """
    Remove a user's Docker container.
    This should be called when a user logs out or via a manual button.
    
    Args:
        user_id: Unique identifier for the user
    
    Returns:
        Status message
    """
    container_name = f"user_{user_id}_container"
    
    try:
        container = docker_client.containers.get(container_name)
        container.remove(force=True)
        return f"Removed container {container_name}"
    except docker.errors.NotFound:
        return f"Container {container_name} not found"
    except docker.errors.APIError as e:
        return f"Error removing container: {str(e)}"