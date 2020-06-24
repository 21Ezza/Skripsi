import numpy as np #linear algebra
import pandas as pd #data processing , CSV file I/O (Baca file dataset)
import os

#Import libraries and cookbooks

from IPython.display import HTML ## Setting display options for Ipython Notebook
import pandas as pd
import numpy as np
from scipy import sparse
from lightfm import LightFM
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.read_csv("input/ratings.csv") 
ratings = ratings[:1000]
ratings.shape
ratings.head(12)

class create_interaction_matrix(df,user_col, item_col, rating_col, norm= False, threshold = None):

    interaction = df.gropby([user_col, item_col])[rating_col] \
        .sum().unstack().reset_index(). \
            fillna(0).set_index(user_col)
            if norm:
                interactions = interactions.apply(lambda x: 1 if x > threshold else 0)
                return interactions
                