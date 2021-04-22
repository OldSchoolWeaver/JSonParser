# The JSON Parser Script

This script loads and reads a Json File and converts the elements of the file into a set of diferent objects. 

## Aplication

There are five python scripts in this application:

      Run - Script that initiates the simulation.To Initiate the Simulation run the Run.py script, 
            the output of the simulation will be the elements of the Json file printed in the console. 
            The script will exit with the success code of 0.
            
    
      JsonParser - Script responsible for loading the Json file, read it and convert it into the correpondent 
                   objects. 

      Ingredients - Script responsible for the Interface of the Ingrendient class. It also contains the
                    definition and implementation of the Natural Ingredient Class, Artificial Ingredient Class
                    and Unknown Ingredient Class.

      Aux - Script that has re-usable functions that are used across different scripts.                     

      UnitTest - Script to initiates 3 unit tests on the classes used on this script.  

The Json Parser produces an output like the one ilustrated below
                Name:  Candy X
                Price:  3.14
                        List of Ingredients: 
                                Name:  honey
                                Category:  natural
                                Name:  sugar
                                Category:  artifical

## Dependencies

The Json Parser application requires python3 to be installed and the following packages:

        Package         Version
        #--------------- -------
        numpy==1.20.2
        pandas==1.2.4
        pip==20.2.3
        python-dateutil==2.8.1
        pytz==2021.1
        setuptools==49.2.1
        six==1.15.0
        tabulate==0.8.9

## Run the application

There are 2 ways of running this application:

    1) Python 3:

        Ensure that Python3 is installed if the above dependencies are not installed just execute the following commands:
            pip3 install -r requirements.txt
        Run the the script:
            python3 Run.py

    2) Docker

        Ensure that you have docker installed. If you don't have docker, please check the following documentation (https://docs.docker.com/get-docker/)
        Run the following command:
            make all

