# Task Management API

A simple task management application built using **FastAPI** and **SQLAlchemy** for managing tasks. This API allows users to create, update, and view tasks with a variety of statuses. It supports **PostgreSQL** for persistent data storage.

## Features

- **Create tasks** with a title, description, and status.
- **Update tasks** by modifying the title or status.
- **Get a list of tasks** with pagination support.
- **Health check** endpoint to check API status.
- **Task statuses**: `pending`, `in-progress`, and `completed`.

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for interacting with the database.
- **PostgreSQL**: Relational database used for storing task data.
- **Pydantic**: Data validation library used by FastAPI.
- **Alembic**: Database migrations tool.

## Requirements

- Python 3.8+
- PostgreSQL
- Virtual environment (recommended)

### Steps to Follow

**Create a virtual environment:**

```python
python -m venv .venv
```

**Activate the virtual environment:**

```python
.\.venv\Scripts\activate
```

**Install dependencies:**

```python
pip install -r requirements.txt
```

**Configure the database:**

Create a `.env` file in the root directory of the project and add the following line:

```bash
DATABASE_URL=postgresql+psycopg2://postgres:admin123@localhost:5432/task_management

```

           **Replace `postgres:admin123` with your PostgreSQL username and password.**

**Run migrations**:

To set up the database schema, run Alembic migrations:

```python
alembic upgrade head
```

## Running the API

To start the FastAPI server locally, run the following command:

```python
uvicorn main:app --reload

```

The API will be available at `http://127.0.0.1:8000`. You can test the endpoints in the browser or use a tool like [Postman](https://www.postman.com/) or [Curl](https://curl.se/).

### Health Chec

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Checks if the API is running and the database is accessible.
    
    **Response:**
    
    ```json
    
    {
      "status": "healthy"
    }
    
    ```
    

### Create a Task

- **Endpoint**: `/tasks/`
- **Method**: `POST`
- **Description**: Creates a new task with the provided title, description, and status.
    
    **Request:**
    
    ```json
    
    {
      "title": "first",
      "description": "This is the first task",
      "status": "pending"
    }
    
    ```
    
    **Response:**
    
    ```json
    
    {
      "id": "ba8c9ba7-fd92-439e-b431-8d0130b54c04",
      "title": "first",
      "description": "This is the first task",
      "status": "pending",
      "created_at": "2025-04-08T15:09:29.264783",
      "updated_at": "2025-04-08T15:09:29.264783"
    }
    
    ```
    

### Update a Task

- **Endpoint**: `/tasks/{task_id}`
- **Method**: `PUT`
- **Description**: Updates the title or status of an existing task.
    
    **Request:**
    
    ```json
    
    {
      "title": "Updated title",
      "status": "in-progress"
    }
    
    ```
    
    **Response:**
    
    ```json
    
    {
      "id": "ba8c9ba7-fd92-439e-b431-8d0130b54c04",
      "title": "Updated title",
      "description": "This is the first task",
      "status": "in-progress",
      "created_at": "2025-04-08T15:09:29.264783",
      "updated_at": "2025-04-08T15:09:29.264783"
    }
    
    ```
    

### List Tasks (with Pagination)

- **Endpoint**: `/tasks/`
- **Method**: `GET`
- **Description**: Retrieves a paginated list of tasks. Supports pagination through the `next` field for fetching the next page of tasks.
    
    **Request:**
    
    ```bash
    
    GET /tasks/?page=1&limit=10
    
    ```
    
    **Response:**
    
    ```json
    
    {
      "tasks": [
        {
          "id": "ba8c9ba7-fd92-439e-b431-8d0130b54c04",
          "title": "first",
          "description": "This is the first task",
          "status": "pending",
          "created_at": "2025-04-08T15:09:29.264783",
          "updated_at": "2025-04-08T15:09:29.264783"
        },
        {
          "id": "e8b6d05d-7bc2-4a71-b1b0-495ca4f8b075",
          "title": "second",
          "description": "This is the second task",
          "status": "in-progress",
          "created_at": "2025-04-08T15:11:45.123456",
          "updated_at": "2025-04-08T15:11:45.123456"
        }
      ],
      "next": "http://127.0.0.1:8000/tasks/?page=2&limit=10"
    }
    
    ```
    
    - **tasks**: List of task objects.
    - **next**: URL to fetch the next page of tasks, if available.

## Database Schema

### `Task` Table

| Column | Type | Description |
| --- | --- | --- |
| `id` | UUID | Unique identifier for each task |
| `title` | String | Title of the task |
| `description` | Text | Description of the task (optional) |
| `status` | Enum(`pending`, `in-progress`, `completed`) | Current status of the task |
| `created_at` | TIMESTAMP | Timestamp when the task was created |
| `updated_at` | TIMESTAMP | Timestamp when the task was last updated |

## Troubleshooting

- **Database connection issues**: Make sure that PostgreSQL is running and the connection URL is correct.
- **Migrations**: If you encounter issues with migrations, try running:
    
    ```bash
    
    alembic upgrade head
    
    ```
    
- **Internal server errors**: Check the logs for stack traces to pinpoint any issues with your code or the database.