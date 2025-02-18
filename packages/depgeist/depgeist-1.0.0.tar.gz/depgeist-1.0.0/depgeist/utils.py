import subprocess

def run_command(command):
    """Run a shell command and return the output"""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()