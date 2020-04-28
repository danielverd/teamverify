from readTeamSyntax import parseTeam
import argparse
import os
import owlready2

def parseArgs():
    parser = argparse.ArgumentParser(description="Reads in Pokemon team from stdin.")
    parser.add_argument("team", help="txt file containing team")
    return parser.parse_args()

def getTeamString(team, html):
    """Returns a dictoinary containing the six Pokemon in the provided team.

    Keyword arguments:
    team -- the path to the Smogon official team string

    html -- true if the team is given as a webpage, false if given as text
    """
    if html:
        print('-- ERROR: HTML parsing not yet supported --')
        exit()
    else:
        with open(team,'r') as textfile:
            data = textfile.read()
    
    teamList = parseTeam(data)
    
    print(type(data))
    return teamList

def teamReasoner(teamList):
    onto = owlready2.get_ontology(os.getcwd()+'\\pokemon.owl').load()
    team = onto.Playstyles()

    #debugi = 0
    for pokemon in teamList:
        newPokemon = onto.Pokemon()
        newPokemon.hasSpecies = onto.Pokemon('spec'+pokemon['Species'])
        newPokemon.hasItem = onto.Items('it'+pokemon['Item'])

        newPokemon.hasHPEVs = pokemon['HPEVs']
        newPokemon.hasAtkEVs = pokemon['AtkEVs']
        newPokemon.hasDefEVs = pokemon['DefEVs']
        newPokemon.hasSpAEVs = pokemon['SpAEVs']
        newPokemon.hasSpDEVs = pokemon['SpDEVs']
        newPokemon.hasSpeEVs = pokemon['SpeEVs']

        newPokemon.hasMove.append(onto.Moves('mv'+pokemon['Move1']))
        newPokemon.hasMove.append(onto.Moves('mv'+pokemon['Move2']))
        newPokemon.hasMove.append(onto.Moves('mv'+pokemon['Move3']))
        newPokemon.hasMove.append(onto.Moves('mv'+pokemon['Move4']))
        print(newPokemon)
        team.hasPokemon.append(newPokemon)
        #debugi+=1
        #if debugi > 3:
        #    break

    print(team)
    onto.save(file='pokemonmeme3.owl',format='rdfxml')
    with onto:
        owlready2.sync_reasoner()


if __name__ == "__main__":
    args = parseArgs()

    if 'pokepast.es' in args.team:
        team = getTeamString(args.team,True)
    elif '.txt' in args.team:
        teamPath = os.getcwd()+'\\'+args.team
        team = getTeamString(args.team,False)
    else:
        print('-- ERROR: Unsupported input format --')
        exit()

    print(team)

    teamReasoner(team)