# System Scope and Context

## Business Context

As indicated in the business context diagram below, the system only interacts with three external actors, namely the Administrator, The Brewer, and the ISpindel. The Administrator is responsible for managing the system, including adding new users, managing user roles, and monitoring the system. The Brewer is responsible for creating new brews, managing existing brews, and monitoring the progress of the brews. The ISpindel is responsible for collecting real-time data from the brewing process and sending it to the system.

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 02-Context-Vew-Business

left to right direction

cloud iSpindle
actor Brewer
database "Online Recipe\nDatabase" as RecipeDB

node "HoppyBrew" as HoppyBrew
database "PostgreSQL" as PostgreSQL

RecipeDB --> HoppyBrew : CRUD Recipes
iSpindle --> HoppyBrew : Transmit Live\nData
Brewer --> HoppyBrew : CRUD Recipes\nand Brews
HoppyBrew <..> PostgreSQL : <<flows>>
HoppyBrew --> Brewer : Instructions\nand Notifications
@enduml
    </code>
</pre>

![High-level business context diagram for the application.](file:///home/asbjorn/repo/iu-project-software-engineering/documents/docs/images/02-Context-Vew-Business.png)

**Brewer:** The Brewer is responsible for creating new brews, managing existing brews, and monitoring the progress of the brews. The Brewer interacts with the system to create new recipes, manage existing recipes, and monitor the progress of the brews.

**Administrator:** The Administrator is responsible for managing the system, including adding new users, managing user roles, and monitoring the system. The Administrator interacts with the system to add new users, manage user roles, and monitor the system.

**iSpindel:** The iSpindel is responsible for collecting real-time data from the brewing process and sending it to the system. The iSpindel interacts with the system to transmit live data from the brewing process.

**Online Recipe Database:** The Online Recipe Database is responsible for storing and managing recipes for the system. The Online Recipe Database interacts with the system to store and retrieve recipes.

**HoppyBrew:** HoppyBrew is the system that is being developed. It is responsible for managing brewing recipes and brew logs. HoppyBrew interacts with the Brewer, Administrator, iSpindel, and Online Recipe Database to provide the functionality of the system.

**PostgreSQL:** PostgreSQL is the database technology that is being used to store and manage data for the system. PostgreSQL interacts with HoppyBrew to store and retrieve data.

## Use Case Diagram

The following use cases have been identified for the application:

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 01-Use-Case-Diagram

left to right direction

actor Administrator as Admin
actor Brewer as Brewer
actor Database as DB
actor ISpindel as ISpindel
actor "{abstract}" as AbstractUser

Admin --|> AbstractUser
Brewer --|> AbstractUser

rectangle "HoppyBrew" as HoppyBrew {
    usecase "Manage  Users" as ManageUsers
    usecase "Manage Recipes" as ManageRecipes
    usecase "Define water profile" as DefineWaterProfile
    usecase "Create Batch" as CreateBatch
    usecase "Manage Batches" as ManageBatches
    usecase "{abstract}\nManage Profiles" as ManageProfiles
    usecase "Manage Devices" as ManageDevices
    usecase "Manage Inventory" as ManageInventory
    usecase "Manage System Settings" as ManageSystemSettings
    usecase "Collect\nRealtime Data" as CollectRealtimeData

    Admin --> ManageUsers
    AbstractUser --> ManageRecipes
    AbstractUser --> ManageBatches
    AbstractUser --> ManageProfiles
    AbstractUser --> ManageDevices
    AbstractUser --> ManageInventory
    AbstractUser --> ManageSystemSettings

    CreateBatch .> ManageBatches : <<extends>>

    ManageRecipes .> CreateBatch : <<extends>>
    CreateBatch --> DB

}

    ManageInventory --> DB
    ManageRecipes --> DB
    ManageProfiles --> DB
    
    ManageDevices <-- ISpindel
    CollectRealtimeData <-- ISpindel
    
@enduml
  </code>
</pre>

![High-level use case diagram for the application.](file:///home/asbjorn/repo/iu-project-software-engineering/documents/docs/images/01-Use-Case-Diagram.png)

#### Actors

The following actors are involved in the use cases:

| **Actor** | **Description** |
| -- | ---- |
| **Admin** | The admin is responsible for managing the application and its users. |
| **Brewer** | The brewer is responsible for managing and creating brewing recipes and brews. |
| **ISpindel** | The iSpindel is responsible for providing data to the application. |
| **Database** | The database is responsible for storing and managing data for the application. |

Table: Actors involved in the use cases for the application.

#### Use Cases

The following use cases are supported by the application:

| **Id** | **Use Case** | **Description** |
| - | -- | ---- |
| **UC1** | **Manage Users** | The admin can manage users, including creating, updating, and deleting users. |
| **UC2** | **Manage Recipes** | The brewer can manage recipes, including creating, updating, and deleting recipes. |
| **UC3** | **Create Batch** | The brewer can create a batch based on a recipe. |
| **UC4** | **Manage Batches** | The brewer can manage batches, including creating, updating, and deleting batches. |
| **UC5** | **Manage Profiles** | The brewer can manage profiles, including creating, updating, and deleting profiles. |
| **UC6** | **Manage Devices** | The admin can manage devices, including creating, updating, and deleting devices. |
| **UC7** | **Manage Inventory** | The admin can manage inventory, including creating, updating, and deleting inventory items. |
| **UC8** | **Manage System Settings** | The admin can manage system settings, including updating system settings. |
| **UC9** | **Collect Realtime Data** | The iSpindel can collect realtime data and send it to the application. |

Table: High-level use cases for the application.

## Technical Context

From a technical perspective, the system interacts with several external systems and services. The system is dependent on the iSpindel for collecting real-time data from the brewing process. The system is also dependent on a database for storing and managing data. The system uses GitHub for version control and collaboration. Finally, the system uses Docker for containerization and deployment.

TODO: Create a new diagram for the technical context view.

The technical context diagram provides a high-level overview of the technical environment in which the system operates. The diagram shows the system and its interactions with external systems and services. The diagram also shows the dependencies of the system on external systems and services.

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 03-Context-View-Technical

title Technical Context Diagram

actor user as "Operator"
entity ISpindel as "iSpindel"
boundary WebServer as "Web Server"
control AppServer as "Application Server"
database Database as "SQLDatabase"

ISpindel -> AppServer : HTTP Request
AppServer -> ISpindel : HTTP Response

user -> WebServer : HTTP Request
WebServer -> AppServer : HTTP Request
AppServer -> Database : SQL Query
Database -> AppServer : SQL Response
AppServer -> WebServer : HTTP Response
WebServer -> user : HTTP Response

@enduml
    </code>
</pre>

![Technical-Context-Vew](file:///home/asbjorn/repo/iu-project-software-engineering/documents/docs/images/03-Context-View-Technical.png)

**Backend:** The backend of the application is responsible for processing the data and storing it in the database. The backend communicates with the frontend using RESTful APIs. The backend is developed using Python and FastAPI, with PostgreSQL as the database technology.

**Frontend:** The frontend of the application is responsible for displaying the data to the user. The frontend communicates with the backend using RESTful APIs.

**Database:** The database of the application is responsible for storing and managing the data. The database communicates with the backend using SQL queries.

\clearpage
