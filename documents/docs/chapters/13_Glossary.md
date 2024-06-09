# Glossary

This glossary contains the most important domain and technical terms that stakeholders use when discussing the system. Clearly defining terms ensures all stakeholders have an identical understanding of these terms and do not use synonyms or homonyms. The glossary includes terms with their definitions and potentially translations if needed.

## Computer Science Terminologies

| **Term**                    | **Definition**                                                                                                                                       |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**                   | In use case parlance, parties outside the system that interact with the system. They may be users or other systems.                                    |
| **Architecture**            | The high-level structure of software systems, identifying a set of components that collaborate to achieve system goals.                               |
| **Conceptual Architecture** | Directs attention to an appropriate decomposition of the system without delving into interface specification and type information.                     |
| **Features**                | The differentiating functionality of a product, which may not be available in other products or with the same quality characteristics.                |
| **Functional Requirements** | Capture the intended behavior of the system or what the system will do, expressed as services, tasks, or functions.                                   |
| **Logical Architecture**    | Detailed architecture specification, precisely defining component interfaces and connection mechanisms and protocols.                                 |
| **Meta-architecture**       | High-level decisions influencing the structure of the system, through style, patterns, principles, and philosophy, guiding structural choices.        |
| **Non-functional Requirements** | Capture required properties of the system, such as performance, security, maintainability, etc.                                                   |
| **Product Line**            | Consists of basically similar products with different cost/feature variations per product.                                                           |
| **Product Family**          | Includes a number of product lines targeted at different markets or usage situations, with common elements of functionality and identity.             |
| **Qualities**               | System qualities or non-functional requirements, capturing properties of the system like performance, security, maintainability, etc.                 |
| **Scenario**                | An instance of a use case, representing a single path through the use case, describing interactions between actors and the system.                    |
| **Use Case**                | Defines a goal-oriented set of interactions between external actors and the system under consideration, detailing the steps to achieve a goal.        |
| **Use Case Diagram**        | A graphical representation of use cases and their relationships to the actors.                                                                        |
| **User Interface**          | The part of the system with which users interact, including screens, forms, reports, and so on.                                                      |
| **User Story**              | A short, simple description of a feature told from the perspective of the person who desires the new capability, usually a user or customer.         |
| **View**                    | A representation of a whole system from the perspective of a related set of concerns, used to describe the system from different stakeholders' viewpoints. |
| **Viewpoint**               | A specification of the conventions for constructing and using a view, defining the kinds of models to be constructed and the rules governing them.    |
| **Viewtype**                | A template for a view, specifying the types of models to be constructed and the rules governing their construction.                                    |
| **Work Product**            | A document or model produced as part of a software development process, used to capture and communicate information about the system being developed. |
| **Entity-Relationship Diagram (ERD)** | A visual representation of the relationships between entities in a database, showing how data is organized and related.                   |
| **Object Relational Mapper (ORM)** | A programming technique that maps objects from an object-oriented programming language to a relational database.                                  |
| **CRUD**                    | Acronym for Create, Read, Update, Delete – basic operations for managing data.                                                                        |
| **Quality Attribute**       | A property or characteristic of the system that affects its overall performance and user experience, such as usability, reliability, or scalability.  |

Table: Computer Science Glossary.

## Brewing Specific Terminologies

| **Term**               | **Definition**                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------|
| **Brew Log**           | A record of the brewing process, including details such as ingredients, timings, and observations.      |
| **iSpindel**           | A digital hydrometer used in brewing to monitor the fermentation process by measuring tilt and temperature. |
| **Recipe**             | A set of instructions for brewing beer, including ingredients and steps.                                |
| **Stakeholder**        | An individual or group with an interest or concern in the project, such as users, developers, or project managers. |
| **IBU**                | International Bitterness Units, a measure of the bitterness of beer, determined by the amount of hops used in brewing. |
| **ABV**                | Alcohol by Volume, a measure of the alcohol content of beer, expressed as a percentage of the total volume. |
| **OG**                 | Original Gravity, a measure of the sugar content of beer before fermentation, used to calculate the alcohol content. |
| **FG**                 | Final Gravity, a measure of the sugar content of beer after fermentation, used to calculate the alcohol content. |
| **EBC**                | European Brewery Convention, a measure of the color of beer, expressed in units of color.               |
| **BU/GU**              | Bitterness Units to Gravity Units ratio, a measure of the balance between bitterness and sweetness in beer. |
| **Sparging**           | The process of rinsing the grains with hot water to extract sugars for fermentation.                    |
| **Mashing**            | The process of soaking malted grains in hot water to extract sugars for fermentation.                   |
| **Boiling**            | The process of heating the wort to a boil, adding hops and other ingredients, and sterilizing the liquid.|
| **Fermentation**       | The process of adding yeast to the wort to convert sugars into alcohol and carbon dioxide.              |
| **Conditioning**       | The process of aging beer after fermentation to develop flavors and carbonation.                        |
| **RO Water**           | Reverse Osmosis water, a type of purified water used in brewing to remove impurities and minerals.       |
| **Yeast Starter**      | A small batch of wort used to grow yeast cells before pitching them into the main batch of beer.        |
| **Cold Crash**         | The process of cooling beer to near-freezing temperatures to clarify the liquid before bottling or kegging. |
| **Kegging**            | The process of transferring beer from a fermenter to a keg for carbonation and serving.                 |
| **Bottling**           | The process of transferring beer from a fermenter to bottles for carbonation and storage.               |
| **Carbonation**        | The process of adding carbon dioxide to beer to create bubbles and effervescence.                       |
| **Lautering**          | The process of separating the liquid wort from the solid grains after mashing.                          |
| **Sparge Water**       | The hot water used to rinse the grains during the sparging process.                                     |
| **Mash Tun**           | The vessel used for mashing and lautering the grains in the brewing process.                            |
| **Fermenter**          | The vessel used for fermenting the wort after boiling and cooling.                                      |
| **Airlock**            | A device used to allow carbon dioxide to escape from the fermenter while preventing oxygen from entering. |
| **Hydrometer**         | A device used to measure the specific gravity of beer, indicating the sugar content and fermentation progress. |
| **Thermometer**        | A device used to measure the temperature of the wort during brewing and fermentation.                   |
| **pH Meter**           | A device used to measure the acidity of the wort and beer during brewing and fermentation.              |
| **Hop Spider**         | A device used to contain hops during the boiling process, preventing them from clogging the equipment.  |
| **Immersion Chiller**  | A device used to cool the wort quickly after boiling, reducing the risk of contamination.               |

Table: Brewing Glossary.

\clearpage

## Conclusion

In conclusion, the development of HoppyBrew has been a challenging yet rewarding journey. Despite not implementing the iSpindel integration due to its complexity and the testing constraints, the project achieved several key milestones and functional implementations.

### Achievements

1. **Database and Models:** Successfully created the database, including the models and CMS, which start up correctly. This setup involved ensuring smooth communication between the three Docker containers for the backend, database, and frontend.
2. **CRUD Operations:** Implemented and tested CRUD operations for hops, fermentables, miscellaneous items, yeast, recipes, and batches.
3. **Web Scraping:** Conducted web scraping to pull down various recipes, including those from the Brewer Association, and successfully stored this data in the database.
4. **Import and Export of XML Files:** Implemented functionalities to import and export BeerXML files, allowing seamless data exchange with applications like Brewfather.
5. **Continuous Integration and Deployment (CI/CD):** Set up CI/CD pipelines using GitHub Actions, successfully building and testing Docker containers, and ensuring interconnectedness between containers. This setup also included linting for code quality and partial implementation of deployment processes to Docker Hub.
6. **Documentation:** Developed comprehensive documentation using Markdown, converted to PDF using Pandoc. Despite the technical challenges, this documentation ensures clarity and ease of understanding for future developers.
7. **Makefile:** Worked with makefiles to streamline and automate the build process, which proved to be a powerful tool for managing project build tasks efficiently.

### Challenges

1. **Dependency and Version Control:** Faced significant issues with managing dependencies and version control due to discrepancies between different tutorials and updates, leading to frequent application breaks and fixes.
2. **Database Migration:** Encountered extensive challenges with database relationships and migrations, which would have benefited from earlier use of database versioning tools.
3. **Front-end Development:** Although new to Vue.js and Nuxt.js, managed to develop the frontend, despite occasional breaks and the need to frequently rebuild the virtual environment.
4. **Complex Implementations:** Left out complex features such as equipment profiles, water profiles, and mash profiles due to time constraints and their similarity to recipe CRUD operations.
5. **Docker and Docker Compose:** Spent considerable time working with Docker and Docker Compose, realizing their differences. Docker Compose, while useful for local development, was not recommended for the Unraid system, leading to additional complexity in deployment strategies.

### Learnings

1. **Scrum Methodology:** Gained a deep appreciation for Scrum, finding its dynamic and agile approach highly effective.
2. **Tools and Technologies:** Learned to use Atlassian Jira for project management, Docker for containerization, FastAPI for backend development, and Vue.js/Nuxt.js for frontend development.
3. **Documentation Practices:** Invested time in building thorough documentation, learning the intricacies of Markdown and conversion tools like Pandoc.
4. **GitHub vs. GitLab:** Initially explored using GitLab for its strong CI/CD capabilities but realized late in the project that the assignment required using GitHub. Upon reflection, found GitHub to be stronger and easier to work with, facilitating smoother project management and CI/CD implementation.
5. **Makefile:** Utilized makefiles to automate build tasks, enhancing the efficiency and manageability of the project’s build process.

Overall, the HoppyBrew project provided a comprehensive learning experience, equipping me with valuable skills and knowledge in modern web application development and project management methodologies. Despite some unfinished features and the decision to deprioritize certain functionalities, the project stands as a robust proof of concept, ready for further development and refinement.

\clearpage
