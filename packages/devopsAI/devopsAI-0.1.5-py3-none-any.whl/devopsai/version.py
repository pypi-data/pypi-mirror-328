"""Version checking utility for devopsAI."""

import sys
import os

def get_version():
    return '0.1.5'

def main():
    """
    Print the package version.
    Can be used as a CLI entry point.
    """
    version = get_version()
    
    if "Error" in version:
        print(version, file=sys.stderr)
        sys.exit(1) 

    print(f"devopsAI version: {version}")
    print('''\nDevOpsAI - A utility for executing system commands via API.
Usage: ai <your query>

For more details, visit: https://github.com/Dineshkanna654/devops
    ''')

if __name__ == '__main__':
    main()
