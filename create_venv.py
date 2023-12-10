import os
import sys
import subprocess

def create_venv(project_dir):
    venv_dir = os.path.join(project_dir, 'venv')

    # Create virtual environment
    subprocess.run([sys.executable, '-m', 'venv', venv_dir], check=True)

    # Commands to activate venv and install requirements
    activate_command = '. ' + os.path.join(venv_dir, 'bin', 'activate') if os.name != 'nt' else os.path.join(venv_dir, 'Scripts', 'activate')
    install_command = f'pip install -r {os.path.join(project_dir, "requirements.txt")}'

    return activate_command, install_command

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python create_venv.py <project_directory>")
        sys.exit(1)

    project_dir = sys.argv[1]
    activate_command, install_command = create_venv(project_dir)

    print("\nVirtual environment created.")
    print("\nRun the following commands in your terminal:")
    print(activate_command)
    print(install_command)
