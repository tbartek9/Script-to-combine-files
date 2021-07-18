# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:59:12 2021

@author: Bartosz Terka
"""
"""
This script combines files with the same extension.
1)put the script in the folder together with the folder containing the files
2)complete the names of folder and file in lines 13,14 and 17
"""
import os
name=open('name.txt','a') #in place of name.xx enter the name and file extension which will be created 
folders=os.listdir('folder') #in place of folder enter the name of folder that contains the files to combine
licznik=len(folders)
os.chdir('folder') #in place of folder enter the name of folder that contains the files to combine
i=0
while(i<licznik):
    plik=open(folders[i],'r')
    name.write(plik.read())
    i+=1
    