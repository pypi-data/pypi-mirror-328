# AI Computer Python Client

A Python client for interacting with the AI Computer service. This client provides a simple interface for executing Python code in an isolated sandbox environment.

## Installation

```bash
pip install ai-computer-client
```

## Quick Start

```python
import asyncio
from ai_computer import SandboxClient

async def main():
    # Initialize the client
    client = SandboxClient()
    
    # Setup the client (gets token and creates sandbox)
    setup_response = await client.setup()
    if not setup_response.success:
        print(f"Setup failed: {setup_response.error}")
        return
        
    try:
        # Execute some code
        code = """
        print('Hello from AI Computer!')
        result = 42
        print(f'The answer is {result}')
        """
        
        # Stream execution
        async for event in client.execute_code_stream(code):
            if event.type == 'stdout':
                print(f"Output: {event.data}")
            elif event.type == 'stderr':
                print(f"Error: {event.data}")
            elif event.type == 'error':
                print(f"Execution error: {event.data}")
                break
            elif event.type == 'completed':
                print("Execution completed")
                break
    
    finally:
        # Clean up
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
```

## Features

- Asynchronous API
- Streaming execution output
- Automatic sandbox management
- Error handling and timeouts
- Type hints for better IDE support

## API Reference

### SandboxClient

The main client class for interacting with the AI Computer service.

#### Methods

- `setup()`: Initialize the client and create a sandbox
- `execute_code(code: str, timeout: int = 30)`: Execute code and return combined output
- `execute_code_stream(code: str, timeout: int = 30)`: Execute code and stream output
- `cleanup()`: Delete the sandbox
- `wait_for_ready()`: Wait for sandbox to be ready

## Development

### Running Tests

```bash
pip install -e ".[dev]"
pytest
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License 