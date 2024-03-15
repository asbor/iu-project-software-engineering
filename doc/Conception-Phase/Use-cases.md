# Use-cases

![alt text](../Use-Case-Diagrams-(EA)/HoppyBrew.bmp)

## Use-case 1: Create a new user

### Description

This use-case describes the process of creating a new user in the system.

### Actors

- User
- System
- Database

### Pre-conditions

- The user is not already registered in the system.
- The user has a valid email address.
- The user has a valid username.
- The user has a valid password.

### Post-conditions

- The user is registered in the system.
- The user can log in to the system.
- The user can use the system.
- The user can log out of the system.
- The user can delete their account.
- The user can reset their password.
- The user can change their password.
- The user can change their email address.

### Main Scenario

1. The user navigates to the registration page.
2. The user enters their email address, username, and password.
3. The user clicks the "Register" button.
4. The system validates the user's input.
5. The system creates a new user in the database.
6. The system sends a confirmation email to the user.
7. The user clicks the link in the confirmation email.
8. The system activates the user's account.
9. The user is redirected to the login page.
10. The user logs in to the system.
11. The user is redirected to the home page.
12. The user can use the system.
13. The user can log out of the system.
14. The user can delete their account.
15. The user can reset their password.
16. The user can change their password.

### Alternative Scenarios

- The user enters an invalid email address, username, or password.
- The user clicks the "Register" button without entering any information.
- The user clicks the "Register" button without entering a valid email address.
- The user clicks the "Register" button without entering a valid username.
- The user clicks the "Register" button without entering a valid password.
- The user enters an email address that is already registered in the system.
- The user enters a username that is already registered in the system.
- The user does not receive the confirmation email.
- The user does not click the link in the confirmation email.
- The user enters an incorrect confirmation code.
- The user enters an incorrect email address, username, or password when logging in.

### Notes

- The user's email address, username, and password must be unique.
- The user's email address must be valid.
- The user's username must be valid.
- The user's password must be valid.
- The confirmation email must be sent within a reasonable amount of time.
- The confirmation code must be valid for a reasonable amount of time.
- The user's account must be activated within a reasonable amount of time.

[text](plantuml/UseCase1.puml)

