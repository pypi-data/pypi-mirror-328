"""Command-line interface for DevOpsAI."""

import sys
import logging
from .core import call_api, extract_commands, execute_commands

def main():
    """Main entry point for the DevOpsAI CLI."""
    if len(sys.argv) > 1:
        command = ' '.join(sys.argv[1:])
        logging.info(f"Processing command: {command}")

        api_response = call_api(command)
        if not api_response:
            logging.error("API request failed. Exiting.")
            sys.exit(1)
            
        response_text = api_response["response"]
        executable_commands = extract_commands(response_text)

        print(executable_commands)

        if executable_commands:
            success = execute_commands(executable_commands)
            if not success:
                logging.error("One or more commands failed to execute.")
                sys.exit(1)
        else:
            logging.error("Failed to extract executable commands.")
            print(response_text)
            sys.exit(1)
    else:
        logging.error("Usage: ai <your query>")
        sys.exit(1)
    
    return 0

if __name__ == "__main__":
    # This allows running the CLI directly during development
    sys.exit(main())