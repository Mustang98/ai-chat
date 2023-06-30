# AI-Chat
A simple prototype of the dialogue system with AI celebrities

## Demo
Try it yourself at http://35.193.20.238:8000/

## Getting Started
To build and run AI-Chat project using Docker, follow these steps:



1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/Mustang98/ai-chat.git
   cd ai-chat
   ```
2. Set `OPENAI_KEY` and `DATABASE_URL` variables in .env file:
   ```bash
   nano .env
   ```
3. Build the Docker image:
   ```bash
   docker build -t ai-chat-app .
   ```
4. Run the Docker container:
   ```bash
   docker run -p 8000:8000 ai-chat-app
   ```

That's it! Now you can access the application at http://localhost:8000

## Project Description
The server side of the project is implemented using FastAPI + Uvicorn. All data is stored in the PostgreSQL database. SQLAlchemy is used for interaction with DB via the ORM approach. Alembic is used to create migrations to DB and maintain linear history. There are 4 data entities represented as SQL tables:
- `User`: represents a user of the dialogue system. One user can have many dialogues - at most 1 with each character.
- `Character`: represents an AI character, which users can chat with.
- `Dialogue`: represents a dialogue between a particular user and character. The dialog contains 0 or more messages.
- `Message`: represents a message sent by a user or character in a particular dialog.
  
Detailed properties of the abovementioned entities, as well as their relations and SQL indexes, are available in the `/database/orm_models.py` file.

The client side is a web application implemented using Angular.js and Bootstrap. It consists of a single screen where the user can select an AI character and chat with it. When user opens application for the first time, server assigns him a unique `user_id` which is saved to the user's local storage. Later this id is used to retrieve user's dialogues history and keep dialogue state between sessions.

Client-server interaction is done via REST API. Server provides the following endpoints:
- `POST /users`: Create a new user
- `GET /characters`: Get list of AI characters
- `POST /dialogues`: Create a new dialogue or read an existing one
- `POST /messages`: Send a new message to the dialogue
  
Detailed API specification can be found here: http://35.193.20.238:8000/docs

Input-output data validation and parsing are performed by Pydantic using predefined structures located in `/structures`.

Dependency management is conducted by `poetry`.

For the dialogue engine, the server uses OpenAI API with the DaVinci-3 model.



## Project Structure
The project follows the following directory structure:

- `/clients`: Contains clients that interact with 3rd-party apps. Currently, there is only a client for OpenAI API.
- `/database`: Contains database engine and ORM models.
- `/frontend`: Contains the Angular.js frontend code.
- `/migrations`: Contains database migration scripts.
- `/routes`: Contains REST API endpoints and handlers.
- `/structures`: Contains Pydantic structures for CRUD operations via REST API.
- `.env`: `python-dotenv` file containing necessary environment variables.
- `Dockerfile`: Dockerfile for containerizing the application.
- `alembic.ini`: Configuration file for Alembic database migration tool.
- `main.py`: Main script to run the FastAPI server.
- `poetry.lock` and `pyproject.toml`: Dependency management files.
