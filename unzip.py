#Imports

import os
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
Function: move

Using os and shutil packages to unzip the file and to move them to the respective directory
'''

def move():

    for i,j in list_phaster:

        os.system('unzip '+i+'.zip')

        source1='summary.txt'
        source2='detail.txt'
        source3='phage_regions.fna'
        destination='phaster_info/'+j

        shutil.move(source1, destination)
        shutil.move(source2, destination)
        shutil.move(source3, destination)




'''
Function: rm_files

Here we remove every zip file from our directory because they won't be needed anymore
'''

def rm_files():

    os.system('rm *.zip')




#Execution of each function
move()
rm_files()
