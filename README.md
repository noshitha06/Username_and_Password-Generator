# Username and Password Generator

This is a Python console application that can generate usernames from a file and create random passwords.

## Features

* **Username Generation**: Reads a file containing names and student IDs to create unique usernames.
* **Password Generation**: Generates a random password that includes numbers, uppercase and lowercase letters, and a special character.
* **Menu-Driven Interface**: Provides a simple menu for the user to choose between generating usernames, creating a password, or quitting the program.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [your-repository-url]
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd [your-project-directory]
    ```
3.  **Run the script:**
    ```bash
    python BlackGudhibandiMod4Project-1.py
    ```

## Usage

When you run the program, a menu will appear with three options:

* **'u'**: To create usernames. You will be prompted to enter a file name (e.g., `names.txt`). The program will then read this file, generate usernames, and write them to a new file named `username.txt`.
* **'p'**: To generate a new password. The program will print a random password to the console.
* **'q'**: To quit the program.

### Example Input File Format (for 'u' command)

The program expects a file where each line contains a first name, last name, and a student ID, separated by commas.
