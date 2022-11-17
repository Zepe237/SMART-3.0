from random import *
import json 
import re
from tkinter import W 
tab = [];
tabQuestion =[] ;
trouve = 0
cpt = 0
cpt2 =0

with open("SMART2022-AT-dbpedia-test.json" ,"r") as rf:
    questions = json.load(rf);
for i in range(0,50711):
    n = randint(0,50711);
    for j in range(0, len(tab)):
        if n == tab[j] :
            trouve = 1 ;
            print("ceci existe déja");
            break ;
    
    if trouve == 0:
        tab.append(n);
        cpt+=1;
        if cpt == 100 :
            break ;
print (cpt);

for m in range(0 , cpt):
    print (tab[m]);
    for question in questions :
        if  tab[m] == question['id']:
            print('\n')
            print("j ai trouver un elt")
            cpt2+=1
            print(question['id'])
            tabQuestion.append(question);
            break ;
print('\n')
print(len(questions))
print(len(tabQuestion))
print(len(tab))

with open('manual.txt','w+') as manual :
    for quest in tabQuestion:
        manual.write(str(quest['id'])+ '\t' + str(quest['question']))
        manual.write('\n')
    