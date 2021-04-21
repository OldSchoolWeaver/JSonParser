#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import numpy as np
import datetime as dt
from ingredient import ArtificialIngredient, NaturalIngredient


def test_ArtificialIngredient():
    """
        This test ensures that we can create an object of Artificial Ingredient
    """
    object_artificial_ingredient = ArtificialIngredient('test', 'artificial')    
    assert object_artificial_ingredient is not None

def test_NaturalIngredient():
    """
        This test ensures that we can create an object of Natural Ingredient
    """
    object_natural_ingredient = NaturalIngredient('test', 'natural')    
    assert object_natural_ingredient is not None 
