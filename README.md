# Python Recipe app (command line version)

**Content**

- Project description
- User interface
- Technical aspects (overview)
- Technical aspect (development)

## Project description

This Recipe app has been created to help users plan their next meals. Users can create and modify recipes with ingredients and cooking time, which then display a difficulty parameter automatically calculated by the app. Users can also search for recipes by their ingredients.

The Recipe app is separated in two development phases: 

**1-** First, a command line application, which is able to create, read, and modify recipes, as well as searching for recipes based on ingredients.

**2-** Second, a web application using the Django framework, built on the first deliverable (command line application) to deliver a more user-friendly UI for the Recipe app. 

**The current repository and README concerns the first part (command line application).** To see the second part related to Django, please visit the [following repository](placeholer).

> (insert link when Achievement 2 repository will be created)

## User interface

Since all input and output takes place on a command line for this first part of the project, the UI is limited in terms of presentation. Below is an image of what it looks like.

> (insert image of the command line version once complete)

  
## Technical aspects (overview)

The Recipe app works on Python 3.6+ installations and is connected to a MySQL database locally hosted.


## Technical aspects (development)

This section presents the development process of the command line application, step by step.

### Step 1

**1.1 – Python installation**

First open the Command Prompt, and type `python --version`. This allows to see if Python is already installed on the machine or not. If this command returns `python X.X.X` (version number), it means Python is already installed.  Note that a Python 3.8.x or 3.9.x version is required.

If Python is not installed, head over  [download version 3.8.7](https://www.python.org/downloads/release/python-387/) from Python official website and click on **Windows Installer** according to your system version (32-bit or 64-bit). Once downloaded, open the file and follow the installation instructions. 

**1.2 - Virtual environment creation**

Install the `virtualenvwrapper` package via the Command Prompt. Then,  create a new virtual environment by running the command `mkvirtualenv <the name you want>.`


**1.3 - First Python file creation** 

Still on the Command Prompt, move (cd) to the directory in which you want the Python code files to be located, and run the command `code .`. This will open Visual Code Studio, and allow creating a python file and start writing codes. Once the codes are written, save the file.

**1.4 - Running the Python code file**

Still on the Command Prompt (and in the folder path where the Python file  has been saved), run the command `python <script filename>`. This will start the Python interpreter and asks it to run commands from the specified script file. The results of the codes will then be displayed in the Command Prompt.

**Note**: If the codes aren't rendering as supposed in step 1.4, it's possible to use the Python shell REPL, and write the codes line by line directly in it to see the output for each line (which is useful to try out syntax or quick debugging).