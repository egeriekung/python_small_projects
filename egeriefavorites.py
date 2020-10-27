#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:05:15 2020

@author: apple
"""

egerie_favorites = {'toys':['lol doll','baby doll'],
                    'food':['banana','jelly','apple'],
                    'books':['matilda','the blue duck'],
                    'people':['everyone'],
                    'activities':['coding','play with brothers']}

for key in egerie_favorites.keys():
    for item in egerie_favorites[key]:
        print('Egerie favorite {} is {}'.format(key,item))

for item in egerie_favorites['books']:
    print(item)

answer = ''
answer = input('Name one of egerie favorites: ')

for key in egerie_favorites.keys():
    for item in egerie_favorites[key]:
        if answer in egerie_favorites[key]:
            print('you got it!')
            break