# Backend Coding Challenge

At aspaara a squad of superheroes works on giving superpowers to planning teams.
Through our product dashboard, we give insights into data – a true super-vision
superpower. Join forces with us and build a dashboard of the future!

![aspaara superhero](aspaara_superhero.png)

## Goal

Create a simple backend application that provides an API for a dashboard which
allows a planner to get insights into client and planning information.

You will find the corresponding data that needs to be imported into the database
in `planning.json`, which contains around 10k records.

## Requirements

1. Create proper database tables that can fit the data model.
2. Create a script that imports the data into the database (sqlite).
3. Create REST APIs to get the planning data from the database.
    1. The APIs don't need to be complete, just create what you can in the
       available time.
    2. Please include at least one example on how to do each of the following:
        1. pagination
        2. sorting
        3. filtering / searching

## Data Model

* ID: integer (unique, required)
* Original ID: string (unique, required)
* Talent ID: string (optional)
* Talent Name: string (optional)
* Talent Grade: string (optional)
* Booking Grade: string (optional)
* Operating Unit: string (required)
* Office City: string (optional)
* Office Postal Code: string (required)
* Job Manager Name: string (optional)
* Job Manager ID: string (optional)
* Total Hours: float (required)
* Start Date: datetime (required)
* End Date: datetime (required)
* Client Name: string (optional)
* Client ID: string (required)
* Industry: string (optional)
* Required Skills: array of key-value pair (optional)
* Optional Skills: array of key-value pair (optional)
* Is Unassigned: boolean

## Preferred Tech Stack

* Python 3.8+
* FastAPI
* SQLAlchemy

## Submission

* Please fork the project, commit and push your implementation and add
  `sundara.amancharla@aspaara.com` as a contributor.
* Please update the README with any additional details or steps that are
  required to run your implementation.
* We understand that there is a limited amount of time, so it does not have to
  be perfect or 100% finished. Plan to spend no more than 2-3 hours on it.

For any additional questions on the task please feel free to email
`sundara.amancharla@aspaara.com`.


How to run the project:

Create a virtual environment for the project(assuming you have created the virtual environment, follow the below instructions)

The project has 2 parts. Script and the api file.

1) Open the project in your favorite IDE and activate the Virtual Environment.
2) Install requirments using 'pip install -r requirements.txt'
3) Run the following command to create initiate sqlite database and create tables using model. Command: uvicorn main:app --reload
4) You will see a database file by the name of planning.db in your main directory. (So far so good)

Script to populate db
5) Now go into the scripts folder in the project and run the 'load_json_to_db.py' file. You can run it using the command 'python load_json_to_db' or you can directly run it through your IDE (if you're using PyCharm then simply right click anywhere in the file and select 'run load_json_to_db' option
6) Instruction 5 will populate the table with planning.json file data. 
7) main.py file contains all of the API's to display data. 
8) Templates have been also used to display a limited amount of data just for UI purpose to see the implementation. 

After following the above instructions, you can simply hit http://127.0.0.1:8000/ url in the browser and interact with all the API's. It is a very basic implementation of the 3 mentione API's just to deliver the idea of the task and its solution. Might not be the best solution but tried my best in the given time. 
