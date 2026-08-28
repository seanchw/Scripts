#!/bin/bash

#command should be echo '<encoded text>' | base64 -d

#Define the file path that we want to decode
read -p "What file would you like to decode in base64?: " user_input

#check if the file exists
if [ -f "$user_input" ]; then
    echo "Decoding..."
    content=$(cat "$user_input")
    echo $content | base64 -d
else
    echo "Error: File does not exist!"
    exit 1
fi
