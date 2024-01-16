# Python recipe app (command line version)

**Table of content**

- [Project description](#project-description)
- [User interface](#user-interface)
- [Technical aspects](#technical-aspects)
- [App dependencies ](#app-dependencies)


## Project description

This Recipe app (Command Line Interface version) was created to allow people to manage recipes. Users can create, read, modify and delete recipes, as well as search for recipes based on ingredients. For each recipe, users can add the recipe name, ingredients and cooking time, which then automatically calculate (based on the two latest elements) a difficulty level. 

Users can perform those different operations from the main menu of the application.

## User interface

Since all input and output takes place on a command line for this project, the UI is limited in terms of presentation. Below is a representation of what the app main menu looks like.

**Pick a choice:**
1. Create a recipe
2. View all recipes
3. Search for a recipe by ingredient
4. Edit a recipe
5. Delete a recipe  
Type 'quit' to exit  
Your choice (pick a number or type 'quit'):
  
## Technical aspects

The Recipe app works on Python 3.6+ installations and is connected to a MySQL database locally hosted.

## App dependencies

The following packages and dependencies are required for the Recipe web app to work (also accessible via the requirement.txt file):

asttokens==2.4.0  
backcall==0.2.0  
colorama==0.4.6  
decorator==5.1.1  
executing==2.0.0  
ipython==8.12.3  
jedi==0.19.1  
matplotlib-inline==0.1.6  
parso==0.8.3  
pickleshare==0.7.5  
prompt-toolkit==3.0.39  
pure-eval==0.2.2  
Pygments==2.16.1  
six==1.16.0  
stack-data==0.6.3  
traitlets==5.11.2  
typing_extensions==4.8.0  
wcwidth==0.2.8  
