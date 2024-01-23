# Polls_app_auth

Welcome to Polls_app_auth! This Python project is a web application that allows users to create and participate in polls with authentication features.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Project Description

Polls_app_auth is designed to be a secure and user-friendly platform for creating and participating in polls. The project emphasizes the importance of authenticated users to maintain the integrity of poll data.

### Importance of the Project

Polls are a crucial tool for collecting opinions and feedback from a diverse audience. Polls_app_auth enhances this experience by adding authentication, ensuring that only authorized users can create or manage polls.

## Installation

To run Polls_app_auth locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tshamala-pathy/Polls_app_auth.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Polls_app_auth
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Configure environment variables:**

    Create a `.env` file in the root directory and add the necessary variables, such as database connection details and authentication secrets.

7. **Run the application:**

    ```bash
    python app.py
    ```

Visit `http://localhost:3000` to access the application.

## Usage

1. Create an account or log in if you already have one.
2. Navigate to the polls section.
3. Create a new poll by providing the necessary details.
4. Share the poll link with your audience.
5. Participants can vote after authenticating.

## Screenshots
![Login Page](![Screenshot 2023-11-09 233823](https://github.com/tshamala-pathy/Polls_app_auth/assets/146994366/e699b5af-369c-46f6-a6d1-dfdfc5ddaef2)
)
![Poll Creation](![Screenshot 2023-11-09 233914](https://github.com/tshamala-pathy/Polls_app_auth/assets/146994366/42759a4f-23c9-49be-8e3c-5414326b5112)
)
![Voting](![Screenshot 2023-11-09 233934](https://github.com/tshamala-pathy/Polls_app_auth/assets/146994366/2d68adf4-3890-4d5c-957c-ff6c847cff25)
)

Include screenshots of your application in action. These could showcase the login page, poll creation, and participation process. Images help users understand the look and feel of your application.

## Contributing

Contributions are welcome! Please follow the [Contributing Guidelines](CONTRIBUTING.md) to contribute to this project.

## Credits

This project is maintained by Tshamala Pathy. If you have any questions or need assistance, feel free to reach out.

- [Github](https://github.com/tshamala-pathy)

## License

This project is licensed under the [MIT License](LICENSE).
