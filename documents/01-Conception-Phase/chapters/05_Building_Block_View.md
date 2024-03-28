# Building Block View

## Whitebox Overall System

<div hidden>

```plantuml
@startuml 04-white-box-overall-system

title White Box Overall System

interface " " as I01
interface " " as I02

component "Client Browser" as ClientBrowser
component "ISpindel" as ISpindel

cloud "Internet" {
    component "Cloudflare" as cloudflare
}

ClientBrowser --( I01 : Uses
I01 - cloudflare 

ISpindel --( I02 : Transmits Data
I02 - cloudflare 




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

            api - HoppyBrew : Uses
            HoppyBrew -- db_adapter : Uses
            api -- uvicorn  : Runs
            api -- endpoints  : Uses
            api -- APIRouter  : Uses
        }

        interface " " as I03
        CloudflareTunnel --( I03 : Uses
        I03 -- api


        node "PostgreSQL Container" {
            component "PostgreSQL" as db
        }

        interface " " as I04
        db_adapter --( I04 : Uses
        I04 -- db
    }
}
@enduml
```

</div>

![Overview Diagram](../images/04-white-box-overall-system.svg)

The motivation for the decomposition is to separate the concerns of the different parts of the system. The client browser is responsible for displaying the data to the user, the ISpindel is responsible for collecting the data, and the Unraid Server is responsible for processing the data and storing it in the database. The Cloudflare service is responsible for routing the data between the client browser and the Unraid Server.

Contained Building Blocks 

| Building Block | Responsibilities |
| -------------- | ---------------- |
| Client Browser | Display data to the user |
| ISpindel | Collect data |
| Cloudflare | Route data between the client browser and the Unraid Server |
| App Container | Process data and store it in the database |
| PostgreSQL Container | Store data in the database |

Important Interfaces

{
    TODO: Description of important interfaces
}

## Blackbox Overall System

<div hidden>

```plantuml
@startuml 05-black-box-overall-system
rectangle "Client Browser" {
    component "Client Browser" as client_browser
}

rectangle "ISpindel" {
    component "ISpindel" as iSpindel
}

rectangle "Cloudflare" {
    component "Cloudflare" as cloudflare
}

rectangle "HoppyBrew" {
    component "HoppyBrew" as hoppybrew
}

rectangle "PostgreSQL" {
    component "PostgreSQL" as postgres
}

client_browser -- cloudflare
iSpindel -- cloudflare
cloudflare -- hoppybrew
hoppybrew -- postgres

@enduml
```

</div>

![Overview Diagram](../images/05-black-box-overall-system.svg)

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
