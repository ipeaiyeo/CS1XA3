#!/bin/bash -i

if [$# -eq 1 ]
then
   if [ $1 -eq 1 ]
   then
       echo "Create a TODO log for me"
       if [ -e "todo.log" ]
       then
          rm todo.log
       fi
       search=$(git ls-files)
       for word in $search;
       do
        while IFS= read eachLine
        do
           echo $eachLine "#TODO" >> todo.log
        done <"$word"
       done
   elif [ $1 -eq 2 ]
   then
       echo "This is the COMPILE ERROR LOG feature"
   elif  [$1 -eq 3 ]
   then
       echo "This is the MERGE LOG feature"
   elif [ $1 -eq 4 ]
   then
       echo "This is the DELETE TEMPORARY FILE feature"
   else
       echo "The input entered is wrong"
       echo "Your input has to be between 1 and 4"
   fi
else
    echo "This is an incorrect number of arguments"
fi

