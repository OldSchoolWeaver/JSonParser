# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import logging
import os
import sys
import pandas as pd
import numpy as np
from datetime import date
import datetime
import json
from ingredient import NaturalIngredient, ArtificialIngredient, UnknowIngredient
from aux import loadJson

class Candy():
    '''
        Creates a Candy Object
    '''
    
    def __init__(self,name: str, price: float, list_of_ingredients: list):
        
        '''
        Initiates a Candy Object
        Args:
            name: name of the candy
            price: price of the ingredients
            list_of_ingredients: list of the ingredients
        '''
        self.name = name
        self.price=price
        self.list_of_ingredients=list_of_ingredients

    @staticmethod
    def listAllCandies(list_of_candies: list):
    
        """
            This function receives a list of of candies and performs a loop to iterate trough all of the candy objects 
            in the list and print their attributes.
            
            Args:
            list_of_candies : list with all the Candy Objects

        """    
        try: 
            print('\nThese are the candies available: \n')
            for candie in list_of_candies:
                print('Name: ', candie.name)
                print('Price: ',candie.price)
                print('\t List of Ingredients: ')
                for ingredient in candie.list_of_ingredients:
                    print('\t\t Name: ',ingredient.name)
                    print('\t\t Category: ',ingredient.category)
            
            #Script was excuted successfully 
            sys.exit(0)

        except Exception as e:
            #Script failed 
            print('Error running function List All Candies ' , e)
            sys.exit(1)    

    @staticmethod
    def parseIngredientType(ingredient: dict):
        '''
                Function responsible for categorization of the ingredients.
                Argrs: 
                    ingredient: Json object with ingredients elements
                Return:
                    Ingredient object
        '''
        
        category = ingredient['category']
                    
        if category == "artifical":
            return ArtificialIngredient(ingredient['name'], ingredient['category'])
        elif category == "natural": 
            return NaturalIngredient(ingredient['name'], ingredient['category'])
        else:
            return UnknowIngredient(ingredient['name'],'Unknown')


    @staticmethod
    def createsCandyList(json_list_of_candies: list):

        """
            This function receives a json list of ingredients. It iterates trough the list creating the Candy Object 
            with the correspondent Ingredients segregating them into Natural or Artificial.

            Args:
            json_list_of_ingredients : json list with the all the cadies and the correpondent nested attributes

            Returns:
            list_of_candies : a list with all the candy objects

        """    

        list_of_ingredients = [] #Initiates list
        list_of_candies = [] #Initiates list
        
        try:

            for candy in json_list_of_candies:
              
                for aux in candy['ingredients']:
                    list_of_ingredients.append(Candy.parseIngredientType(aux))

                new_candy = Candy(candy['name'],candy['price'],list_of_ingredients)
                list_of_candies.append(new_candy)
                
                list_of_ingredients = [] #Resets the list

            return list_of_candies

        except Exception as e:
            print('Error running the function createsCandyList: ' , e)
            sys.exit(1)    

