# Building Block View

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
        component "Cloudflare" as CloudflareTunnel

        cloudflare <|..|> CloudflareTunnel : <<TUNNEL>>

        node "App Container" as Application_Container {
            component "HoppyBrew" as HoppyBrew
            component "Psycopg\ndb-adapter" as db_adapter
            component "FastAPI" as api
            component "uvicorn" as uvicorn
            component "endpoints" as endpoints
            component "APIRouter" as APIRouter
            component "EntityManager" as EntityManager
            component "PictureGallery" as PictureGallery

            portin "Port:80" as port80
            portin "Port:443" as port443
            portin "Port:9501" as port9501
            portout "Port:5432" as port5432
            

            api - HoppyBrew : Uses
            HoppyBrew -- db_adapter : Uses
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

        database "PostgreSQL Container" {
            component "PostgreSQL" as PostgreSQL
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

![Overview Diagram](../images/04-white-box-overall-system.png)

The motivation for the decomposition is to separate the concerns of the different parts of the system. The client browser is responsible for displaying the data to the user, the ISpindel is responsible for collecting the data, and the Unraid Server is responsible for processing the data and storing it in the database. The Cloudflare service is responsible for routing the data between the client browser and the Unraid Server.

Contained Building Blocks:

**Client Browser:** The client browser is responsible for displaying the data to the user. It communicates with the Cloudflare service to send and receive data.

**ISpindel:** The ISpindel is responsible for collecting the data. It communicates with the Cloudflare service to send and receive data.

**Cloudflare:** The Cloudflare service is responsible for routing the data between the client browser and the Unraid Server.

**Unraid Server:** The Unraid Server is responsible for processing the data and storing it in the database. It communicates with the Cloudflare service to send and receive data.

**Docker Engine:** The Docker Engine is responsible for managing the containers of the Unraid Server. It communicates with the Cloudflare service to send and receive data.

**App Container:** The App Container is responsible for running the HoppyBrew application. It communicates with the Cloudflare service to send and receive data. It also communicates with the PostgreSQL database to store the data.

**PostgreSQL Container:** The PostgreSQL Container is responsible for running the PostgreSQL database. It communicates with the HoppyBrew application to receive data.

**FastAPI:** The FastAPI is responsible for providing the API endpoints for the HoppyBrew application. It communicates with the HoppyBrew application to process the data.

**Psycopg db-adapter:** The Psycopg db-adapter is responsible for connecting the HoppyBrew application to the PostgreSQL database. It communicates with the HoppyBrew application to store the data.

**uvicorn:** The uvicorn is responsible for running the FastAPI application. It communicates with the FastAPI application to process the data.

**endpoints:** The endpoints are responsible for providing the API endpoints for the FastAPI application. They communicate with the FastAPI application to process the data.

**APIRouter:** The APIRouter is responsible for routing the API requests to the appropriate endpoints. It communicates with the FastAPI application to process the data.

**EntityManager:** The EntityManager is responsible for managing the entities of the HoppyBrew application. It communicates with the HoppyBrew application to process the data.

**PictureGallery:** The PictureGallery is responsible for managing the pictures of the HoppyBrew application. It communicates with the HoppyBrew application to process the data.


| Building Block | Responsibilities |
| -------------- | ---------------- |
| **Client Browser** | The client browser is responsible for displaying the data to the user. It communicates with the Cloudflare service to send and receive data. |
| **ISpindel** | The ISpindel is responsible for collecting the data. It communicates with the Cloudflare service to send and receive data. |
| **Cloudflare** | The Cloudflare service is responsible for routing the data between the client browser and the Unraid Server. |
| **HoppyBrew** | The HoppyBrew application is responsible for processing the data and storing it in the database. It communicates with the Cloudflare service to send and receive data. It also communicates with the PostgreSQL database to store the data. |
| **PostgreSQL** | The PostgreSQL database is responsible for storing the data. It communicates with the HoppyBrew application to receive data. |
| **Cloudflare Tunnel** | The Cloudflare Tunnel is responsible for routing the data between the Cloudflare service and the Unraid Server. |
| **Docker Engine** | The Docker Engine is responsible for managing the containers of the Unraid Server. It communicates with the Cloudflare service to send and receive data. |
| **App Container** | The App Container is responsible for running the HoppyBrew application. It communicates with the Cloudflare service to send and receive data. It also communicates with the PostgreSQL database to store the data. |
| **PostgreSQL Container** | The PostgreSQL Container is responsible for running the PostgreSQL database. It communicates with the HoppyBrew application to receive data. |
| **FastAPI** | The FastAPI is responsible for providing the API endpoints for the HoppyBrew application. It communicates with the HoppyBrew application to process the data. |
| **Psycopg db-adapter** | The Psycopg db-adapter is responsible for connecting the HoppyBrew application to the PostgreSQL database. It communicates with the HoppyBrew application to store the data. |
| **uvicorn** | The uvicorn is responsible for running the FastAPI application. It communicates with the FastAPI application to process the data. |
| **endpoints** | The endpoints are responsible for providing the API endpoints for the FastAPI application. They communicate with the FastAPI application to process the data. |
| **APIRouter** | The APIRouter is responsible for routing the API requests to the appropriate endpoints. It communicates with the FastAPI application to process the data. |
| **EntityManager** | The EntityManager is responsible for managing the entities of the HoppyBrew application. It communicates with the HoppyBrew application to process the data. |
| **PictureGallery** | The PictureGallery is responsible for managing the pictures of the HoppyBrew application. It communicates with the HoppyBrew application to process the data. |



Important Interfaces

{
    TODO: Description of important interfaces
}

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

        rectangle "Cloudflare\nDocker Container" {
            component "Cloudflare Tunnel" as cloudflareTunnel
        }

        rectangle "Application\nDocker Container" {
            component "HoppyBrew" as hoppybrew
        }

        rectangle "Database\nDocker Container" {
            component "PostgreSQL" as postgres
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

![Overview Diagram](../images/05-black-box-overall-system.png)

### \<Name black box 1\>

### Client Browser

The client browser is responsible for displaying the data to the user. It communicates with the Cloudflare service to send and receive data.

### ISpindel

The ISpindel is responsible for collecting the data. It communicates with the Cloudflare service to send and receive data.

### Cloudflare

The Cloudflare service is responsible for routing the data between the client browser and the Unraid Server.

### HoppyBrew

The HoppyBrew application is responsible for processing the data and storing it in the database. It communicates with the Cloudflare service to send and receive data. It also communicates with the PostgreSQL database to store the data. This can also be seen as the business logic of the application.

### PostgreSQL

The PostgreSQL database is responsible for storing the data. It communicates with the HoppyBrew application to receive data.

\clearpage
