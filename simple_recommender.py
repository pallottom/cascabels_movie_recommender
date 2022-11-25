import random
import pandas as pd
import pickle
import sklearn

model = pickle.load(open("my_nmf_model.sav", "rb"))

films = ["Burnt by the Sun", 
	"Pulp Fiction", 
	"Star Trek", 
	"Ghostbusters", 
	"Day after tomorrow", 
	"Lion King", "King Richard"]

def recommend(user_input_from_app):
	random.shuffle(films)   ## Using nmf_mode together with user_input_dict to give recommendations to user.
	return films[:3]


def recommend_nmf(user_input_from_app, model="my_nmf_model.sav", k=10):    
    """Filters and recommends the top k movies for any given input query based on a trained NMF model.
    Parameters
    ----------
    query : dict
        A dictionary of movies already seen. Takes the form {"movie_A": 3, "movie_B": 3} etc
    model : pickle pickle model read from disk
    k : int, optional no. of top movies to recommend, by default 10
    """
    # 1. candiate generation
    new_user_list=[]
    for i in range(len(films)):
        new_user_list.append(random.randint(0,5))
    new_user_list = [new_user_list]
    new_user_pd = pd.DataFrame(new_user_list, columns=films)
    P_new_user = model.transform(new_user_pd)
    # construct a user vector
    
   
    # 2. scoring
    
    # calculate the score with the NMF model
    
    
    # 3. ranking
    
    # set zero score to movies allready seen by the user
    
    # return the top-k highst rated movie ids or titles
    
    return 