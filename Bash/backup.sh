#!/bin/bash

#Define what directory you would like to backup
read -p "What directory would you like to backup?: " user_input

#Check if the directory exists
if [ -d "$user_input" ]; then
	echo "Backing up directory: $user_input"
	zip -r ~/Desktop/backup.zip $user_input
	echo "Backup complete!"
else
	echo "Error: Directory does not exist"
	exit 1
fi
