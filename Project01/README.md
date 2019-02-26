# Feature 1 ( Script Input ) 
1. The user selects a command between 1 and 4 for the different features.
2. Whatever feature is selected wil be executed by the system
3. Any number selected will display the feature to be executed by the system
4. Any other number other than 1 - 4 will diaplay an error message because ther is no such input
5. If more than one number is selected, it wont be executed 

# Feature 2  (Creating a TODO log)
1. Check if the todo.log file exists
2. If it does, the system should remove it
3. Defined a variable "search" that checks every file in the current repo
4. For every word found from the "search", read the each line in the file
5. Put each of these words in a file todo.log with #TODO in front of it 
 

# Feature 4 (Deleting all untracked and files ending in the extension **.tmp**)
*This is how to use the script*
1. Create a file in current directory (sample.tmp)
2. Do not **git add** the file (*this makes it untracked*)
3. Git status will show that there is one *untracked* file 
   >On branch project01
   >Untracked files: 
   >                sample.tmp 
4. Use the command * git clean -n * (This shows the untacked file that would be deleted)
   *$git clean -n*
   >Would remove sample.tmp
5. Use the command * git clean -f * (This actually deletes the file)
   *$git clean -f*
   >Removing sample.tmp

 
