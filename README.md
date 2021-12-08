# Message in A Bottle - Messages

This is the source code of Message in a Bottle Messages microservice, self project of _Advanced Software Engineering_ course, University of Pisa.

## Team info

- The *squad id* is **Squad 3**.
- *Team leader* is [Antonio Pace](https://github.com/pacant) and the other members are [Giulio Piva](https://github.com/gystemd), [Alessandro Cecchi](https://github.com/PaolinoRossi) and [Francesco Carli](https://github.com/fcarli3).

#### Members
Persons that have developed this microservice are marked in **bold**.
| Name and Surname      | Email                           |
| ----------------      | ------------------------------- |
|   Antonio Pace        |   a.pace10@studenti.uipi.it     |
|   Giulio Piva         |   g.piva2@studenti.unipi.it     |
| **Alessandro Cecchi** |   a.cecchi8@studenti.unipi.it   |
|   Francesco Carli     |   f.carli8@studenti.unipi.it    |
|                       |                                 |


## Instructions

### Initialization

To setup the project initially you have to run these commands inside the project's root.

`virtualenv -p python3 venv`

`source venv/bin/activate`

`pip install -r requirements.dev.txt`

### Run the project

To run the project you have to setup the flask environment, you can do it by executing the following commands:

cp env_file .env
export FLASK_ENV=development
flask run

#### Flask routes

To show the primary routes of flask application you can issue the following command:

`flask routes`

The default swagger-ui interface is available on _/ui_

#### Executing migrations

If you change something in the models package or you create a new model, you have to run these commands to apply the modifications:

`flask db migrate -m '<message>'`

and

`flask db upgrade`

#### Application Environments

The available environments are:

-   debug
-   development
-   testing
-   production

If you want to run the application with development environment you can run the `run.sh` script.

**Note:** if you use `docker-compose up` you are going to startup a production ready microservice, hence postgres will be used as default database and gunicorn will serve your application.

If you are developing application and you want to have the debug tools, you can start application locally (without `docker-compose`) by executing `bash run.sh`.

### Run tests

To run all the tests, execute the following command:

`python -m pytest`

You can also specify one or more specific test files, in order to run only those specific tests. In case you also want to see the overall coverage of the tests, execute the following command:

`python -m pytest --cov=mib`

In order to know what are the lines of codes which are not covered by the tests, execute the command:

`python -m pytest --cov-report term-missing`

You can run tests also executing command `tox` from the project's root folder.

## Conventions

-   Name of files are snake_cased
-   Name of methods, properties, variables are snake_cased
-   Name of classes are PascalCased
-   Name of constants are UPPERCASE
-   The class name of managers are in the format `<BeanName>Manager`