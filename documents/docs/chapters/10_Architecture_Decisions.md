# Architecture Decisions

## Model-View-Controller (MVC) Architecture

We have decided to use the Model-View-Controller (MVC) architecture for the application. The MVC architecture is a software design pattern that separates the application into three main components: the model, the view, and the controller. The model represents the data and business logic of the application, the view represents the user interface, and the controller acts as an intermediary between the model and the view. This separation of concerns helps to improve the maintainability, scalability, and testability of the application. It also allows for easier collaboration between developers, as each component can be developed independently.

## RESTful APIs

We have decided to use RESTful APIs for communication between the frontend and backend of the application. RESTful APIs are a set of architectural constraints that define how web services should be designed and implemented. They are based on the principles of statelessness, uniform interface, and resource-based architecture. RESTful APIs use standard HTTP methods such as GET, POST, PUT, and DELETE to perform operations on resources, and use standard data formats such as JSON or XML to represent data. This makes it easy to develop, test, and maintain the APIs, as well as allowing for interoperability with other systems and services.

## sqlalchemy

We have decided to use sqlalchemy as the Object Relational Mapper (ORM) for the application. sqlalchemy is a powerful and flexible ORM that provides a high-level interface for interacting with databases. It allows developers to work with database objects as Python objects, and provides support for complex queries, transactions, and data integrity constraints. sqlalchemy also provides support for multiple database backends, including PostgreSQL, MySQL, and SQLite, which makes it suitable for a wide range of applications. This will help us interact with the PostgreSQL database in a more efficient and reliable manner, as well as providing a more object-oriented approach to working with data.

## Single Page Application (SPA)

We have decided to use a Single Page Application (SPA) for the frontend of the application. An SPA is a web application that loads a single HTML page and dynamically updates the content as the user interacts with the application. This provides a more responsive and interactive user experience, as the page does not need to be reloaded every time the user performs an action. SPAs are also easier to develop and maintain, as they use a modular and component-based architecture. This allows for better code organization, reusability, and testability, as well as making it easier to scale and extend the application.

## Containerization

We have decided to use containerization for the deployment of the application. Containerization is a lightweight and portable technology that allows applications to be packaged into self-contained units called containers. Containers include everything needed to run the application, including the code, runtime, libraries, and dependencies. This makes it easy to deploy and scale the application, as containers can run on any system that supports containerization. Containerization also provides isolation and security for the application, as each container runs in its own environment and does not interfere with other containers. This helps to ensure consistency and reliability across different environments, as well as making it easier to manage and update the application.

## Continuous Integration and Continuous Deployment (CI/CD)

We have decided to use Continuous Integration and Continuous Deployment (CI/CD) for the development and deployment of the application. CI/CD is a set of practices and tools that automate the process of building, testing, and deploying software. Continuous Integration involves automatically building and testing the code whenever changes are made, to ensure that the code is working correctly. Continuous Deployment involves automatically deploying the code to production whenever changes are made, to ensure that the code is available to users. This helps to improve the quality, speed, and reliability of the development process, as well as reducing the risk of errors and downtime. It also allows for faster feedback and iteration, as changes can be deployed quickly and easily.

\clearpage
