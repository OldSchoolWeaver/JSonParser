#!/usr/bin/env python3
# coding: utf-8
from JSonParser import Candy
from aux import loadJson

def RunSimulation():
    json_file='./Ingredients.json'
    list_of_candies = Candy.createsCandyList(loadJson(json_file))
    Candy.listAllCandies(list_of_candies)

if __name__ == '__main__':
    
    #Run Simulation
    RunSimulation()
    