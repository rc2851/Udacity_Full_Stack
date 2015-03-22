## Udacity Project 2 - Tournament Results

This project is designed to support the Swiss style tournament by creating, storing,
and ranking tournament results on a Linux virtual machine.
<hr>
### Virtual machine setup:
	1. Install Git
		[Git](http://git-scm.com/downloads "Git").	
	2. Install [Vagrant](http://vagrantup.com/ "Vagrant") and [Vitual Box](https://www.virtualbox.org/ "Virtual Box")
	3. Use Git to clone the fullstack-nanodegree-vm repository
		From the terminal type the following:
		git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack
	4. Launch the Vagrant VM
		Change directory, type: cd fullstack/vagrant
		Launch the virtual machine, type: vagrant up 
	5. Login to the virtual machine
		Type: vagrant ssh 

	*When desired, to stop the virtual machine type: vagrant halt
<hr>
### Steps to run the Tournament Results project:
	1. Copy the following files to the location of the tournament directory on  
	   your computer: (..\GitHub\fullstack\vagrant\tournament)
			* tournament.py
			* tournament_test.py
			* tournament.sql
	2. Create Postgesql database.
		Type: psql
		name the database "tournament"
		At the prompt, type: CREATE DATABASE tournament;
		Type: \q
	3. Create database tables:
		Connect to database "tournament", type: psql tournament
		Run tournament.sql in Postgresql, type: \i tournament.sql
	4. Exit Postgresql
	   	Type: \q
	5. From the command prompt run the Tournament tester.
		Type: python tournament_test.py
