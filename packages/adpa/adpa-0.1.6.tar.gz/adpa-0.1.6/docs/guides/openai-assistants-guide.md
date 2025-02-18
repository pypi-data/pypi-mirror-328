# OpenAI Assistants Guide

Version 0.7.0

## Overview

The OpenAI Assistants API provides a powerful way to create AI assistants that can perform various tasks using different capabilities. This guide covers the key concepts and provides practical code examples for implementing assistants.

## Key Concepts

1. **Assistant**: A persistent entity with specific instructions and capabilities
2. **Thread**: A conversation session that maintains context
3. **Message**: Individual messages within a thread
4. **Run**: Execution of the assistant's response to messages
5. **Tools**: Additional capabilities like code interpretation, retrieval, and function calling

## Code Examples

### 1. Creating an Assistant

```python
from openai import OpenAI
client = OpenAI()

# Create an assistant with specific capabilities
assistant = client.beta.assistants.create(
    name="Python Coding Assistant",
    instructions="You are a Python programming expert. Help users write clean, efficient code.",
    model="gpt-4-1106-preview",
    tools=[
        {"type": "code_interpreter"},
        {"type": "retrieval"}
    ]
)
```

### 2. Managing Threads and Messages

```python
# Create a new thread
thread = client.beta.threads.create()

# Add a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Help me write a Python function to calculate Fibonacci numbers."
)

# Run the assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Wait for completion
run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
)

# Get messages
messages = client.beta.threads.messages.list(thread_id=thread.id)
```

### 3. Using Function Calling

```python
# Define available functions
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# Create assistant with function calling
assistant = client.beta.assistants.create(
    name="Weather Assistant",
    instructions="Help users get weather information.",
    model="gpt-4-1106-preview",
    tools=tools
)

# Implement function handler
def handle_function_call(name, arguments):
    if name == "get_weather":
        # Implement actual weather API call
        return f"Weather data for {arguments['location']}"
```

### 4. File Handling and Retrieval

```python
# Upload a file
file = client.files.create(
    file=open("data.pdf", "rb"),
    purpose="assistants"
)

# Create assistant with file access
assistant = client.beta.assistants.create(
    name="Research Assistant",
    instructions="Help analyze research papers.",
    model="gpt-4-1106-preview",
    tools=[{"type": "retrieval"}],
    file_ids=[file.id]
)
```

### 5. Complete Working Example

```python
from openai import OpenAI
import time

class AssistantManager:
    def __init__(self, api_key=None):
        self.client = OpenAI(api_key=api_key)
        
    def create_assistant(self, name, instructions, model="gpt-4-1106-preview", tools=None):
        """Create a new assistant with specified configuration."""
        return self.client.beta.assistants.create(
            name=name,
            instructions=instructions,
            model=model,
            tools=tools or []
        )
    
    def create_thread(self):
        """Create a new conversation thread."""
        return self.client.beta.threads.create()
    
    def send_message(self, thread_id, content):
        """Send a message to the thread."""
        return self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=content
        )
    
    def run_assistant(self, thread_id, assistant_id):
        """Run the assistant and wait for completion."""
        run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
        
        while True:
            run_status = self.client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )
            
            if run_status.status == 'completed':
                break
            elif run_status.status == 'failed':
                raise Exception("Assistant run failed")
            
            time.sleep(1)
        
        return run
    
    def get_messages(self, thread_id):
        """Get all messages in the thread."""
        return self.client.beta.threads.messages.list(
            thread_id=thread_id
        )

# Usage example
if __name__ == "__main__":
    manager = AssistantManager()
    
    # Create an assistant
    assistant = manager.create_assistant(
        name="Coding Helper",
        instructions="Help with Python programming questions",
        tools=[{"type": "code_interpreter"}]
    )
    
    # Create a thread
    thread = manager.create_thread()
    
    # Send a message
    manager.send_message(
        thread_id=thread.id,
        content="Write a Python function to sort a list of numbers."
    )
    
    # Run the assistant
    manager.run_assistant(thread.id, assistant.id)
    
    # Get responses
    messages = manager.get_messages(thread.id)
    for msg in messages:
        print(f"{msg.role}: {msg.content[0].text.value}")

## Best Practices

1. **Error Handling**
   - Always implement proper error handling for API calls
   - Handle rate limits and timeouts gracefully
   - Check run status for failures

2. **Resource Management**
   - Clean up unused files and assistants
   - Implement proper thread management
   - Monitor API usage

3. **Security**
   - Never expose API keys in code
   - Validate user inputs
   - Implement proper access controls

4. **Performance**
   - Reuse threads when appropriate
   - Implement caching where possible
   - Use streaming for long responses

## Common Use Cases

1. **Code Generation and Review**
   ```python
   assistant = client.beta.assistants.create(
       name="Code Reviewer",
       instructions="Review Python code for best practices and suggest improvements.",
       model="gpt-4-1106-preview",
       tools=[{"type": "code_interpreter"}]
   )
   ```

2. **Document Analysis**
   ```python
   assistant = client.beta.assistants.create(
       name="Document Analyzer",
       instructions="Analyze documents and extract key information.",
       model="gpt-4-1106-preview",
       tools=[{"type": "retrieval"}]
   )
   ```

3. **Interactive Tools**
   ```python
   assistant = client.beta.assistants.create(
       name="Tool Assistant",
       instructions="Help users with various tools and calculations.",
       model="gpt-4-1106-preview",
       tools=[
           {"type": "code_interpreter"},
           {"type": "function"}
       ]
   )
   ```

## Limitations and Considerations

1. **Rate Limits**
   - Monitor API usage
   - Implement exponential backoff for retries
   - Consider implementing queue systems for high-volume applications

2. **Cost Management**
   - Track token usage
   - Implement budget controls
   - Use appropriate models based on needs

3. **Model Capabilities**
   - Different models have different capabilities
   - Consider using GPT-4 for complex tasks
   - Test thoroughly with your specific use case

## Additional Resources

1. [OpenAI Assistants API Documentation](https://platform.openai.com/docs/assistants/overview)
2. [OpenAI Python Library](https://github.com/openai/openai-python)
3. [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

## Troubleshooting

Common issues and solutions:

1. **Rate Limiting**
```python
import time
from openai import RateLimitError

def retry_with_exponential_backoff(func, max_retries=3):
    """Retry a function with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
```

2. **Thread Management**
```python
def cleanup_old_threads(client, max_age_days=7):
    """Clean up old threads."""
    old_threads = client.beta.threads.list(
        created_before=time.time() - (max_age_days * 24 * 60 * 60)
    )
    for thread in old_threads:
        client.beta.threads.delete(thread.id)
```

3. **File Management**
```python
def manage_files(client, file_path, purpose="assistants"):
    """Upload and manage files."""
    try:
        file = client.files.create(
            file=open(file_path, "rb"),
            purpose=purpose
        )
        return file
    finally:
        # Implement cleanup logic
        pass
```

Remember to regularly check the [OpenAI Status Page](https://status.openai.com/) for any service disruptions or updates.
