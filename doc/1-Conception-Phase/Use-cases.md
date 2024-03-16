# Use-cases

In this section, we will identify the actors and use-cases for the brewing system. The actors are the entities that interact with the system, and the use-cases are the tasks that the actors perform. The following approach to identify the actors and use cases stems from the book [@UML@Classroom].

## Questions for identifying actors

- Who uses the main use cases?
- Who needs support for their daily work?
- Who is responsible for system administration?
- What are the external devices/(software) systems with which the system must communicate?
- Who has an interest in the results of the system?

The following actors are identified:

- **Administrator (Admin):** Oversees and manages the overall operation of the brewing system.
- **Brewer (Brew):** Engages in the brewing process and utilizes the system's functionalities.
- **Database (DB):** Stores and manages data related to users, recipes, equipment, and other brewing-related information.
- **ISpindel (Spindel):** Provides real-time data collection capabilities for monitoring the fermentation process.

## Questions for identifying use cases

- What are the main tasks that an actor must perform?
- Does and actor want to query or even modify information contained in the system?
- Does an actor want to inform the system about changes in other systems?
- Should an actor be informed about unexpected events within the system?

The following use-cases are identified:

The main tasks that the actors must perform are:

- **Manage Recipes:** create, read, update, and delete (CRUD) recipes.
- **Manage Equipment:** CRUD brewing equipment.
- **Manage Batches:** CRUD brewing batches, and update all parameters during all four brewing phases (Planing, Brewing, Fermentation, and Conditioning).
- **Manage Inventory:** CRUD inventory items.
- **Manage schedule:** CRUD brewing schedule.
- **Monitor Fermentation:** real-time monitoring of the fermentation process.
- **Manage Users:** CRUD users.
- **Manage settings:** Update system settings and configurations.
- **Manage Notifications:** CRUD notifications.

Does an actor want to query or even modify information contained in the system?

- **Query Recipes:** Query recipes based on different criteria.
- **Query Equipment:** Query equipment based on different criteria.
- **Query Batches:** Query batches based on different criteria.
- **Query Inventory:** Query inventory items based on different criteria.
- **Query schedule:** Query brewing schedule based on different criteria.
- **Query Users:** Query users based on different criteria.
- **Query system logs:** Query system logs based on different criteria.
- **Query Notifications:** Query notifications based on different criteria.

Does an actor want to inform the system about changes in other systems?

- **Inform about Equipment:** Inform the system about changes in the brewing equipment.
- **Inform about Inventory:** Inform the system about changes in the inventory.
- **Inform about schedule:** Inform the system about changes in the brewing schedule.

Should an actor be informed about unexpected events within the system?

- **Notify Admin:** Notify the admin about unexpected events within the system.
- **Notify Brewer:** Notify the brewer about unexpected events within the system.

# Use cases

Key | Value
--- | ---
**Name:** | Manage Recipes
**Short Description:** | CRUD recipes.
**Preconditions:** | The actor must be logged in.
**Postconditions:** | The recipe is created, read, updated, or deleted.
**Error situations:** | The recipe already exists<br>the recipe does not exist<br>the recipe is not valid.
System state in the event of an error | The system state remains unchanged.
Actors | Admin, Brewer
Trigger | The actor wants to create, read, update, or delete a recipe.
Standard process | The actor selects the recipe to be created, read, updated, or deleted.
Alternative processes | None


