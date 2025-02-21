import sys
import os

ENV_PATH = os.path.expanduser("~/.nogeese/pybscope/env/pybscope-env")

def activate_env():
    """Activates the pybscope virtual environment."""
    if not os.path.exists(ENV_PATH):
        print("Error: pybscope environment not found! Run the installer first.")
        sys.exit(1)

    os.system(f"source {ENV_PATH}/bin/activate && bash")

def deactivate_env():
    """Deactivates the pybscope virtual environment."""
    os.system("deactivate")

def main():
    """Handles command-line arguments for pybscope."""
    if len(sys.argv) > 1:
        if sys.argv[1] == "env":
            activate_env()
        elif sys.argv[1] == "env-get-out":
            deactivate_env()
        else:
            print("Unknown command. Use 'pybscope env' or 'pybscope env-get-out'.")
            sys.exit(1)
    else:
        print("pybscope command-line tool")
        print("Usage:")
        print("  pybscope env           - Enter the pybscope environment")
        print("  pybscope env-get-out   - Exit the pybscope environment")
        sys.exit(0)
