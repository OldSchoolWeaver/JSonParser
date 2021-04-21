# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import json

def loadJson(file: str):

    """
    This function receives a string with the JSon File location and loads 
    the file into a list
    
    Args:
        file_name: file source name
    """

    try:
        f = open(file,) #open json file 
        ingredient_dic = json.load(f)
        return ingredient_dic

    except Exception as e:
        print('Error Loading Json file: ' , e)
        sys.exit(1)    

