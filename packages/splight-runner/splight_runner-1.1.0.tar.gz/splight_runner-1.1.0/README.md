# Splight Runner

---

The `splight-runner` package is a tool for running processes that may interact 
with the **Splight Engine** in order to report monitoring information of the 
process.

## Description

The `splight-runner` main functionality is to run different kinds of *Python* 
processes related in some way to the **Splight Engine**, for example,
*components* that were developed using the **Splight Library**. 

For this reason, the different features in the runner are for reporting the 
status of the process and centralizing logs to be accessed through the 
**Splight Engine**. So the `splight-runner` is used when the process is 
launched from the **Splight Engine**, this means that it should not be used 
during the development of the component even though the process will be
running under the `splight-runner`.

## Usage

The package has different commands that can be used. Here you can find a list
of all the commands with a short description and how to use them.

### Running Components

The first command is used for running components that use the **Splight Library**. 
The command is
```bash
splight-runner run-component <path>/main.py --component-id=<component_id>
```
This command will execute the component whose main file is called `main.py` and 
will modify some default functioning in order to report the status of the component and
send the logs of the component to the **Splight Engine**. In the next sections, you can 
find how these modifications are done by the `splight-runner`.

In order to this command work as expected some environment variables are needed. 
The following are the list of variables that should be configured before running the 
command:
```bash
SPLIGHT_ACCESS_ID=<access_id>
SPLIGHT_SECRET_KEY=<secret_key
SPLIGHT_PLATFORM_API_HOST=https://api.splight-ai.com
COMPONENT_ID=<component_id>
```
Some of the variables are pointing to the production environment, but if you are 
interested in using another environment like "integration" or maybe a local 
environment you need to modify the corresponding variable value.

It is important to mention that the `splight-runner` should be used for components that
use the **Splight Lib** and **Splight CLI** grater than version `4.0.0`. For components
with older versions we can't ensure the proper functioning.

## Structure

You may be asking what the `splight-runner` does in order to do whatever it does.
Well, that's not an easy question to respond but let's try to explain a little bit.

So far, the package has two main functionalities, sending logs and reporting status. 
With the two features we already have a lot of magic is happening, but maybe in the future
we will add some more.

`splight-runner` works as a wrapper around the process that will be executed, 
this means some configurations are done, so the process in question is executed.

For example, when the command `run-component` is used, the environment variable
`PYTHONPATH` is modified in order to include the directory where the file `sitecustomize.py`
of the `splight-runner` is located. That file is a *Python* configuration file that can 
be used to customize the behavior of Python's site module. The site module is 
responsible for setting up Python's runtime environment, including configuring 
paths, importing modules, and performing other site-specific tasks.

So, using this file we can modify the default behaviors of libraries, for example, we 
can modify the import process of modules or libraries in order to change or add
a new behavior. This way we can modify the `logging` module and intercept 
the logging process to show the logs messages and also send the logs messages
to the **Splight Engine**. Some similar implementation is used for 
reporting the component's status. 


## Development and Contributing

Since the main goal of the tool is to be used for running different kinds of 
`Python` processes, is mandatory not to interfere with the process's 
dependencies, this should be considered when adding new features for the 
`splight-runner`. This is the reason why some basic functionalities 
are implemented in the source code and not imported from a third-party 
library, for example, a command parser for the different commands was created 
in the code and no library was used like `click` or `typer`.

The package is fully dockerized, for testing new features you can use the 
docker image that can be build with 
the command
```bash
make build
```
For running the docker container the command is
```bash
make start
```
and to stop the container:
```bash
make stop
```

It is important to note that testing new features in the `splight-runner` is 
not an easy task, you may need to modify the docker-compose file in order to 
include new volumes.
