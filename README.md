# Converse3.0

## AI Chat Bot with Gemini AI using Python and Flask

This project demonstrates how to build an AI-powered chat bot using Gemini AI from Google, integrated with Python and Flask. The bot supports user registration, authentication with JWT tokens, and interaction through a RESTful API. It utilizes PostgreSQL for data storage and can be run locally or in a Docker container.

### Technologies Used

- Python: Programming language used for backend development.
- Flask: Lightweight web framework for creating web applications in Python.
- PostgreSQL: Open-source relational database for data storage.
- Docker: Optional for containerization and easy deployment.
- Google Gemini API: Provides generative AI capabilities for natural language processing.

## Table of Contents

- [GIFs and Screenshots](#gifs-and-screenshots)
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Update Configurations in .env](#update-configurations-in-env)
  - [Run using Docker](#run-using-docker)
  - [Run using Docker Compose](#run-using-docker-compose)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Credits](#credits)
- [Contribution](#contribution)

## GIFs and Screenshots

![Converse-Website](demo/Website.gif)

### Landing Page

![Landing Page](demo/LandingPage.gif)

### Registration Page

![Registration Page](demo/RegistrationPage.gif)

### Login Page

![Login Page](demo/LoginPage.gif)

### Homepage

![Homepage](demo/HomePage.gif)

### Normal AI Chat Page

![Normal AI Chat Page](demo/NormalChatWithAIPage.png)

## Project Structure

```
├── converse_backend
│   ├── client
│   │   └── ai_models
│   │   └── gemini
│   ├── controllers
│   ├── models
│   ├── service
│   └── utils
├── converse_frontend
│   ├── public
│   └── src
│   ├── assets
│   ├── components
│   │   ├── chatResponse
│   │   ├── landingpage
│   │   ├── layout
│   │   ├── shared
│   │   │   └── navBar
│   │   ├── ui
│   │   └── username
│   ├── pages
│   │   ├── auth
│   │   │   ├── register
│   │   │   │   └── components
│   │   │   └── signin
│   │   │   └── components
│   │   ├── converseChat
│   │   ├── converseChatDb
│   │   │   └── components
│   │   ├── converseChatDoc
│   │   │   └── components
│   │   ├── dashboard
│   │   │   └── components
│   │   └── landing-page
│   │   └── components
│   ├── providers
│   ├── routes
│   │   └── hooks
│   └── types
└── demo
```

## Setup

### Prerequisites

- Python 3.10+
- PostgreSQL
- Docker and Docker Compose (Optional)

### Update Configurations in .env

```
APP_SECRET_KEY=app_secret_here
JWT_SECRET_KEY=jwt_secret_here

CORS_ORIGINS=http://localhost:5173,http://20.44.62.11:5173

DATABASE_URI=postgresql://postgres:password@localhost:5432/postgres

HOST=127.0.0.1
PORT=5000

GOOGLE_API_KEY=AIzaSyBqVVcd85PoRkGmojC4vTRBfwN4X-fnic9
GEMINI_MODEL_NAME=gemini-pro

```

#### To obtain API key from Google

- Visit [Google AI Studio](https://aistudio.google.com/), log in, and create an API key.
- Update .env file with the API key.

### Run using Docker

#### Backend

Go to `converse_backend` directory

```bash
docker build -t converse-backend-docker-image .
docker run -d -p 8000:8000 --name converse-backend converse-backend-docker-image

```

#### Frontend

Go to `converse_frontend` directory

```bash
docker build -t convers-frontend-docker-image -f Dockerfile.dev .
docker run -d -p 5173:5173 --name converse-frontend convers-frontend-docker-image

```

### Run using Docker Compose

#### For Development

```bash
docker compose --profile dev up
```

#### For Production

```bash
docker compose --profile prod up
```

> Note: Add the configurations in `.prod.env` for running the backend

> Note: For production, use production-grade servers like nginx to serve the frontend

### Installation

#### Clone the repository

```bash
git clone <repository_url>
cd <project_folder>

```

#### Setup PostgreSQL

- Install PostgreSQL and create a database.
- Update .env file with PostgreSQL database URI.

#### Set up Python Virtual Environment

```bash
python -m venv venv

```

In Linux

```bash
source venv/bin/activate
```

In Windows

```bash
venv\Scripts\activate
```

#### Install Python Dependencies

```bash
pip install -r requirements.txt

```

#### Run the application

```bash
python main.py

```

The development server will be hosted on http://localhost:8000 by default.

## API Endpoints

| Endpoint                                      | Method | Description                         |
| --------------------------------------------- | ------ | ----------------------------------- |
| `/register`                                   | POST   | Register a new user                 |
| `/login`                                      | POST   | Authenticate and obtain JWT token   |
| `/normal_chat_with_ai`                        | POST   | Chat with the AI using Gemini model |
| `/normal_chat_history_list`                   | GET    | Retrieve list of chat history       |
| `/normal_chat_history?chat_id=<chat_id>`      | GET    | Retrieve chat history by ID         |
| `/normal_chat_history_list?chat_id=<chat_id>` | DELETE | Delete chat history by ID           |
| `/normal_chat_history_list`                   | DELETE | Delete all the chats of that user   |

### Detailed Endpoint Descriptions

#### POST `/register`

**Description**: Register a new user.

**Request Body**:

```json
{
  "username": "string",
  "password": "string"
}
```

**Response Body**:

```json
{
  "message": "User has been successfully registered"
}
```

#### POST `/login`

**Description**: Authenticate and obtain JWT token.

**Request Body**:

```json
{
  "username": "string",
  "password": "string"
}
```

**Response Body**:

```json
{
  "access_token": "jwt_token_here"
}
```

#### POST `/normal_chat_with_ai`

**Description**: Chat with the AI using Gemini model.

**Request Body**:

```json
{
  "message": "string"
}
```

**Auth Headers**:

```
Authorization: Bearer your_jwt_token_here
```

**Response Body**:

```json
{
  "ai_response": "response_here",
  "chat_id": "chat_id_here"
}
```

#### GET `/normal_chat_history_list`

**Description**: Retrieve list of chat history.

**Auth Headers**:

```
Authorization: Bearer your_jwt_token_here
```

**Response Body**:

**200 OK**

```json
{
  "data": [
    {
      "chat_id": "chat_id_here",
      "chat_name": "chat_name_here"
    }
  ],
  "message": "Chat history list has been successfully retrieved"
}
```

#### GET `/normal_chat_history?chat_id=<chat_id>`

**Description**: Retrieve chat history by ID.

**Auth Headers**:

```
Authorization: Bearer your_jwt_token_here
```

**Response Body**:

**200 OK**

```json
{
  "data": {
    "chat_history": [
      {
        "role": "user",
        "text": "promp1_here"
      },
      {
        "role": "model",
        "text": "response1_here"
      },
      {
        "role": "user",
        "text": "prompt2_here"
      },
      {
        "role": "model",
        "text": "response2_here"
      }
    ],
    "chat_id": "34"
  },
  "message": "Chat history has been successfully retrieved"
}
```

#### DELETE `/normal_chat_history_list?chat_id=<chat_id>`

**Description**: Delete chat history by ID.

**Auth Headers**:

```
Authorization: Bearer your_jwt_token_here
```

**Response Body**:

**204 NO CONTENT**

#### DELETE `/normal_chat_history_list`

**Description**: Delete all the chats.

**Auth Headers**:

```
Authorization: Bearer your_jwt_token_here
```

**Response Body**:

**204 NO CONTENT**

## Credits

- This project uses Google Gemini AI for generating responses in the chat bot.
- Built with Python, Flask, SQLAlchemy, and Docker.

## Contribution

Feel free to open issues or pull requests if you find any bugs or have improvements.
