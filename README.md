# TeamVerify : A Team Analysis tool for Competitive Pokemon

TeamVerify is a Competitive Pokemon teambuilding companion tool based on automated reasoning. 

## Installation

TeamVerify is listed on the PyPI repository. Therefore, it is an easy install for anyone already running Python. Ensure you have a working distribution of Python 3.6 or higher then run the following command in a terminal window:
```
pip install teamverify
```
TeamVerify also needs to run a first-time setup script to populate its knowledge base. Once TeamVerify is installed simply run this command in a terminal window.
```
teamverify-fts
```
We also advise that you re-run this command whenever Smogon implements a major tier shift. TeamVerify's knowledge base only contains a subset of all Pokemon, so it may fall out-of-date as Pokemon shift into and out of OU.


## Usage
```
teamverify {txt/pokepaste} [outputfile]
```


### Old readme, slated for deletion

This repository contains all code for my automated pokemon teambuilder project. Descriptions of individual files will be added as new files are created. This automated Pokemon teambuilder is based on OWL ontologies for automated reasoning.

readTeamSyntax - contains the parseTeam function, which reads teams in the text format provided by Pokemon Showdown or PokePaste and returns it in dictionary form.

scrapePokedex - contains the scrollPage and scrapeDex functions, which use Selenium webdrivers to populate a competitivePokedex.csv file. This file contains several details key to deriving semantic concepts within competitive Pokemon teams.