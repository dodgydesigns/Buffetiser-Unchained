#!/bin/bash

cd /Users/mullsy/workspace/Buffetiser_Unchained

application='Buffetiser_Unchained'
application_directory=$(pwd)
server_name=$(hostname)
django_version=$(python3 -m django --version)


function info() {
    echo ""
	echo "	Application: 		" $application
	echo "	Current directory:	" $application_directory
	echo "	Django version:		" $django_version
	echo ""
}


function run_server() {
	# Start the built-in Django test server
    echo ""
	echo "Starting Django test server..."
	nohup python3 manage.py runserver > /dev/null 2>&1 & 
	echo ""
}

function kill_server() {
	# Stop the built-in Django test server
    echo ""
	echo "Killing Django test server."
	pkill -f runserver
	echo "Dead."
	echo ""
}

function make_migrations() {
	# By running makemigrations, you’re telling Django that you’ve made some changes to your models 
	# (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
    echo ""
	echo "Adding model changes to migration."
	python3 manage.py makemigrations buffetiser_main
	echo "Dead."
	echo ""
}

function migrate() {
	# The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables 
	# according to the database settings in your mysite/settings.py
    echo ""
	echo "Migrating to DB"
	python3 manage.py migrate
	echo "Dead."
	echo ""
}

function shell() {

    echo ""
	echo "Running interactive shell"
    python manage.py shell
}





menu(){
echo "
-----------------
1) Info
2) Run Server
3) Kill Server
4) Make Migrations
5) Migrate
6) Shell

0) Exit
-----------------
Choose an option: "
        read a
        case $a in
	        1) info ; menu ;;
	        2) run_server ; menu ;;
	        3) kill_server ; menu ;;
	        4) make_migrations ; menu ;;
	        5) migrate ; menu ;;
	        6) shell ; menu ;;
	        0) exit 0 ;;
        esac
}

# Call the menu function
menu