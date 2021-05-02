Gazebo, Turtlebot3, web browser, gzweb.

What is gzweb?
GzWeb is usually installed on an Ubuntu server. Gzweb is a client for Gazebo which runs on a web browser. Once the server is set up and running, clients can interact with the simulation simply by accessing the server's URL on a web browser.

Installing Gazebo, gzweb and dependencies:
The main dependencies for GzWeb are the Gazebo development libraries, version 9 or greater, and NodeJS version 6 or greater.

	sudo apt install gazebo9 libgazebo9-dev

# Run the following to install dependencies:
	sudo apt install libjansson-dev libboost-dev imagemagick libtinyxml-dev mercurial cmake build-essential

# Next install nodejs and npm using node's version manager nvm:
 # install nvm
 	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash

 # source .bashrc so we can use the nvm cmd
 	source ~/.bashrc

 # install node version 6 or above
 	nvm install 6

Build GzWeb:
# Clone the repository into a directory in your home folder for example:
	cd ~; git clone https://github.com/osrf/gzweb

#Enter the GzWeb repository and switch to the latest release branch:
	cd ~/gzweb
	git checkout gzweb_1.4.1
	
	
# The first time you build, you'll need to gather all the Gazebo models which you want to simulate in the right directory ('http/client/assets') and prepare them for the web.

# Before running the deploy script, it's important to source the Gazebo setup.sh file:

# If you installed gazebo via deb packages:
	source /usr/share/gazebo/setup.sh
	
# If you did a source install then:
	source <YOUR_GAZEBO_PATH>/share/gazebo/setup.sh
	
# Run the deploy script, this downloads models from the web and may take a couple of minutes, see more options below.
	npm run deploy --- -m
	
Running GZweb:
Running GzWeb involves the following pieces:

    gzserver running the headless Gazebo simulation (runs by default on http://127.0.0.1:11345)

    GzWeb's NodeJS server which communicates with gzserver using Gazebo Transport. It works as a bridge between the Javascript and the C++ code.

    An HTTP server which serves static content such as models and website assets (icons, HTML, CSS, client-side Javascript...)

    A Websocket server which forwards simulation updates coming from gzserver to the browser

    A browser client which connects to the HTTP and websocket servers
    
# Start them as follows:

#1. On the server machine, start gazebo or gzserver first, it's recommended to run in verbose mode so you see debug messages:
	gzserver --verbose
	
#2. On another terminal, from your GzWeb directory, run the following command to start both the HTTP and Websocket servers:
	npm start

#3 Open a browser that has WebGL and websocket support (i.e. most modern browsers) and point it to the IP address and port where the HTTP server is started, for example:
	http://localhost:8080
	
#4. To stop gzserver or the GzWeb servers, just press Ctrl+C in their terminals.

# Run the python script to see the turtle in action in our web browser:

run your python turtlebot3 file in catkin_ws directory:

	rosrun name_of_the_package turtlebot3_move_gz.py

