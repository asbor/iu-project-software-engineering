# Building Block View

## Blackbox Overall System

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 05-black-box-overall-system

left to right direction

rectangle "Client" {
    component "Client Browser" as client_browser
}

rectangle "Devices" {
    component "ISpindel" as iSpindel
}

cloud "Cloudflare" {
    component "Cloudflare" as cloudflare
}
rectangle "Unraid Server" {
    rectangle "Docker Engine" {

        node "Cloudflare\nDocker Container" {
            component "Cloudflare Tunnel" as cloudflareTunnel
        }

        node "Application\nDocker Container" {
            component "HoppyBrew" as hoppybrew
        }

        node "Database\nDocker Container" {
            database "PostgreSQL" as postgres
        }
    }
}


client_browser -- cloudflare
iSpindel -- cloudflare
cloudflare -- cloudflareTunnel
cloudflareTunnel -- hoppybrew
hoppybrew -- postgres

@enduml
    </code>
</pre>

![Overview Diagram](file:///home/asbjorn/repo/iu-project-software-engineering/documents/docs/images/05-black-box-overall-system.png)

### Client Browser

The client browser is responsible for displaying the data to the user. It communicates with the Cloudflare service to send and receive data.

### Cloudflare

The Cloudflare service is responsible for routing the data between the client browser and the Unraid Server.

### ISpindel

The ISpindel is responsible for collecting the data. It communicates with the Cloudflare service to send and receive data.

### HoppyBrew

The HoppyBrew application is responsible for processing the data and storing it in the database. It communicates with the Cloudflare service to send and receive data. It also communicates with the PostgreSQL database to store the data. This can also be seen as the business logic of the application.

### PostgreSQL

The PostgreSQL database is responsible for storing the data. It communicates with the HoppyBrew application to receive data.

## Whitebox Overall System

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 04-white-box-overall-system

title White Box Overall System

interface " " as I01
interface " " as I02
interface " " as I03

component "Client Browser" as ClientBrowser{
    portout "Port:80" as ClientPort80
    portout "Port:443" as ClientPort443
}
component "ISpindel" as ISpindel{
    portout "Port:9501" as ISpindel_port
}

cloud "Internet" {
    component "Cloudflare" as cloudflare
}

ClientPort80 -down-( I01 : Uses
I01 -down- cloudflare 

ClientPort443 -down-( I02 : Uses
I02 -down- cloudflare

ISpindel_port --( I03 : Transmits Data
I03 - cloudflare 


rectangle "Unraid Server" {
    node "Docker Engine" {
        node "Cloudflare\nDocker Container" {
            component "Cloudflare Tunnel" as CloudflareTunnel
        }

        cloudflare <|..|> CloudflareTunnel : <<TUNNEL>>

        node "App Container" as Application_Container {
            component "HoppyBrew" as HoppyBrew
            component "Psycopg\ndb-adapter" as db_adapter
            component "FastAPI" as api
            component "uvicorn" as uvicorn
            component "endpoints" as endpoints
            component "APIRouter" as APIRouter
            component "PictureGallery" as PictureGallery
            component "SQLAlchemy" as SQLAlchemy

            portin "Port:80" as port80
            portin "Port:443" as port443
            portin "Port:9501" as port9501
            portout "Port:5432" as port5432

            api - HoppyBrew : Uses
            HoppyBrew -- SQLAlchemy : Uses
            SQLAlchemy - db_adapter : Uses
            api -- uvicorn  : Runs
            api -- endpoints  : Uses
            api -- APIRouter  : Uses

            port80 -down- api : Connects
            db_adapter -down- port5432 : Connects
        }

        interface " " as I04
        CloudflareTunnel --( I04 : Uses
        I04 -- port80
        I04 -- port443
        I04 -- port9501

        node "PostgreSQL Container" {
            database "PostgreSQL" as PostgreSQL
            portin "Port:5432" as PostgreSQL_port5432
            PostgreSQL_port5432 - PostgreSQL : Connects
        }

        interface " " as I05
        port5432 -down-( I05 : Uses
        I05 -down- PostgreSQL_port5432
    }
}
@enduml
    </code>
</pre>

![Overview Diagram](file:///home/asbjorn/repo/iu-project-software-engineering/documents/docs/images/04-white-box-overall-system.png)

The motivation for the decomposition is to separate the concerns of the different parts of the system. The client browser is responsible for displaying the data to the user, the ISpindel is responsible for collecting the data, and the Unraid Server is responsible for processing the data and storing it in the database. The Cloudflare service is responsible for routing the data between the client browser and the Unraid Server.

Contained Building Blocks:

### PictureGallery (Blackbox)

**Intent/Responsibility:**

The PictureGallery component is responsible for managing the pictures in the application. 


**Interfaces:**

| **Interface** | **Description** |
| -- | ---- |
| REST interface | /api/PictureGallery/* |

Table: PictureGallery interfaces.

### FastAPI (Blackbox)

**Intent/Responsibility:**

The FastAPI component is responsible for providing the web framework for the application. It provides a set of APIs for the different parts of the application, such as users, recipes, batches, profiles, devices, inventory, and system settings. It communicates with the SQLAlchemy component to store and retrieve data.

### APIRouter (Blackbox)

**Intent/Responsibility:**

The APIRouter component is responsible for routing the requests to the different parts of the application. It provides a set of routes for the different parts of the application, such as users, recipes, batches, profiles, devices, inventory, and system settings. It communicates with the FastAPI component to handle the requests and responses.

### Endpoints (Blackbox)

**Intent/Responsibility:**

The Endpoints component is responsible for defining the endpoints for the different parts of the application. It provides a set of endpoints for the different parts of the application, such as users, recipes, batches, profiles, devices, inventory, and system settings. It communicates with the FastAPI component to handle the requests and responses.

### SQLAlchemy (Blackbox)

**Intent/Responsibility:**

The SQLAlchemy component is responsible for providing the Object Relational Mapper (ORM) for the application. It provides a high-level interface for interacting with the PostgreSQL database, including support for complex queries, transactions, and data integrity constraints. It communicates with the FastAPI component to store and retrieve data.

### Psycopg db-adapter (Blackbox)

**Intent/Responsibility:**

The Psycopg db-adapter component is responsible for providing the database adapter for the application. It provides a low-level interface for interacting with the PostgreSQL database, including support for connecting, querying, and updating data. It communicates with the SQLAlchemy component to store and retrieve data.

### uvicorn (Blackbox)

**Intent/Responsibility:**

The uvicorn component is responsible for providing the ASGI server for the application. It provides a high-performance server for handling the requests and responses of the application. It communicates with the FastAPI component to run the application.

### HoppyBrew (Blackbox)

**Intent/Responsibility:**

The HoppyBrew component is responsible for providing the business logic of the application. It provides a set of APIs for the different parts of the application, such as users, recipes, batches, profiles, devices, inventory, and system settings. It communicates with the SQLAlchemy component to store and retrieve data.

### Cloudflare (Blackbox)

**Intent/Responsibility:**

The Cloudflare component is responsible for providing the routing service for the application. It provides a secure and reliable connection between the client browser and the Unraid Server. It communicates with the Cloudflare Tunnel component to route the data between the client browser and the Unraid Server.

### Cloudflare Tunnel (Blackbox)

**Intent/Responsibility:**

The Cloudflare Tunnel component is responsible for providing the tunnel for the application. It provides a secure and reliable connection between the client browser and the Unraid Server. It communicates with the Cloudflare service to route the data between the client browser and the Unraid Server.

### PostgreSQL (Blackbox)

**Intent/Responsibility:**

The PostgreSQL component is responsible for providing the database technology for the application. It provides a powerful and reliable relational database management system for storing and managing the data of the application. It communicates with the HoppyBrew component to store and retrieve data.

### Client Browser (Blackbox)

**Intent/Responsibility:**

The Client Browser component is responsible for providing the user interface for the application. It provides a set of interfaces for the different parts of the application, such as users, recipes, batches, profiles, devices, inventory, and system settings. It communicates with the Cloudflare service to send and receive data.

### ISpindel (Blackbox)

**Intent/Responsibility:**

The ISpindel component is responsible for providing the data collection service for the application. It provides a set of interfaces for collecting the data from the brewing process. It communicates with the Cloudflare service to send and receive data.

\clearpage
