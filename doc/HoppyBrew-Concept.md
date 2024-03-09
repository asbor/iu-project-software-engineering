# HoppyBrew Documentation

## Introduction

HoppyBrew stands as a dedicated web application crafted for brewing enthusiasts and homebrewers, specifically designed for self-hosting. Drawing inspiration from [Brewfather](https://brewfather.app/), it operates seamlessly within a Docker container and comes with no associated costs. Developed as part of the Software Engineering course at the Faculty of Informatics, International University of Applied Sciences Bad Honnef - Bonn, HoppyBrew addresses the critical need for streamlined management of brewing processes.

Born from the personal journey of the creator as a homebrewer venturing into self-hosting, HoppyBrew aims to be a bespoke solution. This web application empowers users to independently create, share, and manage their beer recipes, eliminating any dependence on subscription-based services like Brewfather.

What sets HoppyBrew apart is its self-hosted architecture within a Docker container, providing users with easy account creation, login, and seamless control over recipe-related tasks such as creation, editing, and deletion. The application also boasts a user-friendly search function for recipes based on name, style, or ingredients.

Moving beyond mere recipe management, HoppyBrew integrates seamlessly with iSpindel over Ethernet, allowing users to actively monitor and track the fermentation process. It further aids users in keeping a meticulous record of their brewing inventory and generates shopping lists based on selected recipes, thereby elevating the overall brewing experience for users.

## Features

### Recipe Management

HoppyBrew offers a comprehensive recipe management system, allowing users to create, edit, and delete recipes. The application also provides a user-friendly search function for recipes based on name, style, or ingredients.

### Inventory Management

The application enables users to keep a meticulous record of their brewing inventory, including ingredients and equipment. It also generates shopping lists based on selected recipes, thereby streamlining the brewing process.

### iSpindel Integration

HoppyBrew seamlessly integrates with iSpindel over Ethernet, allowing users to actively monitor and track the fermentation process.

### User Authentication

The application provides easy account creation and login, ensuring seamless control over recipe-related tasks.

## Technologies

HoppyBrew is built using the following technologies:

- **Frontend**: React, TypeScript, Material-UI
- **Backend**: Node.js, Express, TypeScript
- **Database**: MongoDB
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Deployment**: AWS EC2
- **Monitoring**: Grafana, Prometheus
- **Reverse Proxy**: Nginx
- **Authentication**: JWT
- **Testing**: Jest, Supertest, React Testing Library
- **Documentation**: Markdown, PlantUML
- **Version Control**: Git, GitHub
- **Project Management**: GitHub Projects, ZenHub
- **Communication**: Discord, Zoom, Microsoft Teams
- **IDE**: Visual Studio Code
- **Collaboration**: GitHub, Visual Studio Live Share

## Architecture

HoppyBrew is designed as a self-hosted web application within a Docker container. The application is deployed on an AWS EC2 instance and is monitored using Grafana and Prometheus. The deployment is managed using GitHub Actions, and the application is served using Nginx as a reverse proxy.

## Development Process

The development process for HoppyBrew follows the Agile methodology, with the project being managed using GitHub Projects and ZenHub. The team communicates using Discord, Zoom, and Microsoft Teams, and the codebase is version-controlled using Git and GitHub.

## Documentation

The documentation for HoppyBrew is written in Markdown and PlantUML, and is hosted on GitHub. The team uses Visual Studio Code for development and Visual Studio Live Share for collaboration.

## Conclusion

HoppyBrew is a dedicated web application designed for brewing enthusiasts and homebrewers, offering a bespoke solution for streamlined management of brewing processes. The application empowers users to independently create, share, and manage their beer recipes, eliminating any dependence on subscription-based services. With its self-hosted architecture within a Docker container, HoppyBrew provides users with easy account creation, login, and seamless control over recipe-related tasks. The application also integrates seamlessly with iSpindel over Ethernet, enabling users to actively monitor and track the fermentation process. HoppyBrew further aids users in keeping a meticulous record of their brewing inventory and generates shopping lists based on selected recipes, thereby elevating the overall brewing experience for users.

## References

- [Brewfather](https://brewfather.app/)