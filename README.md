# pokemon-teambuilder

This repository contains all code for my automated pokemon teambuilder project. Descriptions of individual files will be added as new files are created. This automated Pokemon teambuilder is based on OWL ontologies for automated reasoning.

readTeamSyntax - contains the parseTeam function, which reads teams in the text format provided by Pokemon Showdown or PokePaste and returns it in dictionary form.

scrapePokedex - contains the scrollPage and scrapeDex functions, which use Selenium webdrivers to populate a competitivePokedex.csv file. This file contains several details key to deriving semantic concepts within competitive Pokemon teams.