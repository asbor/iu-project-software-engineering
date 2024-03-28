# Building Block View

## Whitebox Overall System

<div hidden>

```plantuml
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

            port "Port:80" as port80
            port "Port:443" as port443
            port "Port:9501" as port9501
            port "Port:5432" as db_port
            

            api - HoppyBrew : Uses
            HoppyBrew -- db_adapter : Uses
            api -- uvicorn  : Runs
            api -- endpoints  : Uses
            api -- APIRouter  : Uses

            
            port80 -down- api : Connects
            db_adapter -- db_port : Connects
        }

        interface " " as I04
        CloudflareTunnel --( I04 : Uses
        I04 -- port80
        I04 -- port443
        I04 -- port9501

        database "PostgreSQL Container" {
            component "PostgreSQL" as PostgreSQL
            port "Port:5432" as PostgreSQL_port
            PostgreSQL -up- PostgreSQL_port : Connects
        }

        interface " " as I05
        db_port --( I05 : Uses
        I05 -- PostgreSQL_port
    }
}
@enduml
```

</div>

![Overview Diagram](../images/04-white-box-overall-system.png)

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

left to right direction

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
