#Benchmarking NodeJS VS Python

Code used to benchmark [NodeJS](http://nodejs.org/) (using [expressjs](http://expressjs.com/) framework) and [Python](http://www.python.org/) (using [flask](http://flask.pocoo.org/) framework).

# Installation Instructions
These instructions assume an [Ubuntu](http://en.wikipedia.org/wiki/Ubuntu_%28operating_system%29) Linux operating system environment, but with knowledge about one's target server, it could be deployed anywhere.

## Clone This Repository
To clone this repository, type the following:

`git clone https://github.com/barrysteyn/benchmark-node_vs_python.git`

## Node Setup
The following is required to be installed (I suggest installing it in the order presented below)

* [npm](https://npmjs.org/) - the node package manager. To install on ubuntu, type `sudo apt-get install npm` (works on Ubuntu versions 11.10 and higher).
* [nvm](https://github.com/creationix/nvm) - the node versioning manager (look at [nvm documentation](https://github.com/creationix/nvm) for install instructions).
* [NodeJS](http://nodejs.org/) - install Node using nvm as presented above (see the [nvm documentation](https://github.com/creationix/nvm) for instructions how to do this).

Go to the *node* folder of the cloned repository and type `npm install`. This will install Node's local dependencies that the application requires. 

###Make An Upstart Service For Node
Once the above has been completed, Node must be setup as an [upstart](http://upstart.ubuntu.com/) service. Instructions on how to do this can be found [here](http://doctrina.org/NodeJS-Under-NVM-With-Upstart.html).

## Python Setup
The following is required to be installed (again, install in the order presented)

* [Python](http://www.python.org/) - this comes installed by default on Ubuntu.
* Extra python libraries - `sudo apt-get install python-pip python-dev build-essential` (very important to install).
* [VirtualEnv](http://pypi.python.org/pypi/virtualenv) - Python virtual environment (to install, type  `pip install virtualenv`).
* [VirtualEnvWrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) - A set of shell scripts for [VirtualEnv](http://pypi.python.org/pypi/virtualenv) (to install, type `pip install virtualenvwrapper`).

Create an use a virtual environment called `python-flask-benchmark` by typing the following:

* `mkvirtualenv python-flask-benchmark`. 
* `workon python-flask-benchmark`.

Now install flask by typing `pip install Flask`.

###Make an Upstart Service For Python With Uwsgi
Note: Make sure that you are still in your virtual environment. Type `workon python-flask-benchmark` to ensure you are in it. Install [uwsgi](http://projects.unbit.it/uwsgi/) by typing `pip install uwsgi`. In order to determine exactly where [uwsgi](http://projects.unbit.it/uwsgi/) was installed, type the following:

* `cd ~`
* `find . -name uwsgi`

Look out for the path that ends in `python-flask-benchmark/bin/uwsgi` - this is the path that you will need. Once all this has been completed, [uwsgi](http://projects.unbit.it/uwsgi/) must be setup as an [upstart](http://upstart.ubuntu.com/) service. Instructions on how to do this can be found [here](http://doctrina.org/VirtualEnv-With-Upstart.html).

## Nginx Setup

# System Setup For Running The Tests

