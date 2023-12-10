# Create-venv-From-requirements.txt

Creates a virtual environment in the same directory as a requirements.txt file.

To use the create_venv.py script:
1. Move the create_venv.py file somewhere such as your ~/utilities path.
2.  Confirm that the ~/utilities folder or whatever path chosen is in your PATH. Adding the folder that contains create_venv.py to PATH is required to be able to execute the create_venv.py script from anywhere in Terminal.
3.  Make the command executable in Terminal with:
   * chmod +x ~/utilities/create_venv.py
   * If not using the ~/utilities folder, change ~/utilities to your create_venv.py folder path.
4. Then you will be able to execute create_venv.py from any directory without specifying the full path to the create_venv.py file.
* So for example you could be in any directory and execute the command: create_venv.py /Users/John/Desktop/Code/
* If /Users/John/Desktop/Code/ contains a requirements.txt file, the create_venv.py script will execute and create a venv, then print out in Terminal the next two commands that will activate the newly created venv and install the packages within the requirements.txt file.
