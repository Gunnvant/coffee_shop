# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

This application lets users:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.

## How to run:

### Frontend:
Go to the frontend folder and run ```npm install``` followed by ```ionic serve```. If you are on windows machine use node.js terminal to run ```ionic serve```

### Backend:
Go to backend folder and created a venv, then run ```pip install -r requirements.txt```

### Running tests:
Populate the db with dummy data using ```backend/generate_db.py```. Then import the postman collection in ```/backend``` directory. Finally run the tests

