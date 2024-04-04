# Building Block View

## Whitebox Overall System

![Overview Diagram](../images/04-white-box-overall-system.png)

```plantuml
@startuml
component "Client Browser" {
    portout "Port:443" as Client_Port80
}

component "ISpindel" {
    portout "Port:9501" as ISpindel_Port80
}

cloud "Internet" {
    component "Cloudflare" as cloudflare
}

ISpindel_Port80 -- cloudflare
Client_Port80 -- cloudflare

rectangle "Unraid Server" {
    node "Docker Engine" {
        component "Cloudflare" as tunnel{
            portout "Port 443" as CloudFlare_portout443
        }
        cloudflare <|..|> tunnel : <<TUNNEL>>

        node "App Container" as Application_Container {
            component "HoppyBrew" as HoppyBrew
            component "Psycopg\ndb-adapter" as db_adapter
            component "FastAPI" as api
            component "uvicorn" as uvicorn
            component "endpoints" as endpoints
            component "APIRouter" as APIRouter

            portin "Port 443" as HoppyBrew_portin443
            portout "Port 5432" as HoppyBrew_portout5432

            HoppyBrew_portin443 - api : Listens On

            api - HoppyBrew : Uses
            HoppyBrew -- db_adapter : Uses
            api -- uvicorn  : Runs
            api -- endpoints  : Uses
            api -- APIRouter  : Uses
            
            db_adapter - HoppyBrew_portout5432 : Listens On

        }
        CloudFlare_portout443 -- HoppyBrew_portin443  : Connects To

        node "PostgreSQL Container" {
            component "PostgreSQL" as db
            
            portin "Port 5432" as DATABASE_port5432

            DATABASE_port5432 -- db : Listens On
        }

        HoppyBrew_portout5432 -- DATABASE_port5432 : Connects To
        
    }
}
@enduml
```

The motivation for the decomposition is to separate the concerns of the different parts of the system. The client browser is responsible for displaying the data to the user, the ISpindel is responsible for collecting the data, and the Unraid Server is responsible for processing the data and storing it in the database. The Cloudflare service is responsible for routing the data between the client browser and the Unraid Server.




Contained Building Blocks  
*\<Description of contained building block (black boxes)\>*

| Building Block | Responsibilities |
| -------------- | ---------------- |
| Client Browser | Display data to the user |
| ISpindel | Collect data |
| Cloudflare | Route data between the client browser and the Unraid Server |
| App Container | Process data and store it in the database |
| PostgreSQL Container | Store data in the database |

Important Interfaces  
*\<Description of important interfaces\>*


## Blackbox Overall System

![Overview Diagram](../images/05-black-box-overall-system.png)

```plantuml
@startuml
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
