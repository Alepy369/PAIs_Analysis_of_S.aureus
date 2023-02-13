#Imports

import os
import pathlib
import shutil


#Created lists for the functions bellow

list_accns=['FN433596.1', 'CP015447.2', 'CP012013.1', 'CP012018.1', 'CP006838.1', 'CP012015.1', 'AP019542.1', 'CP020544.1']
list_strains = ['TW20', 'M92', 'Be62', 'Gv88', 'Z172', 'Gv51', 'KG-03', 'CR14-035']



'''
Package zip will make list_accns and list_strains 1 list only that will be called list_phaster
This will make list_phaster look like this:

print(list_phaster)

Output:
[[accn, strain], [accn, strain], etc...]]
'''

list_phaster= zip (list_accns, list_strains)




'''
Function: mkdir

Here we create the directory "phaster_info/(name of the strain)" where the output files will be, using pathlib package
'''

def mkdir():

    for i in list_strains:
        pathlib.Path('phaster_info/'+i).mkdir(parents=True, exist_ok=True)




'''
Function: phaster

Here we use the online API from "Phaster" in order to analyze the phages of each genome/strain

The for loop will read each value in list_phaster in order ([accn, strain] being i the "accn" and j "strain") 
With the package os we can run linux/bash commands like if we were executing them in the terminal

Firstly, it will get the xml from phaster's API that will have the results link
Then we will grep the xml to get the link and redirect it to a "strain".txt file

Next, it opens the file and runs a wget command again with the results link
'''

def phaster():

   for i,j in list_phaster:

       os.system('wget http://phaster.ca/phaster_api?acc='+i+' -O '+j+'.xml')
       grep = "grep -i 'zip' "+j+".xml | sed 's/summary.*//' | tr -d ',' | sed 's/.*://' | tail -c +2 | head -c -2 | head -c -1 > "+j+".txt"
       os.system(grep)

       file = open(j+".txt")
       os.system('wget http://'+file.read())


'''
Function: rm_files

Here we remove every xml and txt file from our directory because they won't be needed anymore
'''

def rm_files():

    os.system('rm *.xml')
    os.system('rm *.txt')



#Execution of each function

mkdir()
phaster()
rm_files()

