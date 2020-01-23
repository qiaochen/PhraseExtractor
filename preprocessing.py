#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:35:37 2020

@author: chen
"""

import pandas as pd


RATING_PATH = "./data/ratings.csv"
FOOD_DICT_PATH = "./data/food_dict.txt"
STOPWORDS_PATH = "./data/stop_words.txt"


def read_data():
    df_ratings = pd.read_csv(RATING_PATH)
    
    with open(STOPWORDS_PATH, 'r') as in_file:
        stop_words = {w.strip() for w in in_file}
    
    with open(FOOD_DICT_PATH, 'r') as in_file:
        food_dict = set()
        for line in in_file:
            word, _ = line.strip().split(" ")
            food_dict.add(word)        
    
    return df_ratings.comment, stop_words, food_dict


            
    
    