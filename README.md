
You can access the deployed site at : https://location-validator.fly.dev/

Installation
To install and run the project locally, follow the steps below:

Install the required dependencies using pip:

pip install -r requirements.txt
Start the project by running the following command:

python3 manage.py runserver
This will start the project locally on your machine. You can access it by opening a web browser and navigating to http://localhost:8000.

Deployment
The Project Name can be deployed using Docker and the fly.io platform. The deployment process involves the following steps:

Ensure that you have Docker installed on your machine.

Build the Docker image using the provided Dockerfile:

docker build -t project_name .
Push the Docker image to a container registry of your choice.

Sign up for an account on fly.io and follow their documentation for deploying a Django application:

https://fly.io/django-beats/deploying-django-to-production/

The documentation will guide you through the process of deploying your project using the fly.io platform.

Database
The Project Name uses SQLite as its default database. SQLite is a lightweight, serverless, and self-contained database engine that is suitable for development and small-scale applications. For production deployments or larger applications, it is recommended to use a more robust database system like PostgreSQL or MySQL.

Contact
For any inquiries or questions, please contact CHINDUKURI VINAY via chvinay8288@gmail.com.

