# Django Social Network API Project

This repository contains a Django-based API project. It offers various endpoints for managing users, sending friend requests, and accepting or rejecting friend requests. The project is designed to handle authentication and user management, making it a robust backend solution.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and registration
- Search for users by email or name
- Send and manage friend requests
- List pending friend requests
- Accept and reject friend requests
- Manage friend lists

## Installation

To set up and run this Django API project on your local machine, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/as4c/Social-network.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Social-network
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv env
   ```

4. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Setup Database:**

   - Configure the database settings in the `settings.py` file according to your setup.

7. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

8. **Start the Server:**

   ```bash
   python manage.py runserver
   ```

9. **Access the API in your Browser or API Client:**

   The server will start at `http://127.0.0.1:8000`. You can access the documentation and test the endpoints using tools like Postman.

## Usage

Once the server is up and running, you can use the following endpoints to manage the application:

- **User Authentication:**
  - `/api/v1/users/login/`: POST request for user login.
  - `/api/v1/users/signup/`: POST request for user registration.

- **User Search:**
  - `/api/v1/users/search/`: GET request to search users by email or name.

- **Friend Request Management:**
  - `/api/v1/users/friend/send-request/`: POST request to send a friend request.
  - `/api/v1/users/friend/send-pending/`: GET request to list pending friend requests.
  - `/api/v1/users/friend/<int:pk>/accept-request/`: POST request to accept a friend request.
  - `/api/v1/users/friend/<int:pk>/reject-request/`: POST request to reject a friend request.

- **Friends List:**
  - `/api/v1/users/friends/`: GET request to list all accepted friends.

For detailed information on each endpoint, check the API documentation.

## Contributing

Feel free to fork this repository and make changes. Follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them.
4. Push to the branch: `git push origin feature-branch`.
5. Create a pull request.

## License

This project is licensed under the MIT License.

