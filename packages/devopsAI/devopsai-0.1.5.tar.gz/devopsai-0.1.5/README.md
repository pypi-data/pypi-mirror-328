# DevOpsAI

A command-line interface for interacting with AI models to assist with DevOps tasks.

## Configuration

DevOpsAI requires an API URL to function. You can configure it in several ways:

### Using environment variables:

```bash
# Set the API URL
export DEVOPSAI_API_URL="https://your-api-endpoint.com/v1/completions"

# Set the API key (if required)
export DEVOPSAI_API_KEY="your-api-key"
```

## Usage

Basic usage:
```bash
ai <your query>
```

Example:
```bash
ai check python version
```

## Connecting with Different Models

### Ollama
```bash
# Set Ollama API URL
export DEVOPSAI_API_URL="http://localhost:11434/api/generate"

# Check Ollama status
ai check the python version
```

For more information about Ollama, visit the [official Ollama GitHub repository](https://github.com/ollama/ollama/blob/main/README.md).

### Other LLM Support

Support for additional models is coming soon:
- OpenAI
- Anthropic Claude
- DeepSeek
- Gemini
- And more!