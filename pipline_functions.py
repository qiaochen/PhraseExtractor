#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:55:33 2020

@author: chen
"""
from collections import defaultdict

def frequent_phrase_detection(corpus, tau):
    """
    Statistics of single and multi-word phrases
    Input: 
        corpus - list of documents
        tau - support, min number of occurences
    Output:
        diction, key: phrase, value: frequncies    
    """
    freq_dict = {}
    index = defaultdict(lambda:set)
    
    # compute occuerences of indices
    for ith_doc, doc in enumerate(corpus):
        for ith_char, char in enumerate(doc):
            index[char].add((ith_doc, ith_char))
        
    # compute and at the meantime compose multi-word phrases
    while index:
        _index = defaultdict(lambda:set) # longer phrases
        for key in index.keys():
            if len(index[key]) >= tau:
                freq_dict[key] = len(index[key])
                for doc_id, w_id in index[key]:
                    if w_id + 1 == len(corpus[doc_id]): 
                        continue
                    longer_w = key + corpus[doc_id][w_id + 1]
                    _index[longer_w].add((doc_id, w_id + 1))
        index = _index
    return freq_dict
                
        
    
    
    