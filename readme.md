#Benchmarking NodeJS VS Python

Code used to benchmark [nodejs](http://nodejs.org/) (using [expressjs](http://expressjs.com/) framework)  and [python](http://www.python.org/) (using [flask](http://flask.pocoo.org/) framework).

## Installation Instructions
These instructions assume an [Ubuntu](http://en.wikipedia.org/wiki/Ubuntu_%28operating_system%29) Linux operating system environment, but with knowledge about one's target server, it could be deployed anywhere.

### Clone This Repository
To clone this repository, type the following:

`git clone https://github.com/barrysteyn/benchmark-node_vs_python.git`

### Node Setup
The following is required to be installed (I suggest installing it in the order presented below)

* [npm](https://npmjs.org/) - the node package manager. To install on ubuntu, type `sudo apt-get install npm` (works on Ubuntu versions 11.10 and higher).
* [nvm](https://github.com/creationix/nvm) - the node versioning manager (look at [nvm documentation](https://github.com/creationix/nvm) for install instructions).
* [NodeJS](http://nodejs.org/) - install Node using nvm as presented above (see the [nvm documentation](https://github.com/creationix/nvm) for instructions how to do this).

Go to the *node* folder of the cloned repository and type `npm install`. This will install Node's local dependencies that the application requires. 

Once the above has been completed, Node must be setup as an [upstart](http://upstart.ubuntu.com/) service. Instructions on how to do this can be found [here](http://doctrina.org/NodeJS-Under-NVM-With-Upstart.html).

### Python Setup

### Nginx Setup

## System Setup For Running The Tests

