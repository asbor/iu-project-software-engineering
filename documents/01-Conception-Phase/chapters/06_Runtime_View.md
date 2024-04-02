# Runtime View

User interactions with the system are depicted in the following sequence diagrams.

## CRUD Recipe

<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
@startuml 06-Runtime-View-CRUD-Recipe

actor Brewer as Brewer
participant "Client Browser" as ClientBrowser
participant "Cloudflare" as Cloudflare
participant "Cloudflare Tunnel" as CloudflareTunnel
participant "HoppyBrew" as HoppyBrew
participant "PostgreSQL" as PostgreSQL

Brewer -> ClientBrowser : 1. Create Recipe
ClientBrowser -> Cloudflare : 2. Send Request
Cloudflare -> CloudflareTunnel : 3. Route Request
CloudflareTunnel -> HoppyBrew : 4. Receive Request
HoppyBrew -> PostgreSQL : 5. Store Recipe
PostgreSQL -> HoppyBrew : 6. Return Response
HoppyBrew -> CloudflareTunnel : 7. Send Response
CloudflareTunnel -> Cloudflare : 8. Route Response
Cloudflare -> ClientBrowser : 9. Receive Response

@enduml
    </code>
</pre>






## \<Runtime Scenario 1\>

- *\<insert runtime diagram or textual description of the scenario\>*

- *\<insert description of the notable aspects of the interactions between the building block instances depicted in this diagram.\>*

## \<Runtime Scenario 2\>

## …

## \<Runtime Scenario n\>
