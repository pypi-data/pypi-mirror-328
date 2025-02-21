import aiohttp
import json
import asyncio
from typing import Optional, Dict, AsyncGenerator, Union, List
from dataclasses import dataclass

@dataclass
class SandboxResponse:
    """Response from sandbox operations.
    
    Attributes:
        success: Whether the operation was successful
        data: Optional response data
        error: Optional error message if operation failed
    """
    success: bool
    data: Optional[Dict] = None
    error: Optional[str] = None

@dataclass
class StreamEvent:
    """Event from streaming code execution.
    
    Attributes:
        type: Type of event ('stdout', 'stderr', 'info', 'error', 'completed', 'keepalive')
        data: Event data
    """
    type: str
    data: str

class SandboxClient:
    """Client for interacting with the AI Sandbox service.
    
    This client provides methods to execute Python code in an isolated sandbox environment.
    It handles authentication, sandbox creation/deletion, and code execution.
    
    Args:
        base_url: The base URL of the sandbox service
        token: Optional pre-existing authentication token
    """
    
    def __init__(
        self,
        base_url: str = "http://aicomputer.dev",
        token: Optional[str] = None
    ):
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.sandbox_id = None
        
    async def setup(self) -> SandboxResponse:
        """Initialize the client and create a sandbox.
        
        This method:
        1. Gets a development token (if not provided)
        2. Creates a new sandbox
        3. Waits for the sandbox to be ready
        
        Returns:
            SandboxResponse indicating success/failure
        """
        async with aiohttp.ClientSession() as session:
            # Get development token if not provided
            if not self.token:
                async with session.post(f"{self.base_url}/dev/token") as response:
                    if response.status == 200:
                        data = await response.json()
                        self.token = data["access_token"]
                    else:
                        text = await response.text()
                        return SandboxResponse(success=False, error=text)
                
            # Create sandbox
            headers = {"Authorization": f"Bearer {self.token}"}
            async with session.post(f"{self.base_url}/api/v1/sandbox/create", headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    self.sandbox_id = data["sandbox_id"]
                    # Wait for sandbox to be ready
                    ready = await self.wait_for_ready()
                    if not ready.success:
                        return ready
                    return SandboxResponse(success=True, data=data)
                else:
                    text = await response.text()
                    return SandboxResponse(success=False, error=text)
    
    async def wait_for_ready(self, max_retries: int = 30, delay: int = 1) -> SandboxResponse:
        """Wait for the sandbox to be in Running state.
        
        Args:
            max_retries: Maximum number of status check attempts
            delay: Delay between retries in seconds
            
        Returns:
            SandboxResponse indicating if sandbox is ready
        """
        if not self.token or not self.sandbox_id:
            return SandboxResponse(success=False, error="Client not properly initialized")
            
        headers = {"Authorization": f"Bearer {self.token}"}
        
        for _ in range(max_retries):
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{self.base_url}/api/v1/sandbox/{self.sandbox_id}/status",
                    headers=headers
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data["status"] == "Running":
                            return SandboxResponse(success=True, data=data)
                    await asyncio.sleep(delay)
        
        return SandboxResponse(success=False, error="Sandbox failed to become ready")
    
    async def execute_code(
        self,
        code: Union[str, bytes],
        timeout: int = 30
    ) -> SandboxResponse:
        """Execute Python code in the sandbox and return the combined output.
        
        This method collects all output from the streaming response and returns it as a single result.
        It captures both stdout and stderr, and handles any errors during execution.
        
        Args:
            code: Python code to execute
            timeout: Maximum execution time in seconds
            
        Returns:
            SandboxResponse containing execution results
        """
        if not self.token or not self.sandbox_id:
            return SandboxResponse(success=False, error="Client not properly initialized. Call setup() first")
            
        # Ensure sandbox is ready
        ready = await self.wait_for_ready()
        if not ready.success:
            return ready
            
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "code": code,
            "timeout": timeout
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/api/v1/sandbox/{self.sandbox_id}/execute",
                    headers=headers,
                    json=data
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        return SandboxResponse(success=False, error=error_text)
                    
                    # Parse the response
                    result = await response.json()
                    return SandboxResponse(success=True, data=result)
                    
        except Exception as e:
            return SandboxResponse(success=False, error=f"Connection error: {str(e)}")
    
    async def execute_code_stream(
        self,
        code: Union[str, bytes],
        timeout: int = 30
    ) -> AsyncGenerator[StreamEvent, None]:
        """Execute Python code in the sandbox and stream the output.
        
        This method returns an async generator that yields StreamEvent objects containing
        the type of event and the associated data.
        
        Args:
            code: Python code to execute
            timeout: Maximum execution time in seconds
            
        Yields:
            StreamEvent objects with execution output/events
        """
        if not self.token or not self.sandbox_id:
            yield StreamEvent(type="error", data="Client not properly initialized. Call setup() first")
            return
            
        # Ensure sandbox is ready
        ready = await self.wait_for_ready()
        if not ready.success:
            yield StreamEvent(type="error", data=ready.error or "Sandbox not ready")
            return
            
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "code": code,
            "timeout": timeout
        }
        
        try:
            # Create a ClientTimeout object with all timeout settings
            timeout_settings = aiohttp.ClientTimeout(
                total=timeout + 30,  # Add buffer for connection overhead
                connect=30,
                sock_connect=30,
                sock_read=timeout + 30
            )
            
            async with aiohttp.ClientSession(timeout=timeout_settings) as session:
                async with session.post(
                    f"{self.base_url}/api/v1/sandbox/{self.sandbox_id}/execute/stream",
                    headers=headers,
                    json=data
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        yield StreamEvent(type="error", data=error_text)
                        return
                        
                    # Process the streaming response
                    async for line in response.content:
                        if line:
                            try:
                                event = json.loads(line.decode())
                                yield StreamEvent(type=event['type'], data=event['data'])
                                
                                # Stop if we receive an error or completed event
                                if event['type'] in ['error', 'completed']:
                                    break
                            except json.JSONDecodeError as e:
                                yield StreamEvent(type="error", data=f"Failed to parse event: {str(e)}")
                                break
                                
        except Exception as e:
            yield StreamEvent(type="error", data=f"Connection error: {str(e)}")
    
    async def execute_shell(
        self,
        command: str,
        args: Optional[List[str]] = None,
        timeout: int = 30
    ) -> SandboxResponse:
        """Execute a shell command in the sandbox.
        
        Args:
            command: The shell command to execute
            args: Optional list of arguments for the command
            timeout: Maximum execution time in seconds
            
        Returns:
            SandboxResponse containing execution results
        """
        if not self.token or not self.sandbox_id:
            return SandboxResponse(success=False, error="Client not properly initialized. Call setup() first")
            
        # Ensure sandbox is ready
        ready = await self.wait_for_ready()
        if not ready.success:
            return ready
            
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "command": command,
            "args": args or [],
            "timeout": timeout
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/api/v1/sandbox/{self.sandbox_id}/execute/shell",
                    headers=headers,
                    json=data
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        return SandboxResponse(success=False, error=error_text)
                    
                    # Parse the response
                    result = await response.json()
                    return SandboxResponse(success=True, data=result)
                    
        except Exception as e:
            return SandboxResponse(success=False, error=f"Connection error: {str(e)}")
    
    async def cleanup(self) -> SandboxResponse:
        """Delete the sandbox.
        
        Returns:
            SandboxResponse indicating success/failure of cleanup
        """
        if not self.token or not self.sandbox_id:
            return SandboxResponse(success=True)
            
        headers = {"Authorization": f"Bearer {self.token}"}
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                f"{self.base_url}/api/v1/sandbox/{self.sandbox_id}",
                headers=headers
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    self.sandbox_id = None
                    return SandboxResponse(success=True, data=data)
                else:
                    text = await response.text()
                    return SandboxResponse(success=False, error=text) 