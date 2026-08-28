#!/bin/bash

#Need to make sure there are at leat two files
if [ $# -lt 2 ]; then
	echo "FORMAT: $0 outputfile file1 file2 file3 etc..."
	exit 1
fi

#Need to assign the output file on the first argument
outputfile="$1"
shift

#Combine the files
cat "$@" > "$outputfile"

echo "Done! Files combined into: $outputfile"
