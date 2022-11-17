#%%
import json;
import re
from typing import Dict ;
import matplotlib.pyplot as plt

def numberOfQuestionsPerCatsgorie(file):
    cptResource= 0
    cptLiteral=0
    cptBoolean=0
    Dict = {'literal':0,'resource':0, 'boolean':0}
    with open(file , 'r', encoding='utf-8')as fs:
        questions = json.load(fs)
        for question in questions:
            if question['category'] == "resource":
                cptResource+=1 
            elif question['category']== "literal":
                cptLiteral+=1
            else:
                cptBoolean+=1
    Dict['literal']=cptLiteral
    Dict['resource']=cptResource
    Dict['boolean']=cptBoolean
    print('Resource : => {} Literal : => {} Booleen : => {}'.format(Dict['resource'],Dict['literal'],Dict['boolean']))
    return Dict
#smart-2022-datasets-main/smart-2022-datasets-main/EL_entity_linking/dbpedia/SMART2022-EL-dbpedia-test.jsonstat = numberOfQuestionsPerCatsgorie('smart-2022-datasets-main/smart-2022-datasets-main/AT_answer_type_prediction/wikidata/SMART2022-AT-wikidata-train.json')
def plot():
    stat = numberOfQuestionsPerCatsgorie('smart-2022-datasets-main/smart-2022-datasets-main/AT_answer_type_prediction/dbpedia/SMART2022-AT-dbpedia-train.json')
    keys = stat.keys()
    values = stat.values()
    color = ['Orange', 'LightBlue']
    plt.bar(keys , values, width=0.2)
    plt.title('Frequency of Appearance of Categories In Dbpedia train dataset')
    plt.xlabel('categories')
    plt.ylabel('number Of Question')
    plt.show()
    

#plot()

def countType(file):
    with open(file,'r',encoding='utf-8') as fs:

        questions = json.load(fs)
        listOfType = []
        dashboard = []
        frequentType = {}
        for question in questions:
            for typ in question['type']:
                if not(typ in listOfType):
                    listOfType.append(typ)
        for typ in listOfType:
            globals()['cpt'+typ]=0
        for question in questions:
            for typ in listOfType:
                if typ in question['type']:
                    
                    globals()['cpt'+typ]+=1
        for typ in listOfType:
            dashboard.append(globals()['cpt'+typ])
        
        frequentType = dict(zip(listOfType, dashboard))
        print(frequentType)
    return frequentType
#countType('smart-2022-datasets-main/smart-2022-datasets-main/AT_answer_type_prediction/dbpedia/SMART2022-AT-dbpedia-train.json')

def plotFrequentGanularType():
    stat = countType('smart-2022-datasets-main/smart-2022-datasets-main/AT_answer_type_prediction/dbpedia/SMART2022-AT-dbpedia-train.json')
    allValues = stat.values()
    values =[]
    keys =[]
    allKeys = stat.keys()
    for key in allKeys:
        #regler ici pour avoir les types qu on veut
        if stat[key]>300 and stat[key]<1000:
            keys.append(key)
            values.append(stat[key])

    color = ['LightSeaGreen', 'MediumAquamarine','LightSlateGray']
    plt.barh( keys ,values )
    plt.title('some less used  Dbpedia_2022 Type')
    plt.xlabel('number Of Question ')
    plt.ylabel('categories')
    plt.show() 
    
#plotFrequentGanularType() 

def getRedondantQuestions(file):
    with open(file,'r',encoding='utf-8') as fs:
        questions = json.load(fs)
        ListQuestion = []
        myset = set()
        cpt=0
        for question in questions:
            ListQuestion.append(question['question'])
            myset.add(question['question'])
            
        dupes = [x for n, x in enumerate(ListQuestion) if x in ListQuestion[:n]]
        myRedondentElements = set(dupes)
        ListOfVariable = []
        i=0
        for item in myRedondentElements:
            globals()['cpt_'+str(i)] = i
            ListOfVariable.append(globals()['cpt_'+str(i)])
            i+=1
        j=0
        listofKey =[]
        for question in myRedondentElements:
            globals()['cpt_'+str(j)]= dupes.count(question)
            listofKey.append(globals()['cpt_'+str(j)])
            j+=1
        RedondentElement = dict(zip(listofKey,myRedondentElements))
        #for i in range(len(listofKey)):
            #print(i)
            #print('>>>'+str(listofKey[i])+ ' : '+ str(RedondentElement[i])+'\n')
        print(RedondentElement)
  
getRedondantQuestions('smart-2022-datasets-main/smart-2022-datasets-main/AT_answer_type_prediction/dbpedia/SMART2022-AT-dbpedia-train.json')

