# DoorLock CLI

A Python-based command-line interface (CLI) for managing a door lock system. This application allows users to set a knock sequence as the passcode and then unlock the door by repeating the sequence. The system includes security features like a maximum number of attempts and a punishment time during which the door lock cannot be attempted again.

## Project Structure

- **`main.py`**: The entry point for the CLI. Initializes the `DoorLock` object and starts the polling process.
- **`doorlock.py`**: Contains the `DoorLock` class that handles the logic for setting a knock sequence, checking it, and enforcing security measures.
-  **`util.py`**: Contains the ```check_knock()``` and ```parse_knock()``` helper functions. ```check_knock()``` is the fundemental time-keeping function for our doorlock. 

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/doorlock-cli.git
    ```

2. Navigate to the project directory:

    ```bash
    cd doorlock-cli
    ```

### Running the Program

To run the door lock CLI, simply execute the `main.py` file:

```bash
python3 main.py




