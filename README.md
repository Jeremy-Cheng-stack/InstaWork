# InstaWork Basic Design

This is the basic design for Instawork Full-Stack take-home assignment. Css has not been fully implemented so it is very bare bones looking. The focus is on Django to have everything be able to run in the backend properly.

## Building the Project
### building through the terminal
Have pipenv installed first <br/>
`pip3 install pipenv`.
<br/>
Then you can work in the virtual environment through the following command inside the work folder:<br/>
`pipenv shell`.
<br/><br/>
Once the vm is setup, you can start the server through the command: <br/>`python3 manage.py runserver`
<br/>
## Testing
Here are some screenshots of what the application looks like.
<br/><br/>
Home Page with the list of members:<br/>
<img width="398" alt="Screen Shot 2023-02-03 at 10 17 15 PM" src="https://user-images.githubusercontent.com/81793294/216745334-21ad33c9-a57f-4f11-a675-4c1890e2731b.png"><br/>
Add team member to the list:<br/>
<img width="317" alt="Screen Shot 2023-02-03 at 10 17 29 PM" src="https://user-images.githubusercontent.com/81793294/216745339-e401e499-92d6-408a-87bf-a474de58201d.png"><br/>
Edit a team member from the list:<br/>
<img width="335" alt="Screen Shot 2023-02-03 at 10 17 40 PM" src="https://user-images.githubusercontent.com/81793294/216745340-7cb9809c-1dde-4e87-9e64-479e56d34e1b.png"><br/>
Delete screen after delete button is clicked: <br/>
<img width="330" alt="Screen Shot 2023-02-03 at 10 17 49 PM" src="https://user-images.githubusercontent.com/81793294/216745344-c49783b4-ac67-41d0-b44a-c7a048d9d06c.png"><br/><br/>
### Note
* Data is stored on sqlite3 which can be accessed through /admin/
* The edit person page can be accessed by clicking on a person's name
* Best result page can be seen with 1440px screen or greater, but of course it works with any screen size
