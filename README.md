# Python recipe app (command line version)

**Table of content**

- [Project description](#project-description)
- [User interface](#user-interface)
- [Technical aspects (overview)](#technical-aspects-overview)
- [Technical aspect (development)](#technical-aspects-development)


## Project description

This Recipe app has been created to help users plan their next meals. Users can create and modify recipes with ingredients and cooking time, which then display a difficulty parameter automatically calculated by the app. Users can also search for recipes by their ingredients.

This project is separated in two parts: 

**1-** A command line application for the Recipe app, which is able to create, read, and modify recipes, as well as searching for recipes based on ingredients.

**2-** A web application using the Django framework, built on the first deliverable (command line application) to deliver a more user-friendly UI for the recipe app. 

**The current repository and README concerns the first part (command line application).** To see the second part related to Django, please visit the [following repository](placeholer). 

> (insert link when Achievement 2 repository will be created)

## User interface

Since all input and output takes place on a command line for this first part of the project, the UI is limited in terms of presentation. Below is an image of what it looks like.

> (insert image of the command line version once complete)

  
## Technical aspects (overview)

The Recipe app works on Python 3.6+ installations and is connected to a MySQL database locally hosted.


## Technical aspects (development)

**Table of content**

- [Step 1](#step-1)  - Setting up the Python environement
- [Step 2 ](#step-2) - Creating the data structures

### Step 1 

#### Setting up the Python environement

**1.1 – Python installation**

First, open the Command Prompt, and type `python --version`. This allows to see if Python is already installed on the machine or not. If this command returns `python X.X.X` (version number), it means Python is already installed.  Note that a Python 3.8.x or 3.9.x version is required.

If Python is not installed, head over  [download version 3.8.7](https://www.python.org/downloads/release/python-387/) from Python official website and click on **Windows Installer** according to your system version (32-bit or 64-bit). Once downloaded, open the file and follow the installation instructions. 

**1.2 - Virtual environment creation**

Install the `virtualenvwrapper` package via the Command Prompt. Then,  create a new virtual environment by running the command `mkvirtualenv <the name you want>` (**see point A in image below**).

![Virtual Environment Creation](https://github.com/AlexaCai/recipe-app-cli/blob/main/1.1/1%20-%20Virtual%20env.%20creation%20and%20VSC%20launching.png?raw=true)

**1.3 - First Python file creation** 

Still on the Command Prompt, move (cd) to the directory in which you want the Python code files to be located, and run the command `code .` (**see point B in image below**). This will open Visual Code Studio, and allow creating a python file and start writing codes. Once the codes are written, save the file.

![VCS launching](https://github.com/AlexaCai/recipe-app-cli/blob/main/1.1/1%20-%20Virtual%20env.%20creation%20and%20VSC%20launching.png?raw=true)


**1.4 - Running the Python code file**

Still on the Command Prompt (and in the folder path where the Python file  has been saved), run the command `python <script filename>` (**see point D in image below**). This will start the Python interpreter and asks it to run commands from the specified script file. The results of the codes will then be displayed in the Command Prompt.

**Note**: If the codes aren't rendering as supposed in step 1.4, it's possible to use the Python shell REPL running `python`, and write the codes line by line directly in it to see the output for each line (which is useful to try out syntax or quick debugging). **See point C in image below**.

![Python REPL and script running](https://github.com/AlexaCai/recipe-app-cli/blob/main/1.1/2%20-%20REPL%20testing%20and%20script%20running.png?raw=true)

### Step 2 

#### Creating the data structures 
*NOTE: The example images presented in this step have been realized using Command Prompt and iPython Shell

**2.1 – Creating a data structure to store each recipe information**

Create the following data structure to store each recipe information:

    recipe_1 = {
	    'name': 'recipe_name', 
	    'cooking_time': 0, 
		'ingredients': ['recipe_ingredients']
		}
Where:

- `recipe_1` = variable for X recipe
- `'name': 'recipe_name'` = first key-value (string)
- `'cooking_time': 0` = second key-value (integer)
- `'ingredients': ['recipe_ingredients']` = third key-value (list)

![Recipe data structure creation](https://github.com/AlexaCai/recipe-app-cli/blob/working-branch/1.2/2%20-data%20structure%20for%20recipes.png?raw=true)

The ***dictionary*** data structure is used to store each recipe information, since each recipe data (recipe name, cooking time and ingredients) needs to be individually labeled, and don't have to be tracked sequentially. A dictionary allows creating an unordered set of items (each of them being a key-value pair) related to a same general thematic (here the recipe) but without having related direct links. A dictionary also allows different data types in the key-value pairs such as string, integers and lists, making it a good choice to store recipes' information.

**2.2 – Creating a recipe**

Based on the data structure defined in step 2.1, add real information to create a recipe.

    recipe_1['name'] = 'tea'
    recipe_1['cooking_time'] = 5
    recipe_1['ingredients'] = ['Tea leaves', 'Sugar', 'Water']

![Recipe creation](https://github.com/AlexaCai/recipe-app-cli/blob/working-branch/1.2/3%20-%20first%20recipe%20creation%20.png?raw=true)

**2.3 – Creating a list that holds all created recipes**

To create a structure that displays all available / created recipes, a ***list*** data structure is used since it allows storing multiple elements and modify / delete them as required. This is particularly useful in the context of a recipe web app, where users could want to reorder, sort or modify recipes, for example. To do so, first create a list:

    all_recipes = [ ]

Then add the newly created recipe (recipe_1) to it:

    all_recipes.append(recipe_1)

![Recipe list creation](https://github.com/AlexaCai/recipe-app-cli/blob/working-branch/1.2/4%20-%20recipe%20list%20creation.png?raw=true)

**2.4 – Optionally, create more recipes**

Optionally, create more recipes for a better user experience and a more complete web app. To do so, steps 2.1 and 2.2 can be done again.

![Recipe list creation](https://github.com/AlexaCai/recipe-app-cli/blob/working-branch/1.2/5-%201additional%20recipes%20addition.png?raw=true)

![Recipe list creation](https://github.com/AlexaCai/recipe-app-cli/blob/working-branch/1.2/5-%202additional%20recipes%20addition.png?raw=true)
<br>

Then, add the newly created recipes to the list containing all recipes (all_recipes) using the same command as presented in step 2.3 :

    all_recipes.append(recipe_2)
    all_recipes.append(recipe_3)
    all_recipes.append(recipe_4)
    all_recipes.append(recipe_5)

![Recipe list creation](https://github.com/AlexaCai/recipe-app-cli/blob/working-branch/1.2/6%20-%20populating%20recipe%20list%20with%20additional%20recipes.png?raw=true)

**2.5 – Optionally, query the recipes in the list to retrieve some useful information**

Optionally, you can now retrieve different information out of the recipes added to the list (all_recipes). For example, to print the ingredients of each recipe, run the command:

    print(all_recipes[0]['ingredients'])
    print(all_recipes[1]['ingredients'])
    print(all_recipes[2]['ingredients'])
    print(all_recipes[3]['ingredients'])
    print(all_recipes[4]['ingredients'])

Where:
- `[0]` in `print(all_recipes[0]['ingredients'])` represent the index position of the first recipe in the list, and so on for the second one, the third one, etc.

![Recipe list creation](https://github.com/AlexaCai/recipe-app-cli/blob/working-branch/1.2/8%20-%20printing%20ingredients%20for%20each%20recipe%20in%20recipe%20list.png?raw=true)
