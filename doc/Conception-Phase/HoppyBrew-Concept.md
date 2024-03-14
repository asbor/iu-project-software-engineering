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
# 5. Acceptance Criteria

## 5.1 Programming Language and Libraries

### Requirement:
- The project allows freedom in selecting programming languages and libraries.

### Intended Solution:
- Developers can choose appropriate tools for implementation, ensuring compatibility and efficiency while maintaining ethical coding practices.

## 5.2 Web-based GUI

### Requirement:
- The web application must feature a self-explanatory and intuitive graphical user interface (GUI).

### Intended Solution:
- The GUI design prioritizes user-friendly navigation and interaction, fostering ease of use and understanding for users of all skill levels.

## 5.3 Value to Customers

### Requirement:
- The application must provide significant value to the target audience, addressing their fundamental needs and enhancing their brewing experience.

### Intended Solution:
- By delivering essential features and innovative solutions, the application aims to become an indispensable tool for brewing enthusiasts and homebrewers, improving their efficiency and enjoyment of the brewing process.

## 5.4 Non-functional Requirements

### Requirement:
- The application must meet non-functional requirements to ensure optimal performance, reliability, and usability.

### Intended Solution:
- Any identified non-functional requirements that cannot be met within the project scope will be documented as technical debt, with plans for future resolution or mitigation.

## 5.5 Documentation

### Requirement:
- Comprehensive project documentation must be provided, including profiles, requirements specifications, software design, and system architecture documentation.

### Intended Solution:
- The project documentation will offer insights into the development process and facilitate future enhancements or modifications, ensuring transparency and maintainability.

## 5.6 Version and Release Control

### Requirement:
- Version and release control mechanisms must be established to manage changes to the software and its associated documentation.

### Intended Solution:
- By implementing robust version control practices, including the use of Git and GitHub, the project will track changes, manage collaboration, and ensure the integrity and availability of all project assets.

## 5.7 GitHub Repository

### Requirement:
- The project's source code and files must be hosted on GitHub as part of building a comprehensive project portfolio.

### Intended Solution:
- Maintaining a public repository on GitHub will showcase coding skills, project management abilities, and commitment to open collaboration and continuous improvement within the software development community.

## 5.8 Cloud Hosting

### Requirement:
- Web applications must be hosted on cloud platforms such as AWS, Google Cloud, or similar services for accessibility and scalability.

### Intended Solution:
- Cloud hosting provides users with direct access to the application's frontend via web browsers, enabling seamless interaction and collaboration across different devices and locations.

## 5.9 Installation and Run Instructions

### Requirement:
- Clear and concise instructions for installing and running the application must be provided to users.

### Intended Solution:
- By facilitating easy installation and deployment, the application maximizes its accessibility and usability for users, ensuring a smooth user experience from setup to operation.

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