# Runtime View

User interactions with the system are depicted in the following sequence diagrams.

## User Login

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 06-User-Login

actor User as User
participant "Client Browser" as ClientBrowser
participant "Cloudflare" as Cloudflare
participant "Cloudflare Tunnel" as CloudflareTunnel
participant "HoppyBrew" as HoppyBrew
participant "PostgreSQL" as PostgreSQL

User -> ClientBrowser : Enters URL
ClientBrowser -> Cloudflare : Sends Request
Cloudflare -> CloudflareTunnel : Routes Request
CloudflareTunnel -> HoppyBrew : Routes Request
HoppyBrew -> PostgreSQL : Queries Database
PostgreSQL --> HoppyBrew : Returns Data
HoppyBrew --> CloudflareTunnel : Returns Data
CloudflareTunnel --> Cloudflare : Returns Data
Cloudflare --> ClientBrowser : Returns Data
ClientBrowser --> User : Displays Data

@enduml
    </code>
</pre>

![User Login](../images/06-User-Login.png)

## User Logout

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 07-User-Logout

actor User as User
participant "Client Browser" as ClientBrowser
participant "Cloudflare" as Cloudflare
participant "Cloudflare Tunnel" as CloudflareTunnel
participant "HoppyBrew" as HoppyBrew
participant "PostgreSQL" as PostgreSQL

User -> ClientBrowser : Clicks Logout
ClientBrowser -> Cloudflare : Sends Request
Cloudflare -> CloudflareTunnel : Routes Request
CloudflareTunnel -> HoppyBrew : Routes Request
HoppyBrew -> PostgreSQL : Queries Database
PostgreSQL --> HoppyBrew : Returns Data
HoppyBrew --> CloudflareTunnel : Returns Data
CloudflareTunnel --> Cloudflare : Returns Data
Cloudflare --> ClientBrowser : Returns Data
ClientBrowser --> User : Displays Data

@enduml
    </code>
</pre>

![User Logout](../images/07-User-Logout.png)

## Create Recipe

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 08-Create-Recipe

actor Brewer as Brewer
participant "Client Browser" as ClientBrowser
participant "Cloudflare" as Cloudflare
participant "Cloudflare Tunnel" as CloudflareTunnel
participant "HoppyBrew" as HoppyBrew
participant "PostgreSQL" as PostgreSQL

Brewer -> ClientBrowser : Clicks Create Recipe
ClientBrowser -> Cloudflare : Sends Request
Cloudflare -> CloudflareTunnel : Routes Request
CloudflareTunnel -> HoppyBrew : Routes Request
HoppyBrew -> PostgreSQL : Queries Database
PostgreSQL --> HoppyBrew : Returns Data
HoppyBrew --> CloudflareTunnel : Returns Data
CloudflareTunnel --> Cloudflare : Returns Data
Cloudflare --> ClientBrowser : Returns Data
ClientBrowser --> Brewer : Displays Data

@enduml
    </code>
</pre>

![Create Recipe](../images/08-Create-Recipe.png)

## Update Recipe

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 09-Update-Recipe

actor Brewer as Brewer
participant "Client Browser" as ClientBrowser
participant "Cloudflare" as Cloudflare
participant "Cloudflare Tunnel" as CloudflareTunnel
participant "HoppyBrew" as HoppyBrew
participant "PostgreSQL" as PostgreSQL

Brewer -> ClientBrowser : Clicks Update Recipe
ClientBrowser -> Cloudflare : Sends Request
Cloudflare -> CloudflareTunnel : Routes Request
CloudflareTunnel -> HoppyBrew : Routes Request
HoppyBrew -> PostgreSQL : Queries Database
PostgreSQL --> HoppyBrew : Returns Data
HoppyBrew --> CloudflareTunnel : Returns Data
CloudflareTunnel --> Cloudflare : Returns Data
Cloudflare --> ClientBrowser : Returns Data
ClientBrowser --> Brewer : Displays Data

@enduml
    </code>
</pre>

![Update Recipe](../images/09-Update-Recipe.png)






## \<Runtime Scenario 1\>

- *\<insert runtime diagram or textual description of the scenario\>*

- *\<insert description of the notable aspects of the interactions between the building block instances depicted in this diagram.\>*

## \<Runtime Scenario 2\>

## …

## \<Runtime Scenario n\>
