# Project Documentation Outline

# 1. Introduction

## 1.1 Background

HoppyBrew is a web application tailored for brewing enthusiasts and homebrewers, designed for self-hosting. Developed as part of the Software Engineering course at the Faculty of Informatics, International University of Applied Sciences Bad Honnef - Bonn, HoppyBrew addresses the critical need for streamlined management of brewing processes.

Crafted from the personal journey of the creator as a homebrewer venturing into self-hosting, HoppyBrew aims to be a bespoke solution. This web application empowers users to independently create, share, and manage their beer recipes, eliminating any dependence on subscription-based services like Brewfather.

What sets HoppyBrew apart is its self-hosted architecture within a Docker container, providing users with easy account creation, login, and seamless control over recipe-related tasks such as creation, editing, and deletion. The application also boasts a user-friendly search function for recipes based on name, style, or ingredients.

Beyond recipe management, HoppyBrew integrates seamlessly with iSpindel over Ethernet, allowing users to actively monitor and track the fermentation process. It further aids users in keeping a meticulous record of their brewing inventory and generates shopping lists based on selected recipes, thereby elevating the overall brewing experience for users.

# 2. Project Overview

## 2.1 Purpose

The purpose of the project is to develop a web application that caters to the needs of brewing enthusiasts and homebrewers, with a specific focus on self-hosting. HoppyBrew aims to streamline the management of brewing processes, empowering users to create, share, and manage their beer recipes independently. Additionally, the application is designed to be ad-free and subscription-free, ensuring a seamless and uninterrupted user experience.

## 2.2 Goals and Objectives

The overarching goals and objectives for the final project include:

- Develop a comprehensive web application tailored for brewing enthusiasts and homebrewers, emphasizing self-hosting, ad-free, and subscription-free usage.
- Provide users with a user-friendly interface for recipe management, inventory tracking, batch monitoring, and integration with external databases for beer styles.
- Ensure the application's scalability and flexibility to accommodate future enhancements and integrations.
- Establish a robust framework for continuous improvement and iteration based on user feedback and evolving requirements.
- Create a sustainable development process using the Scrum methodology to mitigate risks and deliver incremental value throughout the project lifecycle.
- Lay the foundation for future iterations and expansions beyond the scope of the initial project, allowing for ongoing development and improvement post-completion.

These goals and objectives will serve as the guiding principles for the project, with further breakdowns and refinement occurring during the iterative development process within the Scrum framework.

# 3. Application Selection

## 3.1 Type of Application

The selected application is a web-based solution intended for self-hosting, accessible across various devices such as desktops, tablets, and smartphones. Developed using modern web technologies, it ensures compatibility with popular web browsers and mobile devices. The application will run within a Docker container, ensuring a seamless and secure environment for managing brewing processes.

## 3.2 Criteria Compliance

The application will adhere to the following criteria:

- **Self-hosted:** Users can independently manage their brewing processes.
- **Ad-free:** Ensures a seamless user experience without interruptions from advertisements.
- **Subscription-free:** Eliminates dependency on subscription-based services for access.
- **User-friendly:** Features an intuitive interface for effortless recipe creation, sharing, and management.
- **Scalable and flexible:** Capable of accommodating future enhancements and integrations.
- **Sustainable development:** Developed using the Scrum methodology for a sustainable development process.
- **Continuous improvement:** Lays the groundwork for ongoing development and improvement post-completion.
- **Compatibility:** Ensures accessibility across different platforms and devices.
- **Secure:** Hosted within a Docker container to provide a secure environment.
- **Integration:** Integrates with external databases for comprehensive beer style information.
- **Monitoring:** Enables active monitoring and tracking of the fermentation process with iSpindel over Ethernet.
- **Inventory tracking:** Assists users in managing brewing inventory and generating shopping lists.
- **User feedback:** Incorporates user feedback for continuous improvement and iteration.
- **Future expansions:** Provides a foundation for future iterations and expansions.
- **Modern web technologies:** Developed using contemporary web technologies.
- **Docker container:** Hosted within a Docker container for enhanced security and stability.

# 4. Methodologies and Tools

## 4.1 Methodologies

For the development of the project, the Scrum methodology will be adopted. Scrum is chosen for its iterative and incremental approach, which allows for the gradual improvement and refinement of the application over time. This methodology will guide the development process, ensuring effective collaboration, continuous feedback, and adaptation to evolving requirements.

### Tools and Technologies:
- **Scrum Framework:** Utilized to manage the project's development process, including sprint planning, daily stand-ups, sprint reviews, and retrospectives.
- **Vue.js:** Selected for frontend development, although the developer has limited experience with it. This will be an opportunity to learn and apply new skills.
- **Figma:** Employed for web design, despite the developer's unfamiliarity with it. The learning curve will be navigated to create a visually appealing and user-friendly interface.
- **Python API and Postgres:** Used for backend development, with the developer having some experience that will be further developed throughout the project.
- **Web Scraping:** Required for retrieving data from external sources, an area where the developer lacks experience but is willing to explore and learn.

## 4.2 Risk Mitigation

Mitigating risks is a crucial aspect of project management, especially given the numerous challenges and uncertainties faced. To address potential risks, the following strategies will be implemented:

- **Learning and Skill Development:** Dedicated time will be allocated to learning and mastering new tools and technologies, including Vue.js, Figma, Python API, Postgres, and web scraping.
- **Support Networks:** Leveraging online resources, forums, and communities to seek guidance, support, and advice when encountering challenges during the development process.
- **Time Management:** Implementing effective time management strategies to balance project work with personal responsibilities as a stay-at-home dad.
- **Incremental Development:** Adopting the Scrum methodology to break down the project into manageable tasks and prioritize them based on importance and complexity, allowing for incremental progress and adaptation to changing circumstances.
- **Continuous Learning and Adaptation:** Embracing a growth mindset and remaining open to feedback and constructive criticism, using each setback as an opportunity for learning and improvement.
- **Contingency Planning:** Anticipating potential obstacles and setbacks and developing contingency plans to mitigate their impact on project progress.

By proactively addressing these risks and implementing appropriate mitigation strategies, the project aims to minimize disruptions and maximize the likelihood of successful outcomes.

# 5. Acceptance Criteria

## 5.1 Programming Language and Libraries

### Requirement:

The project permits flexibility in selecting programming languages and libraries to ensure compatibility and efficiency while upholding ethical coding practices.

### Intended Solution:

The front end will be developed using Vue.js for its robust features and ease of use. Python will be utilized for the back end to leverage its versatility and extensive libraries. The database will be implemented in SQL for reliable data storage and retrieval.

## 5.2 Web-based GUI

### Requirement:

The web application must feature a user-friendly and intuitive graphical user interface (GUI) to facilitate seamless navigation and interaction for users of all skill levels.

### Intended Solution:

The GUI design will prioritize clear layout and intuitive controls, enhancing user experience and usability. User feedback will be solicited and incorporated iteratively to refine the GUI design and ensure optimal usability.

## 5.3 Value to Customers

### Requirement:

The application must provide substantial value to its target audience by addressing their core needs and enhancing their brewing experience.

### Intended Solution:

The application will offer essential features such as recipe management, inventory tracking, and batch monitoring to streamline brewing processes. Integration with external databases for beer styles and the ability to import recipes from various sources will further enrich the user experience, delivering tangible value to customers.

## 5.4 Non-functional Requirements

### Requirement:

The application must meet non-functional requirements such as performance, reliability, and security to ensure optimal operation and user satisfaction.

### Intended Solution:

Emphasis will be placed on optimizing application performance, implementing robust security measures, and ensuring reliable operation to meet non-functional requirements. Any identified non-functional requirements that cannot be met initially will be documented as technical debt for future resolution.

## 5.5 Documentation

### Requirement:

Comprehensive project documentation, including profiles, requirements specifications, software design, and system architecture, must be provided to facilitate understanding and maintainability.

### Intended Solution:

Thorough documentation will be prepared at each stage of the project, detailing project objectives, requirements, design decisions, and implementation details. This documentation will serve as a valuable resource for developers, stakeholders, and future maintainers, ensuring transparency and facilitating ongoing development and enhancement of the application.

## 5.6 Version and Release Control

### Requirement:

Version and release control mechanisms must be established to manage changes to the software and its associated documentation effectively.

### Intended Solution:

The project will utilize Git for version control, allowing for the tracking of changes, collaboration among team members, and management of software releases. Regular releases will be planned and executed to deliver new features and updates to users in a timely and organized manner.

## 5.7 GitHub Repository

### Requirement:

The project's source code and files must be hosted on GitHub to enable collaboration, transparency, and version control.

### Intended Solution:

A public GitHub repository will be created to host the project's source code, documentation, and other related files. This repository will serve as a centralized platform for collaboration, allowing developers to contribute code, track changes, and manage project tasks effectively.

## 5.8 Cloud Hosting

### Requirement:

Web applications must be hosted on cloud platforms such as AWS or Google Cloud to ensure accessibility, scalability, and reliability.

### Intended Solution:

The application will be deployed on a cloud hosting platform, providing users with reliable access to the application's frontend via web browsers. Cloud hosting offers scalability, flexibility, and reliability, ensuring optimal performance and availability for users.

## 5.9 Installation and Run Instructions

### Requirement:

Clear and concise instructions for installing and running the application must be provided to users to facilitate ease of setup and operation.

### Intended Solution:

Comprehensive installation and run instructions will be prepared, guiding users through the process of setting up and running the application on their local environment or accessing it via the cloud hosting platform. These instructions will be user-friendly and easy to follow, ensuring a smooth user experience from installation to operation.

# 6. Phases Overview

   6.1 Conception Phase

   - Stress the significance of thorough planning to ensure successful implementation.

   6.2 Design Phase (To be continued in subsequent documentation phases)

   - Provide a brief overview of the upcoming phases.

# 7. Conclusion

   7.1 Summary

   - Summarize key points and expectations for the concept phase.

---

*Note: This outline is written in Markdown (md) format for easy conversion into actual documentation.*