import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

from sklearn.decomposition import NMF
import warnings
warnings.filterwarnings("ignore")   ## ignore NMF warnings

import random
import pickle

ratings= pd.read_csv('../file_name_ratings.csv', index_col="userId")  
model = pickle.load(open("my_nmf_model.sav", "rb"))
#user_films2 = {'71 (2014)' : 3,'Round Midnight (1986)' :2 , 'Salems Lot (2004)' :4}
films = list(ratings.columns)

#print(films)
#print(user_films2)

def recommend_nmf2(user_input_from_app, model="my_nmf_model.sav", k=10 ):    
    model = pickle.load(open("my_nmf_model.sav", "rb"))
    new_user_list=[]
    full_dict = {}
    for film in films:
        if film in user_input_from_app:
            full_dict[film] = [user_input_from_app[film]]
        else:
            full_dict[film] = [np.nan]
    new_user_pd = pd.DataFrame(full_dict)
    new_user_pd_copy = new_user_pd.copy()
    new_user_pd.fillna(0, inplace = True)
    P_new_user = model.transform(new_user_pd)
    Q = model.components_
    R_new_user = np.dot(P_new_user, Q)
    new_user_df = pd.DataFrame(R_new_user,index=['new_user'], columns=films)
    unrated_boolean = np.isnan(new_user_pd_copy).values[0]
    unrated_df = new_user_df.iloc[:, unrated_boolean]
    sorted_new_user_df = unrated_df.T.sort_values(by="new_user", ascending=False)
    recommandation = list(sorted_new_user_df.head(k).index)
    return recommandation