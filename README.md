# Project Name: Urban Traffic Management System

## Project Description
This project is a RESTful API built with **Django** and **Django REST Framework**. Its purpose is to manage urban traffic data by tracking and logging information about vehicles, roads, traffic events, and real-time traffic data.

This system serves as the **backend** for a broader application.

## API Features

The API exposes the following endpoints to interact with the data:

-   `/traffic/roads/` : To manage information about roads.
-   `/traffic/vehicles/` : To manage vehicle information.
-   `/traffic/events/` : To manage traffic events (accidents, road work, etc.).
-   `/traffic/traffic_data/` : To log and retrieve real-time traffic data (speed, position).

Each endpoint supports standard REST API operations:
-   **GET** : To retrieve a list of resources or a specific resource.
-   **POST** : To create a new resource.
-   **PUT** : To update an existing resource.
-   **DELETE** : To delete a resource.

Search and filtering functionalities are enabled on the main endpoints. For example, you can search for a vehicle by its license plate.

## Technologies Used
-   **Python 3.13**
-   **Django 5.2.4**
-   **Django REST Framework**
-   **SQLite** (development database)

## How to Run the Project

Follow these steps to install and run the project locally:

1.  **Clone the GitHub repository**:
    ```bash
    git clone <Your GitHub repo URL>
    cd <your_folder_name>
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: If you don't have a requirements.txt file, create one with `pip freeze > requirements.txt`.*

3.  **Apply database migrations**:
    ```bash
    python manage.py makemigrations traffic
    python manage.py migrate
    ```

4.  **Create a superuser** (to access the admin interface and permissions):
    ```bash
    python manage.py createsuperuser
    ```

5.  **Start the development server**:
    ```bash
    python manage.py runserver
    ```

The server will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The API can be accessed at [http://127.0.0.1:8000/traffic/](http://127.0.0.1:8000/traffic/).