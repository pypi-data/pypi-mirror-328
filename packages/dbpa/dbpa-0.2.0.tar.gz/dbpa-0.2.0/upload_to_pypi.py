import os
import sys
from pathlib import Path
import subprocess

def read_env_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip().startswith('PYPI_API_TOKEN_2='):
                return line.strip().split('=', 1)[1]
    return None

def main():
    # Get the token
    env_path = Path('.env')
    if not env_path.exists():
        print("Error: .env file not found")
        sys.exit(1)
        
    token = read_env_file(env_path)
    if not token:
        print("Error: PYPI_API_TOKEN_2 not found in .env")
        sys.exit(1)
        
    # Set up environment
    os.environ['TWINE_USERNAME'] = '__token__'
    os.environ['TWINE_PASSWORD'] = token
    
    # Upload to PyPI
    cmd = ['twine', 'upload', '--verbose', 'dist/*']
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print(f"Exit code: {result.returncode}")
    except Exception as e:
        print(f"Error during upload: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
