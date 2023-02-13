#Imports

import sys
import shutil
import pathlib

from Bio import SeqIO
from Bio import Entrez

#Created lists for the functions bellow

list_strains = ['TW20', 'M92', 'Be62', 'Gv88', 'Z172', 'Gv51', 'KG-03', 'CR14-035']
list_accns=['FN433596.1', 'CP015447.2', 'CP012013.1', 'CP012018.1', 'CP006838.1', 'CP012015.1', 'AP019542.1', 'CP020544.1']



'''
Function: eSearch

Here we use Biopython package to connect to NCBI database and do a eSearch with 2 parameters "db" and "term"
That refers to which database we are going to look for ou sequences and the accession number or the "term" that we are going to use to find them respectively
'''

def eSearch(db, term):

    Entrez.email = 'verygudLondonyes@gmail.com'

    eSearch = Entrez.esearch(db=db, term=term, usehistory="y", retmax = 9999)
    eSearchResult = Entrez.read(eSearch)
    return eSearchResult




'''
Function: printOutputToFile

This one will make every output that goes to the standard output to a file
Parameters are path (path of the file), type (type/extension of the file) and output (the output that would appear in the cmd it's going to be in the file)
'''

def printOutputToFile(path, type, output):

    stdout= sys.stdout
    sys.stdout= open(path, type)

    print(output)

    sys.stdout= stdout

    return None



'''
Function: mkdir_gbks

Here we create the folder where the genbank files will be, using pathlib package
'''

def mkdir_gbks():

    for i in list_strains:
        pathlib.Path('gbks').mkdir(parents=True, exist_ok=True)



'''
Function: rename_file2strain

Here we rename the genbank file extension from .gb to .gbk so that GIPSy can work with them
Using the Biopython package to get the description section of each gbk and shutil's to move the file to its folder
Parameters is only the file name (file_name)
'''

def rename_file2strain(file_name):

    gbk = SeqIO.read(file_name, "genbank")
    name_seq = gbk.description

    if name_seq.split()[2]=="strain":
        strain = name_seq.split()[3]

    elif name_seq.split()[2]=="KG-03":
        strain = name_seq.split()[2]

    else:
        strain = name_seq.split()[4][:-1]

    source="strain.gbk"
    destination='gbks/'+strain+".gbk"

    shutil.move(source, destination)



'''
Function: eFetch

Here we do the eFetch, which is a Biopython package to fecth the sequences from NCBI's database
So, for each id (id_) in the list of IDs that comes in the eSearch do the fetch, print the standard output to the gbk, rename it and move it to the folder "gbks"
'''

def eFetch():

    for id_ in eSearch["IdList"]:

        eFetch = Entrez.efetch(db="nucleotide", id=id_, rettype="gb", retmode="text")
        text = eFetch.read()

        printOutputToFile("strain.gbk", "w", text)

        rename_file2strain("strain.gbk")




#Execution of each function
eSearch=eSearch("nucleotide", "FN433596.1,CP015447.2,CP012013.1,CP012018.1,CP006838.1,CP012015.1,AP019542.1,CP020544.1")
mkdir_gbks()
eFetch()

