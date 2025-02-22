"""Core functionality for DevOpsAI."""

import json
import logging
import platform
import subprocess
import time
from typing import List, TypeVar, Optional
import requests
from .config import get_api_url, get_api_key

T = TypeVar('T')

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Determine OS
SYSTEM = platform.system()

def extract_commands(response: str) -> List[str]:
    """
    Extract commands from a response string that contains a JSON-like list.
    
    Args:
        response: A string that includes a list of commands in JSON format
        
    Returns:
        A list of command strings
    """
    try:
        # Find the opening and closing brackets of the list
        start_idx = response.rfind('[')
        end_idx = response.rfind(']') + 1
        
        if start_idx >= 0 and end_idx > start_idx:
            # Extract the list portion and parse it as JSON
            commands_str = response[start_idx:end_idx]
            commands = json.loads(commands_str)
            return commands
        else:
            return []
    except (json.JSONDecodeError, ValueError):
        return []

def execute_commands(commands: List[str]) -> bool:
    """
    Execute a list of shell commands.
    
    Args:
        commands: List of command strings to execute
        
    Returns:
        True if all commands executed successfully, False otherwise
    """
    print(f"Executing {len(commands)} commands...\n {commands}")
    success = True
    
    for command in commands:
        print(f"Executing: {command}")
        start_time = time.time()
        
        try:
            # Split the command string into list of arguments
            cmd_args = command.split()
            
            # Execute the command and wait for it to complete
            process = subprocess.run(
                cmd_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            
            # Calculate execution time
            execution_time = time.time() - start_time
            
            # Print output
            if process.stdout:
                print(f"Output: {process.stdout}")
            
            logging.info(f"Command completed successfully in {execution_time:.4f} seconds\n")
            
        except subprocess.CalledProcessError as e:
            execution_time = time.time() - start_time
            print(f"Error: {e.stderr}")
            print(f"Command failed after {execution_time:.4f} seconds\n")
            success = False
        except Exception as e:
            execution_time = time.time() - start_time
            print(f"An unexpected error occurred: {str(e)}")
            print(f"Command failed after {execution_time:.4f} seconds\n")
            success = False
            
    return success

def call_api(command: str) -> Optional[dict]:
    """
    Call the AI API to generate a response based on the command and system.
    
    Args:
        command: The command to process
        
    Returns:
        API response as dictionary or None if request failed
    """
    try:
        api_url = get_api_url()
        api_key = get_api_key()
        
        payload = {
            "model": "DevopsAI",
            "prompt": f"{command} in {SYSTEM}",
            "stream": False,
            "parameters": {
                "temperature": 0.0,
                "top_p": 1.0,
                "max_tokens": 50,
                "stop": ["<think></think>"]
            }
        }

        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status() 
        return response.json()
    except ValueError as e:
        logging.error(str(e))
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None