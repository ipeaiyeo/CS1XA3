#!/bin/bash

if [ $1 -eq 1 ]
then
    echo "Create a Todo log"
    if [ -e "todo.log" ] ; then
       rm todo.log
    fi
    get=$(git ls-file)
    for file in $get;
    do
      while IFS= read eachLine
      do
        echo $line "#TODO" >> todo.log
      done <"$file"
    done
