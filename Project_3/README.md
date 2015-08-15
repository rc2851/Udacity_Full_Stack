## Udacity Project 3 - Item Catalog

This project displays restaurant menu item, and permits authenticated users
to add, edit, and delete menu item.

<hr>
### Virtual machine setup:
	1. Install Git
		http://git-scm.com/downloads	
	2. Install Vagrant and VirtualBox
		Vagrant:    http://vagrantup.com/
		VirtualBox: https://www.virtualbox.org/
	3. Use Git to clone the fullstack-nanodegree-vm repository
		From the terminal type the following:
		git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack
	4. Launch the Vagrant VM
		Change directory, type: cd fullstack/vagrant
		Launch the virtual machine, type: vagrant up 
	5. Login to the virtual machine
		Type: vagrant ssh 

	*To stop the virtual machine type: vagrant halt
<hr>
### Steps to run the Item Catalog project:

	Copy the contects from GitHub to the directory (..\GitHub\fullstack\vagrant\oauth)
	Do the following from the Vagrant VM:
	Type "python database_setup.py" to setup the database.
	Type "python lotsofmenus.py" to populate the database with restaurants and menu items. 
	Type "python project.py" to run the web server. 
	Type "http://localhost:5000/restaurants" in the address bar of Mozilla Firefox to view the restaurant menu app.  

	