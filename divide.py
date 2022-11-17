import json 
import re
from random import *
trainQuestion =[]
def divideAT(file ,evalDest, trainDest):
    trainQuestion =[]
    with open(file ,"r", encoding="utf8") as rf:
        questions = json.load(rf);
        taille = len(questions)
        cpt =len(questions)
        print('la premiere taille du tableau de question est :'+ str(len(questions)))
        for i in range(0,100711):
            matched =0
            n = randint(0,50711);
            for question in questions:
                if int(question['id']) == n:
                    matched = 1
                    cpt-=1
                    trainQuestion.append(question)
                    questions.remove(question)
                    print("le compteur est:" + str(cpt))
                    break
            if cpt==(taille*0.2):
                print('cpt a atteind le seuil')
                break
        print('le nombre de question d\'evaluation retenu est  :'+ str(len(questions))+ '\n')
        with open(evalDest,'w+', encoding='utf-8') as eval :
            eval.write('[\n')
            for quest in questions:
                quest['question'] = re.sub('\"',"",quest['question'])
                eval.write('{\n'+ '\t"id":' + str(quest['id'])+ ',\n' +'\t"question":'+ '"'+str(quest['question'])+'"' +'\n' + '},\n')
            eval.write('\n]\n')
        print('le nombre de question de train retenu est  :'+ str(len(trainQuestion))+ '\n')
        print("le nombre de question est :" + str(taille))
        with open(trainDest,'w+', encoding='utf-8') as train :
            train.write('[\n')
            for quest in trainQuestion:
                quest['question'] = re.sub('\"|',"",quest['question'])
                train.write('{\n'+ '\t"id":' + str(quest['id'])+ ',\n' +'\t"question":'+ '"'+str(quest['question'])+'"' +',\n' + '\t"category":' + '"'+str(quest['category'])+ '"' ',\n' + '\t"type":' + str(quest['type'])+ '\n'  '},\n')
            train.write('\n]\n')
    return trainQuestion
#divideAT("AT_answer_type_prediction/wikidata/SMART2022-AT-wikidata-train.json", "AT/wikidata/wikidata-evaluation.json" , "AT/wikidata/wikidata-train.json")

def divideRL(file ,evalDest, trainDest):
    trainQuestion =[]
    with open(file ,"r", encoding="utf8") as rf:
        questions = json.load(rf);
        taille = len(questions)
        cpt =len(questions)
        print('la premiere taille du tableau de question est :'+ str(len(questions)))
        for i in range(0,(taille)*8):
            matched =0
            n = randint(0,20000);
            for question in questions:
                if str(n) in question['id']:
                    matched = 1
                    cpt-=1
                    trainQuestion.append(question)
                    questions.remove(question)
                    print("le compteur est:" + str(cpt))
                    break
            if cpt==(taille*0.2):
                print('cpt a atteind le seuil')
                break
        print('le nombre de question d\'evaluation retenu est  :'+ str(len(questions))+ '\n')
        with open(evalDest,'w+', encoding='utf-8') as eval :
            eval.write('[\n')
            for quest in questions:
                quest['question'] = re.sub('\"',"",quest['question'])
                eval.write('{\n'+ '\t"id":' + '"'+str(quest['id'])+'"'+ ',\n' +'\t"question":'+ '"'+str(quest['question'])+'"' +'\n' + '},\n')
            eval.write('\n]\n')
        print('le nombre de question de train retenu est  :'+ str(len(trainQuestion))+ '\n')
        print("le nombre de question est :" + str(taille))
        with open(trainDest,'w+', encoding='utf-8') as train :
            train.write('[\n')
            for quest in trainQuestion:
                quest['question'] = re.sub('\"|',"",quest['question'])
                train.write('{\n'+ '\t"id":' + '"'+str(quest['id'])+'"'+ ',\n' +'\t"question":'+ '"'+str(quest['question'])+'"' +',\n'+ '\t"relations":' + str(quest['relations'])+ ',\n'+ '\t"num_of_rels":' + str(quest['num_of_rels'])+ '\n' + '},\n')
            train.write('\n]\n')
#divideRL("RL_relation_linking\dbpedia\SMART2022-RL-dbpedia-train.json", "RL/dbpedia/dbpedia-evaluation.json" , "AT/dbpedia/dbpedia-train.json")

            

def model(file):
    tabQuestion =[] ;
    questions = []
    nbrMatchedQuestion = 0
    with open(file ,"r", encoding="utf8") as rf:
        questions = json.load(rf);

    Model = [[0 for i in range(4)] for j in range(16)]
    #Remplissage des entetes de la Matrice Model
    Model[0][0]= 'Question / Answer Type'
    Model[0][1]= 'Ressource'
    Model[0][2]= 'Literal'
    Model[0][3]= 'Boolean'

    #Remplissage de la premiere colone avec les questions Wh-terms
    Model[1][0]= 'Who'
    Model[2][0]= 'What'
    Model[3][0]= 'When'
    Model[4][0]= 'Where'
    Model[5][0]= 'Which'
    Model[6][0]= 'Whom'
    Model[7][0]= 'Whose'
    Model[8][0]= 'Why'
    Model[9][0]= 'Of which'
    Model[10][0]= 'Is'
    Model[11][0]= 'How Many'
    Model[12][0]= 'Does'
    Model[13][0]= 'Name'
    Model[14][0]= 'Did'
    Model[15][0]= 'At What'

    # Declaration du model probabiliste

    ModelProbailiste = [[0 for i in range(4)] for j in range(16)]
    #Remplissage des entetes de la Matrice ModelProbailiste
    ModelProbailiste[0][0]= 'Question / Answer Type'
    ModelProbailiste[0][1]= 'Ressource'
    ModelProbailiste[0][2]= 'Literal'
    ModelProbailiste[0][3]= 'Boolean'

    #Remplissage de la premiere colone avec les questions Wh-terms
    ModelProbailiste[1][0]= 'Who'
    ModelProbailiste[2][0]= 'What'
    ModelProbailiste[3][0]= 'When'
    ModelProbailiste[4][0]= 'Where'
    ModelProbailiste[5][0]= 'Which'
    ModelProbailiste[6][0]= 'Whom'
    ModelProbailiste[7][0]= 'Whose'
    ModelProbailiste[8][0]= 'Why'
    ModelProbailiste[9][0]= 'Of which'
    ModelProbailiste[10][0]= 'Is'
    ModelProbailiste[11][0]= 'How Many'
    ModelProbailiste[12][0]= 'Does'
    ModelProbailiste[13][0]= 'Name'
    ModelProbailiste[14][0]= 'Did'
    ModelProbailiste[15][0]= 'At What'
# creation des differentes Regex
    whoReg = re.compile('^Who' , re.IGNORECASE)
    whatReg = re.compile('^What' , re.IGNORECASE)
    whenReg = re.compile('^When' , re.IGNORECASE)
    whereReg = re.compile('^Where' , re.IGNORECASE)
    whichReg = re.compile('^Which' , re.IGNORECASE)
    whomReg = re.compile('Whom' , re.IGNORECASE)
    whoseReg = re.compile('^Whose' , re.IGNORECASE)
    whyReg = re.compile('^Why' , re.IGNORECASE)
    ofWhichReg = re.compile('^of which' , re.IGNORECASE)
    isReg = re.compile('^is' , re.IGNORECASE)
    howManyReg = re.compile('how many' , re.IGNORECASE)
    doesReg = re.compile('^does' , re.IGNORECASE)
    nameReg = re.compile('name' , re.IGNORECASE)
    didReg = re.compile('did' , re.IGNORECASE)
    atWhatReg = re.compile('^At what' , re.IGNORECASE)
    #creattion des compteurs de variable pour who
    cptWhoRessource =0
    cptWhoLitteral =0
    cptWhoBoolean =0 
    #creattion des comteurs de variable pour what
    cptWhatRessource =0
    cptWhatLitteral =0
    cptWhatBoolean =0
    #creattion des comteurs de variable pour when
    cptWhenRessource =0
    cptWhenLitteral =0
    cptWhenBoolean =0
    #creattion des comteurs de variable pour where
    cptWhereRessource =0
    cptWhereLitteral =0
    cptWhereBoolean =0 
    #creattion des comteurs de variable pour which
    cptWhichRessource =0
    cptWhichLitteral =0
    cptWhichBoolean =0
    #creattion des comteurs de variable pour whom
    cptWhomRessource =0
    cptWhomLitteral =0
    cptWhomBoolean =0
    #creattion des comteurs de variable pour whose
    cptWhoseRessource =0
    cptWhoseLitteral =0
    cptWhoseBoolean =0
    #creattion des comteurs de variable pour ofWich
    cptOfWhichRessource =0
    cptOfWhichLitteral =0
    cptOfWhichBoolean =0
    #creattion des comteurs de variable pour is
    cptIsRessource =0
    cptIsLitteral =0
    cptIsBoolean =0
    #creattion des comteurs de variable pour why
    cptWhyRessource =0
    cptWhyLitteral =0
    cptWhyBoolean =0
    #creattion des comteurs de variable pour HowMany
    cptHowManyRessource =0
    cptHowManyLitteral =0
    cptHowManyBoolean =0
    #creattion des comteurs de variable pour doesReg
    cptDoesRessource =0
    cptDoesLitteral =0
    cptDoesBoolean =0
    #creattion des comteurs de variable pour name
    cptNameRessource =0
    cptNameLitteral =0
    cptNameBoolean =0
    #creattion des comteurs de variable pour did
    cptDidRessource =0
    cptDidLitteral =0
    cptDidBoolean =0
    #creattion des comteurs de variable pour At What
    cptAtWhatRessource =0
    cptAtWhatLitteral =0
    cptAtWhatBoolean =0
    #compteur totaux 
    #compteur du who 
    cptWho =0
    cptWhat =0
    cptWhere =0
    cptWhen =0
    cptWhich =0
    cptWhom =0
    cptWhose =0
    cptWhy =0
    cptWhat =0
    cptOfWhich =0
    cptIs =0
    cptHowMany =0
    cptDoes =0
    cptName =0
    cptDid =0
    cptAtWhat =0
    #Debut du maching
    for question in  questions:
        #test du matching avec Who 
        if whoReg.match(question['question']):
            cptWho+=1 
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                cptWhoRessource +=1
                Model[1][1]=cptWhoRessource

                
            elif question['category']=='boolean' :
                cptWhoBoolean +=1
                Model[1][3]=cptWhoBoolean
                
            else:
                cptWhoLitteral+=1
                Model[1][2]=cptWhoLitteral
                
        #test du matching avec What    
        if  whatReg.match(question['question']):
            cptWhat+=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptWhatRessource +=1
                    Model[2][1]=cptWhatRessource
                    
            elif question['category']=='boolean' :
                cptWhatBoolean +=1
                Model[2][3]=cptWhatBoolean

            else:
                cptWhatLitteral+=1
                Model[2][2]=cptWhatLitteral
                
        # test du matching avec When       
        if whenReg.match(question['question']):
            cptWhen+=1 
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                cptWhenRessource +=1
                Model[3][1]=cptWhenRessource
                
            elif question['category']=='boolean' :
                cptWhenBoolean +=1
                Model[3][3]=cptWhenBoolean
                
            else:
                cptWhenLitteral+=1
                Model[3][2]=cptWhenLitteral
                
        #test du matching avec Where    
        if  whereReg.match(question['question']):
            cptWhere+=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptWhereRessource +=1
                    Model[4][1]=cptWhereRessource
                    
            elif question['category']=='boolean' :
                cptWhereBoolean +=1
                Model[4][3]=cptWhereBoolean
                
            else:
                cptWhereLitteral+=1
                Model[4][2]=cptWhereLitteral
                
        # test du matching avec Which       
        if whichReg.match(question['question']):
            cptWhich+=1 
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                cptWhichRessource +=1
                Model[5][1]=cptWhichRessource
                
            elif question['category']=='boolean' :
                cptWhichBoolean +=1
                Model[5][3]=cptWhichBoolean
                
            else:
                cptWhichLitteral+=1
                Model[5][2]=cptWhichLitteral
                
        #test du matching avec Whom,    
        if  whomReg.match(question['question']):
            cptWhom+=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptWhomRessource +=1
                    Model[6][1]=cptWhomRessource
                    
            elif question['category']=='boolean' :
                cptWhomBoolean +=1
                Model[6][3]=cptWhomBoolean
                
            else:
                cptWhomLitteral+=1 
                Model[6][2]=cptWhomLitteral
                
        # test du matching avec Whose       
        if whoseReg.match(question['question']):
            cptWhose+=1 
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                cptWhoseRessource +=1
                Model[7][1]=cptWhoseRessource
                
            elif question['category']=='boolean' :
                cptWhoseBoolean +=1
                Model[7][3]=cptWhoseBoolean
                
            else:
                cptWhoseLitteral+=1
                Model[7][2]=cptWhoseLitteral
                
        #test du matching avec Why    
        if  whyReg.match(question['question']):
            cptWhy +=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptWhyRessource +=1
                    Model[8][1]=cptWhyRessource
                    
            elif question['category']=='boolean' :
                cptWhyBoolean +=1
                Model[8][3]=cptWhyBoolean
                
            else:
                cptWhyLitteral+=1
                Model[8][2]=cptWhyLitteral
                
        #test du matching avec Of Which    
        if  ofWhichReg.match(question['question']):
            cptOfWhich +=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptOfWhichRessource +=1
                    Model[9][1]=cptOfWhichRessource
                    
            elif question['category']=='boolean' :
                cptOfWhichBoolean +=1
                Model[9][1]=cptOfWhichLitteral
                
            else:
                cptOfWhichLitteral+=1
                Model[9][2]=cptOfWhichLitteral
                
        #test du matching avec Is    
        if  isReg.match(question['question']):
            cptIs +=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptIsRessource +=1
                    Model[10][1]=cptIsRessource
                    
            elif question['category']=='boolean' :
                cptIsBoolean +=1
                Model[10][3]=cptIsBoolean
                
            else:
                cptIsLitteral+=1
                Model[10][2]=cptIsLitteral
                
        #test du matching avec How Many    
        if  howManyReg.match(question['question']):
            cptHowMany +=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptHowManyRessource +=1
                    Model[11][1]=cptHowManyRessource
                    
            elif question['category']=='boolean' :
                cptHowManyBoolean +=1
                Model[11][3]=cptHowManyBoolean
                
            else:
                cptHowManyLitteral+=1
                Model[11][2]=cptHowManyLitteral
                
        #test du matching avec Does    
        if  doesReg.match(question['question']):
            cptDoes +=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptDoesRessource +=1
                    Model[12][1]=cptDoesRessource
                    
            elif question['category']=='boolean' :
                cptDoesBoolean +=1
                Model[12][3]=cptDoesBoolean
                
            else:
                cptDoesLitteral+=1
                Model[12][2]=cptDoesLitteral
                
        #test du matching avec Name    
        if  nameReg.match(question['question']):
            cptName +=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptNameRessource +=1
                    Model[13][1]=cptNameRessource
                    
            elif question['category']=='boolean' :
                cptNameBoolean +=1
                Model[13][3]=cptNameBoolean
                
            else:
                cptNameLitteral+=1
                Model[13][2]=cptNameLitteral
                
        #test du matching avec Did    
        if  didReg.match(question['question']):
            cptDid +=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptDidRessource +=1
                    Model[14][1]=cptDidRessource
                    
            elif question['category']=='boolean' :
                cptDidBoolean +=1
                Model[14][3]=cptDidBoolean
                
            else:
                cptDidLitteral+=1
                Model[14][2]=cptDidLitteral
                
        #test du matching avec At what    
        if  atWhatReg.match(question['question']):
            cptAtWhat +=1
            nbrMatchedQuestion += 1
            if question['category']=='resource':
                    cptAtWhatRessource +=1
                    Model[15][1]=cptAtWhatRessource               
            elif question['category']=='boolean' :
                cptAtWhatBoolean +=1
                Model[14][3]=cptAtWhatBoolean           
            else:
                cptAtWhatLitteral+=1
                Model[15][2]=cptAtWhatRessource
    #Who
    if cptWho!=0:
        ModelProbailiste[1][3]=cptWhoBoolean/cptWho            
        ModelProbailiste[1][3]=cptWhoBoolean/cptWho
        ModelProbailiste[1][1]=cptWhoRessource/cptWho
    #What
    if cptWhat!=0:
        ModelProbailiste[2][1]=cptWhatRessource/cptWhat            
        ModelProbailiste[2][3]=cptWhatBoolean/cptWhat            
        ModelProbailiste[2][2]=cptWhatLitteral/cptWhat
    #When
    if cptWhen!=0:
        ModelProbailiste[3][1]=cptWhenRessource/cptWhen
        ModelProbailiste[3][3]=cptWhenBoolean/cptWhen            
        ModelProbailiste[3][2]=cptWhenLitteral/cptWhen
    #Where
    if cptWhere!=0:
        ModelProbailiste[4][1]=cptWhereRessource/cptWhere            
        ModelProbailiste[4][3]=cptWhereBoolean/cptWhere
        ModelProbailiste[4][2]=cptWhereLitteral/cptWhere
    #which
    if cptWhich!=0:
        ModelProbailiste[5][1]=cptWhichRessource/cptWhich            
        ModelProbailiste[5][3]=cptWhichBoolean/cptWhich            
        ModelProbailiste[5][2]=cptWhichLitteral/cptWhich
    #Whom
    if cptWhom!=0:
        ModelProbailiste[6][1]=cptWhomRessource/cptWhom
        ModelProbailiste[6][3]=cptWhomBoolean/cptWhom
        ModelProbailiste[6][2]=cptWhomLitteral/cptWhom
    #Whose
    if cptWhose!=0:
        ModelProbailiste[7][1]=cptWhoseRessource/cptWhose            
        ModelProbailiste[7][3]=cptWhoseBoolean/cptWhose
        ModelProbailiste[7][2]=cptWhoseLitteral/cptWhose            
    #Why
    if cptWhy!=0:
        ModelProbailiste[8][1]=cptWhyRessource/cptWhy
        ModelProbailiste[8][3]=cptWhyBoolean/cptWhy
        ModelProbailiste[8][2]=cptWhyLitteral/cptWhy
    #Of Which
    if cptOfWhich!=0:
        ModelProbailiste[9][1]=cptOfWhichRessource/cptOfWhich
        ModelProbailiste[9][2]=cptOfWhichLitteral/cptOfWhich
        ModelProbailiste[9][1]=cptOfWhichLitteral/cptOfWhich            
    #Is
    if cptIs!=0:            
        ModelProbailiste[10][1]=cptIsRessource/cptIs
        ModelProbailiste[10][3]=cptIsBoolean/cptIs
        ModelProbailiste[10][2]=cptIsLitteral/cptIs
    #How Many
    if cptHowMany!=0:
        ModelProbailiste[11][1]=cptHowManyRessource/cptHowMany
        ModelProbailiste[11][3]=cptHowManyBoolean/cptHowMany
        ModelProbailiste[11][2]=cptHowManyLitteral / cptHowMany
    #Does
    if cptDoes!=0:
        ModelProbailiste[12][1]=cptDoesRessource/cptDoes
        ModelProbailiste[12][3]=cptDoesBoolean/cptDoes
        ModelProbailiste[12][2]=cptDoesLitteral/cptDoes
    #Name
    if cptName!=0:
        ModelProbailiste[13][1]=cptNameRessource/cptName
        ModelProbailiste[13][3]=cptNameBoolean/cptName
        ModelProbailiste[13][2]=cptNameLitteral/cptName
    #DId
    if cptDid!=0:
        ModelProbailiste[14][1]=cptDidRessource/cptDid
        ModelProbailiste[14][3]=cptDidBoolean/cptDid
        ModelProbailiste[14][2]=cptDidLitteral/cptDid
    #At what
    if cptAtWhat!=0:
        ModelProbailiste[15][1]=cptAtWhatRessource/cptAtWhat
        ModelProbailiste[15][3]=cptAtWhatBoolean/cptAtWhat
        ModelProbailiste[15][2]=cptAtWhatLitteral/cptAtWhat      
    print('\n preparation a l\'affichage du model \n')
    print(Model)
    print('\n preparation a l\'affichage du model probabiliste \n')
    print(ModelProbailiste)
    print('le nombre de question avec what est: '+str(cptWhat) + '\n')
    print('le nombre de question avec who est: '+str(cptWho) + '\n')
    print('le nombre de question avec when est: '+str(cptWhen) + '\n')
    print('le nombre de question avec where est: '+str(cptWhere) + '\n')
    print('le nombre de question avec which est: '+str(cptWhich) + '\n')
    print('le nombre de question avec whom est: '+str(cptWhom) + '\n')
    print('le nombre de question avec whose est: '+str(cptWhose) + '\n')
    print('le nombre de question avec why est: '+str(cptWhy) + '\n')
    print('le nombre de question avec Of Which est: '+str(cptOfWhich) + '\n')
    print('le nombre de question avec Is est: '+str(cptIs) + '\n')
    print('le nombre de question avec How Many est: '+str(cptHowMany) + '\n')
    print('le nombre de question avec Does est: '+str(cptDoes) + '\n')
    print('le nombre de question avec Name est: '+str(cptName) + '\n')
    print('le nombre de question avec Did est: '+str(cptDid) + '\n')
    print('le nombre de question avec At what est: '+str(cptAtWhat) + '\n')
    print('le nombre de question matcher avec notre model est: '+str(nbrMatchedQuestion) + '\n')
    print('le nombre de question total est: '+str(len(questions)) + '\n')

    with open("model.csv", "w+") as model:
        for ligne in Model:
            for item in ligne:
                model.write("\t")
                model.write(str(item))
            model.write('\n')
    with open("modelProbabiliste.csv", "w+") as modelProbabiliste:
        for ligne in ModelProbailiste:
            for item in ligne:
                modelProbabiliste.write("\t")
                modelProbabiliste.write(str(item))
            modelProbabiliste.write('\n')
    return ModelProbailiste

#model("AT_answer_type_prediction/wikidata/SMART2022-AT-wikidata-train.json")

    






        

    
   
       
    
 

        
                