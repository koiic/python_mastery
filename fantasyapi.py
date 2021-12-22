import requests 
import pandas as pd
import numpy as np



if __name__ == '__main__':
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    r = requests.get(url)

    json = r.json()
    
    element_df = pd.DataFrame(json['elements'])
    elements_types_df = pd.DataFrame(json['element_types'])
    teams_df = pd.DataFrame(json['teams'])
    
    print(element_df.head())
    

    print(json.keys())
    