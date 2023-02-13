# PAIs_Analysis_of_S.aureus

## Purpose

The main purpose of this project/report was to identify pathogenicity islands in Staphylococcus aureus. For that, we selected 8 strains to analyse.

The reference genome that was used was the strain [CR14-035](https://www.ncbi.nlm.nih.gov/nuccore/CP020544.1).

We used 3 different programs/web sites, [Phaster](https://phaster.ca/), [GIPSy](https://www.bioinformatics.org/download/gipsy/), [Patric database](https://www.bv-brc.org/).

The main program is GIPSy and it's with it that we were able to identify the PAIs (pathogenicity islands) in our strains. Phaster was for the phage analysis and Patric database (BV-BRC) was used to do a proteome comparison of our sequences.

## Installation

Install [pip](https://pip.pypa.io/en/stable/) with sudo apt.

```bash
sudo apt install python3-pip
```

Next, use the package manager [pip](https://pip.pypa.io/en/stable/) to install [Biopython](http://biopython.org/DIST/docs/tutorial/Tutorial.html).

```bash
sudo pip3 install biopython
```

Check if the package is installed.

```bash
sudo python3 -m pip show biopython
```

# Scripts
## transfer_gb.py

This python script was created to transfer/download the genbank (.gb) files from NCBI's database. After the extraction it'll change the extension of the file to ".gbk" because GIPSy didn't go well with the ".gb".

Along side with the creation of folders so that while executing the home directory doesn't get to messi. 

SIUUU

## phaster.py

Here is were we use Phaster's online API to get the results (zip) to see if there are any phage regions in the strains genome.

## unzip.py

This one it's basically as the file name says, it's going to unzip the results that came from phaster.py and move the respective files to a specific folder.

## GIPSy

You can get the program and its dependecies [here](https://www.bioinformatics.org/download/gipsy/).

After downloading it you can run it (required java installed).

You'll need to have a query genome and a subject genome, which this last one is going to be your reference sequence and the query one its going to be the other ones that you want to analyse.

## Phaster

You can use their web site [here](https://phaster.ca/) if you want to.

There are various possibilities to make this analysis in Phaster. You can give the accession number, the genome sequence or its file.

## Patric Database / BV-BRC

Here we did a functional comparison between strains to analyse some parts of the genome of some sequences and see why some have less similarity than others.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Support

Instituto Politécnico de Setúbal - Bioinformatics Degree

Teachers Francisco Martins Pina e Alberto Júnior. 

## Authors

Alexandre Duarte

Diogo Cabrita

Guilherme Sá
