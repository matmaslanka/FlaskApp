# Flask App
This project is a Flask-based REST API application designed to manage a simple To-Do list. The API provides CRUD.

## Installation

1. Move the project to your preferred directory.
2. Set up a virtual environment:
   python3 -m venv env <br/>
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install the dependencies from requirements.txt:
   `pip install -r requirements.txt`


## Running the project
1. To run the application, launch it by executing the `app.py` file.

## Usage
This project is a Flask-based REST API application designed to manage a simple To-Do list. The API provides CRUD (Create, Read, Update, Delete) operations for tasks, allowing users to interact with the to-do list programmatically. The main features include:

- **Creating a Task:** Users can create new tasks with title attribute.
- **Listing Tasks:** The API allows users to retrieve a list of all tasks or get specific task.
- **Updating a Task:** Users can update existing tasks, modifying title attribute.
- **Deleting a Task:** The API supports deleting a task from the to-do list.

#### The API follows REST conventions for its endpoints, such as:
- **GET /tasks** - for retrieving all tasks <br/>
- **POST /tasks** - for creating tasks e.g.: <br/>
{<br/>
"name": "Do the homework"<br/>
}<br/>
- **GET /tasks/<id>** - for retrieving specific task<br/>
- **PUT /tasks/<id>** - for updating a task e.g.: <br/>
{<br/>
	"name": "Make a bed"<br/>
}<br/>
- **DELETE /tasks/<id>** for removing a task

The app uses SQLite as the database to store and persist task data.

### To perform CRUD operations on the To-Do List API, you can use Postman or a similar API client.