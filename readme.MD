# Blood Bank Management System

The Blood Bank Management System is a command-line interface (CLI) application that allows you to manage blood donors and their donations. It provides functionality to add new donors, update existing donations, and delete donors from the system. The application uses three tables: `donors`, `blood-groups`, and `blood-volumes`.

## Features

- Add a new donor by providing their name, blood group, volume, and date of donation.
- Update the donation volume for an existing donor.
- Delete a donor by their unique ID.
- List all the donations in the system.

## Prerequisites

To use this CLI application, you need to have the following installed:

- Python environment.Run;
   * pipenv install
   * pipenv shell
   * pip install SQLAlchemy
- You should have the following installed;
   * click==8.1.7
   * greenlet==2.0.2
   * SQLAlchemy==2.0.20
- Git (optional, for cloning the repository)

## Installation

1. Clone the repository.
2. Create a Python virtual environment.
3. Activate the virtual environment.
4. Install the required dependencies.

## Usage

1. Run the CLI application by executing the python3 main.py command from the project's root directory from the VSCode text editor terminal, most preferrably.

2. The application will prompt you to enter the required information for blood donation, such as the donor's name, blood group, volume, and date.

3. Use the available commands to perform different operations:

- `add-donation`: Add a new donor and their donation.
- `update-donation`: Update the donation volume for an existing donor.
- `delete-donation`: Delete a donor by their ID.

4. Follow the prompts and enter the required information as needed.Remember , for each of the above commands, preceed it with python3 main.py [COMMAND].

## Contributing

Contributions to this project are welcome! If you would like to contribute, just create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).