# This code sample uses the 'requests' library:
# http://docs.python-requests.org
from abc import ABC, abstractmethod

class Ingredient(ABC):
    '''
    Interface for Ingredient. Represents the abstraction an Ingredient
    '''

    def __init__(self, name : str, category: str):

        '''
        Initiates a Ingredient Object
        Args:
            name: name of the ingredient
            category: category of the ingredient
        '''

        self.name = name
        self.category = category
     
    @abstractmethod
    def name(self):
        '''
        Definiton of the name method
        '''
        pass
    
    @abstractmethod
    def category(self):
        '''
        Definiton of the category method
        '''
        pass

 


class NaturalIngredient(Ingredient):

    '''
        Creates a Natural Ingredient object
    '''

    def __init__ (self, name:str, category: str):
        
        '''
        Initiates a Natural Ingredient object
        
        Args:
            name: name of the ingredient
            category: category of the ingredient
        '''
        
        super(NaturalIngredient,self).__init__(name,category) #uses the constructor of the interface
    
    def name(self):
        """
        This function returns the name of the natural ingredient. 
    
        Returns:
            name : string
        """
        return self.name
    
    def category(self):
        """
        This function returns the category of the natural ingredient. 
    
        Returns:
            category : string
        """
        return self.category

    

class ArtificialIngredient(Ingredient):

    '''
        Creates an Artificial Ingredient object
    '''
        
    def __init__ (self, name:str, category: str):
        '''
        Initiates an Artificial Ingredient object
        
        Args:
            name: name of the ingredient
            category: category of the ingredient
        '''
        super(ArtificialIngredient,self).__init__(name, category) #uses the constructor of the interface
    
    def name(self):
        """
        This function returns the name of the natural ingredient. 
    
        Returns:
            name : string
        """
        return self.name   
    
    def category(self):
        """
        This function returns the category of the artifical ingredient. 
    
        Returns:
            category : string
        """
        return self.category 


class UnknowIngredient(Ingredient):

    '''
        Creates an Artificial Ingredient object
    '''
        
    def __init__ (self, name:str, category: str):
        '''
        Initiates an Artificial Ingredient object
        
        Args:
            name: name of the ingredient
            category: category of the ingredient
        '''
        super(ArtificialIngredient,self).__init__(name, category) #uses the constructor of the interface
    
    def name(self):
        """
        This function returns the name of the natural ingredient. 
    
        Returns:
            name : string
        """
        return self.name   
    
    def category(self):
        """
        This function returns the category of the artifical ingredient. 
    
        Returns:
            category : string
        """
        return self.category 


    