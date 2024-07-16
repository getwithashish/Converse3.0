# Converse3.0

## AI Chat Bot with Gemini AI using Python and Flask

This project demonstrates how to build an AI-powered chat bot using Gemini AI from Google, integrated with Python and Flask. The bot supports user registration, authentication with JWT tokens, and interaction through a RESTful API. It utilizes PostgreSQL for data storage and can be run locally or in a Docker container.

## Technologies Used

- Python: Programming language used for backend development.
- Flask: Lightweight web framework for creating web applications in Python.
- PostgreSQL: Open-source relational database for data storage.
- Docker: Optional for containerization and easy deployment.
- Google Gemini API: Provides generative AI capabilities for natural language processing.

## Setup

### Prerequisites

- Python 3.10+
- PostgreSQL
- Docker and Docker Compose (Optional)

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

### API Endpoints

- POST `/register` - Register a new user.
- POST `/login` - Authenticate and obtain JWT token.
- POST `/normal_chat_with_ai` - Chat with the AI using Gemini model.
- GET `/normal_chat_history_list` - Retrieve list of chat history.
- GET `/normal_chat_history?chat_id=<chat_id>` - Retrieve chat history by ID.
- DELETE `/normal_chat_history_list?chat_id=<chat_id>` - Delete chat history by ID.

#### Set up Google AI Studio and obtain API Key

- Visit [Google AI Studio](https://aistudio.google.com/), log in, and create an API key.
- Update .env file with the API key.

## Credits

- This project uses Google Gemini AI for generating responses in the chat bot.
- Built with Python, Flask, SQLAlchemy, and Docker.

## Contribution

Feel free to open issues or pull requests if you find any bugs or have improvements.
