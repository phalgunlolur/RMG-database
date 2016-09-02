from rmgpy.rmg.model import Species
from rmgpy import settings
from rmgpy.data.kinetics.library import KineticsLibrary

from rmgpy.data.reference import *
import os.path
from rmgpy.kinetics.arrhenius import Arrhenius
from rmgpy.quantity import ScalarQuantity
from rmgpy.data.base import Entry
from rmgpy.reaction import Reaction
import re
import sys
import pandas as pd
import numpy as np
"""
The purpose of this script is to create a reaction library from the least amount of input.

Might eventually make it so it reads in a csv instead of hard-coding inputs below.

Currently the numbers below are all made up, so they should not be used by any means.

For the inputs, every variable that is a list has elements where the indexes correspond with entry in another list
For example, one complete data entry for Arrhenius parameters would be A[i], n[i], and Ea[i]
"""

#initalize library variables
libraryName = 'test'
library = KineticsLibrary()
library.name = libraryName
library.label =libraryName
library.shortDesc = "Library with made up rates"
library.longDesc = """
This library is a test created to showcase the createKineticsLibrary.py script
"""

#read data from csv
try:
    csv_file_name = sys.argv[1]
except:
    raise Exception('must input the path to a csv file for importing kinetics')
data = pd.read_csv(csv_file_name,
    dtype={'year':str,'pages':str,'volume':str,'journal':str,'article title':str,'Author list':str,'short description':str,'long description':str,'reactant 1 SMILES':str,'reactant 2 SMILES':str, 'product 1 SMILES':str, 'product 2 SMILES':str}, 
    skipinitialspace=True,
    na_values=['None','none','NA','Na'],
    names=[u'reactant 1 SMILES', u'reactant 2 SMILES',
       u'product 1 SMILES', u'product 2 SMILES',
       u'A', u'n', u'Ea',
       u'short description', u'long description',
       u'Author list', u'article title', u'journal',
       u'volume', u'pages', u'year'],
    header=0)

AunitsBimolecular = 'cm^3/(mol*s)'
AunitsUnimolecular = 's^-1'
EaUnits = 'kcal/mol'


#done with inputs
#################################################################################################################
#create entries in the library
speciesDict={}
for index in data.index:
    series = data.iloc[index]

    bimolecular = False
    #example item

    #make species
    r1 = Species().fromSMILES(series['reactant 1 SMILES'])
    p1 = Species().fromSMILES(series['product 1 SMILES'])
    r2 = None
    p2 = None
    if pd.notnull(series['reactant 2 SMILES']): 
        r2 = Species().fromSMILES(series['reactant 2 SMILES'])
    if pd.notnull(series['product 2 SMILES']): 
        p2 = Species().fromSMILES(series['product 2 SMILES'])

    #make species labels
    changeDict={} #necessary in case any species already exists in the speciesDict (isomorphic not same instance)
    for spec in [r1, r2, p1, p2]:
        if spec:
            for speciesLabel, existingSpecies in speciesDict.iteritems():
                if spec.isIsomorphic(existingSpecies):
                    changeDict[spec] = existingSpecies #species already in speciesDict
                    break
            else: #species is new
                changeDict[spec] = spec
                spec_formula = spec.molecule[0].getFormula()
                if spec_formula not in speciesDict:
                    spec.label = spec_formula
                else:
                    duplicateNumber = 2
                    while (spec_formula + '-{}'.format(duplicateNumber)) in speciesDict:
                        duplicateNumber += 1
                    spec.label = spec_formula + '-{}'.format(duplicateNumber)
                speciesDict[spec.label] = spec

    #Remake species accounting for duplicates
    r1 = changeDict[r1]
    p1 = changeDict[p1]
    if r2: r2 = changeDict[r2]
    if p2: p2 = changeDict[p2]

    #create reaction
    newReaction = None
    if r2:
        bimolecular = True
        if p2:
            newReaction = Reaction(reactants = [r1, r2], products = [p1, p2])
        else:
            newReaction = Reaction(reactants = [r1, r2], products = [p1])
    elif p2:
        newReaction = Reaction(reactants = [r1], products = [p1, p2])
    else:
        newReaction = Reaction(reactants = [r1], products = [p1])

    #set Arrhenius
    
    newArrhenius = Arrhenius()
    if bimolecular:
        Ainstance = ScalarQuantity(series['A'], AunitsBimolecular)
    else:
        Ainstance = ScalarQuantity(series['A'], AunitsUnimolecular)
    newArrhenius = Arrhenius(A = Ainstance,
                             n = ScalarQuantity(series['n'], ''),
                             Ea = ScalarQuantity(series['Ea'], EaUnits))

    #create reference item for library entry
    referenceType = None
    reference = None
    if pd.notnull(series['Author list']):
        #separate authors
        author_list = series['Author list'].split(';')
        #remove white space
        author_list = [re.sub('(\A\s|\s\Z)*','', author) for author in author_list]
        reference = Article(
            authors=author_list,
            title=series['article title'],
            journal=series['journal'],
            volume=series['volume'],
            pages=series['pages'],
            year=series['year'],)
        referenceType = re.sub('.*\.', '', str(reference.__class__))

    #convert descriptions from nan to ''
    if pd.notnull(series['short description']): shortDesc = series['short description']
    else: shortDesc = ''
    if pd.notnull(series['long description']): longDesc = series['long description']
    else: longDesc = ''
    #create library entry
    newEntry = Entry(index= index,
                     label=str(newReaction),
                     item=newReaction,
                     parent=None,
                     children=None,
                     data=newArrhenius,
                     reference=reference,
                     referenceType= referenceType,
                     shortDesc=shortDesc,
                     longDesc=longDesc,
                     rank=None,)

    #add to entry to library
    library.entries[index] = newEntry

library.save(os.path.join(settings['database.directory'],'kinetics/libraries/{0}/reactions.py'.format(libraryName)))
library.saveDictionary(os.path.join(settings['database.directory'],'kinetics/libraries/{0}/dictionary.txt'.format(libraryName)))
