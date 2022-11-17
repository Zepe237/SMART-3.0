import json 
import re


def extract_words(str):
    Interrogate_words = ["which", "what", "whose", "when", "who", "whom", "where", "how", "why", "whether", "whatsoever", "whither", "whence", "whatever", "wherever"]
    for i in Interrogate_words:
        if i in str:
            return False
    return True

def test(file , fileResult):
    # creation des differentes Regex
    whoReg = re.compile('^Who ' , re.IGNORECASE)
    canReg = re.compile('^can ' , re.IGNORECASE)
    hasReg = re.compile('^has ' , re.IGNORECASE)
    correctReg = re.compile('(.)+correct' , re.IGNORECASE)
    isTrueReg = re.compile('(.)*is (.)+ true' , re.IGNORECASE)
    isToOrReg = re.compile('^is (.)+ to (.)+ or ' , re.IGNORECASE)
    wasToOrReg = re.compile('^was (.)+ to (.)+ or ' , re.IGNORECASE)
    isInReg = re.compile('^is+(.)+ in ' , re.IGNORECASE)
    isGreaterReg = re.compile('(.)*is+(.)+ greater(.)+' , re.IGNORECASE)
    compareReg = re.compile('(.)*(equal|less|greater|great|lesser) (.)+ to|than (.)+' , re.IGNORECASE)
    isLessReg = re.compile('(.)*is+(.)+ less(.)+' , re.IGNORECASE)
    isEqualReg = re.compile('(.)*is+(.)+ equal(.)+' , re.IGNORECASE)    
    doesGreaterReg = re.compile('(.)*(does|did|do|dies) (.)+ greater(.)+' , re.IGNORECASE)
    doesLessReg = re.compile('(.)*(does|did|do|dies) (.)+ less(.)+' , re.IGNORECASE)
    doesEqualReg = re.compile('(.)*(does|did|do|dies) (.)+ equal(.)+' , re.IGNORECASE)
    whatReg = re.compile('^What ' , re.IGNORECASE)
    whatReg = re.compile('^What ' , re.IGNORECASE)
    whatMethodReg = re.compile('^What method' , re.IGNORECASE)
    codeReg = re.compile('(.)*code*(.)' , re.IGNORECASE)
    whatAmountOfReg = re.compile('^What(.)+ amount of (.)+' , re.IGNORECASE)
    whatwasInDPReg = re.compile('^What(.)+(was|is)(.)+in(.)+:(.)+' , re.IGNORECASE)
    whatIsTheOfTheReg = re.compile('^What(.)+is(.)+the(.)+of(.)+,' , re.IGNORECASE)
    whatIsNumberReg = re.compile('^What is(.)+number(.)+,' , re.IGNORECASE)
    whatIsThePopulationReg = re.compile('^What is the +(.)*population ' , re.IGNORECASE)
    whatIsTheNumberOfReg = re.compile('^What is the number of' , re.IGNORECASE)    
    whatIsTheID = re.compile('^What(.)+is(.)+the(.)+ID' , re.IGNORECASE)      
    WhatIsIDReg = re.compile('^What is(.)* ID(.)+' , re.IGNORECASE)      
    whatIsQuantityOfReg = re.compile('^What(.)+quantity(.)+of ' , re.IGNORECASE)
    whenReg = re.compile('When' , re.IGNORECASE)
    whereReg = re.compile('^Where ' , re.IGNORECASE)
    whichReg = re.compile('^Which ' , re.IGNORECASE)
    whichIsReg = re.compile('^Which is' , re.IGNORECASE)
    whichIsTheMainReg = re.compile('^Which is the main' , re.IGNORECASE)
    whichMeanReg = re.compile('^Which means' , re.IGNORECASE)
    whomReg = re.compile('Whom' , re.IGNORECASE)
    whoseReg = re.compile('^Whose ' , re.IGNORECASE)
    whyReg = re.compile('^Why ' , re.IGNORECASE)
    ofWhichReg = re.compile('^of which' , re.IGNORECASE)
    isReg = re.compile('^is ' , re.IGNORECASE)
    howManyReg = re.compile('how many' , re.IGNORECASE)
    doesReg = re.compile('^does ' , re.IGNORECASE)
    nameReg = re.compile('name ' , re.IGNORECASE)
    dateReg = re.compile(' date ' , re.IGNORECASE)
    NameTheOf = re.compile('^name(.)+the (.)+' , re.IGNORECASE)
    withinReg = re.compile('Within ' , re.IGNORECASE)
    whateverReg = re.compile('whatever ' , re.IGNORECASE)
    didReg = re.compile('did ' , re.IGNORECASE)
    atWhatReg = re.compile('^At what ' , re.IGNORECASE)
    atWhatPositionReg = re.compile('(.)*what position ' , re.IGNORECASE)
    atWhatAgeReg = re.compile('^At what age ' , re.IGNORECASE)
    wasReg = re.compile('^was ' , re.IGNORECASE)
    wasInOrReg = re.compile('^was (.)+ in (.)+ or (.)+' , re.IGNORECASE)
    inWhatYearReg = re.compile('^In what year ' , re.IGNORECASE)
    inWhatReg = re.compile('^In what ' , re.IGNORECASE)
    inWhichReg = re.compile('^In which ' , re.IGNORECASE)
    inWhichYearReg = re.compile('^In which year ' , re.IGNORECASE)
    inWhichCountryReg = re.compile('^In which country ' , re.IGNORECASE)    
    inTheIsReg = re.compile('(.)*in (.)+ the (.)+ is (.)+' , re.IGNORECASE)
    inWhichCityReg = re.compile('^In which city ' , re.IGNORECASE)
    whichYearReg = re.compile('^which year ' , re.IGNORECASE)
    doReg = re.compile('^Do ' , re.IGNORECASE)
    fromWhatReg = re.compile('^from what ' , re.IGNORECASE)
    howDidReg = re.compile('^how did ' , re.IGNORECASE)
    theReg = re.compile('^the ' , re.IGNORECASE)
    theOfIsReg = re.compile('^the (.)+ of(.)+ is(.)+ ' , re.IGNORECASE)
    isOrReg = re.compile('^is (.)+ or ' , re.IGNORECASE)
    doesOrReg = re.compile('^does (.)+ or ' , re.IGNORECASE)
    didOrReg = re.compile('^did (.)+ or ' , re.IGNORECASE)
    wasOrReg = re.compile('^was (.)+ or ' , re.IGNORECASE)
    doOrReg = re.compile('^do (.)+ or ' , re.IGNORECASE)
    inHowManyReg = re.compile('(in|On)(.)+how(.)+many(.)+' , re.IGNORECASE)
    countNumOfReg = re.compile('(.)*count the ' , re.IGNORECASE)
    areReg = re.compile('^are ' , re.IGNORECASE)
    howMuchReg = re.compile('how much ' , re.IGNORECASE)
    whatYearReg = re.compile('^what year' , re.IGNORECASE)
    countryCodeReg = re.compile('country code' , re.IGNORECASE)
    whatAmountReg = re.compile('^what amount ' , re.IGNORECASE)
    isTheOrExreg = re.compile('^Is the+ (.)+ or ex', re.IGNORECASE)
    wereReg = re.compile('^Were ' , re.IGNORECASE)    
    GiveCountReg = re.compile('^Give(.)+count (.)' , re.IGNORECASE)
    CountReg = re.compile('(.)*count ' , re.IGNORECASE)
    
    with open(file, 'r' , encoding="utf8") as rf:
        category = ""
        questions = json.load(rf)
        qcount = len(questions)
        counter=0
        with open(fileResult, 'a' , encoding="utf8") as result:
            result.write('[\n \t')
        for question in questions :
            counter+=1
            if withinReg.match(question['question']):
                category = "resource"
                type = []
            elif  howManyReg.match(question['question']):
                category = "literal"
                type = "number"
            elif CountReg.match(question['question']):
                category = "literal"
                type = "number"
            elif hasReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif codeReg.match(question['question']):
                    category= "literal"
                    type = "number"
            elif doesEqualReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif doesGreaterReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif doesLessReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif isTrueReg.match(question['question']):
                    category="boolean"
                    type = "boolean"
            elif correctReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif isLessReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif isGreaterReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif isEqualReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif canReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"
            elif GiveCountReg.match(question['question']):
                    category= "literal"
                    type = "number"
            # test du matching avec Which       
            elif whichReg.match(question['question']):
                if whichIsTheMainReg.match(question['question']):
                    category = "resource"
                    type = []
                elif whichIsReg.match(question['question']):
                    category = "literal"
                    type = "string"
                elif whichYearReg.match(question['question']):
                    category = "literal"
                    type = "date"
                elif whichMeanReg.match(question['question']):
                    category = "literal"
                    type = "string"
                else:
                    category = "resource"
                    type = []
            elif whateverReg.match(question['question']):
                category = "resource"
                type = []
            elif whoReg.match(question['question']):
                category = "resource"
                type = []
            elif  howMuchReg.match(question['question']):
                category = "literal"
                type = "number"
            elif  countryCodeReg.match(question['question']):
                    category = "literal"
                    type = "number"    
            #test du matching avec What    
            elif  whatReg.match(question['question']):
                if whatAmountOfReg.match(question['question']):
                    category = "literal"
                    type = "number"
                elif whatIsQuantityOfReg.match(question['question']):
                    category = "literal"
                    type = "number"
                elif whatIsTheID.match(question['question']):
                    category ="literal"
                    type = "date"
                elif whatMethodReg.match(question['question']):
                    category ="literal"
                    type = "date"
                elif whatYearReg.match(question['question']):
                    category ="literal"
                    type = "date"
                elif WhatIsIDReg.match(question['question']):
                    category= "literal"
                    type = "number"
                elif whatIsThePopulationReg.match(question['question']):
                    category = "literal"
                    type = "number"
                elif whatIsTheNumberOfReg.match(question['question']):
                    category = "literal"
                    type = "number"
                elif whatIsNumberReg.match(question['question']):
                        category = "literal"
                        type = "number"
                elif whatAmountReg.match(question['question']):
                    category = "literal"
                    type = "number"
                elif whatIsTheOfTheReg.match(question['question']):                    
                    category = "literal"
                    type = ["number"]
                elif whatwasInDPReg.match(question['question']):                    
                    category = "boolean"
                    type = ["boolean"]
                else :
                    category = "resource"
                    type = []
            elif compareReg.match(question['question']):
                category = "boolean"
                type = "boolean" 
            # test du matching avec When       
            elif whenReg.match(question['question']):
                category = "literal"
                type = "date"
            #test du matching avec Where    
            elif  whereReg.match(question['question']):
                category = "resource"
                type = []           
                    
            #test du matching avec Whom,    
            elif  whomReg.match(question['question']):
                category = "resource"
                type = []
                    
            # test du matching avec Whose       
            elif whoseReg.match(question['question']):
                category = "resource"
                type = []
                    
            #test du matching avec Why    
            elif  whyReg.match(question['question']):
                category = "resource"
                type = []
            #test du matching avec Of Which    
            elif  ofWhichReg.match(question['question']):
                category = "resource"
                type = []            
            elif  inHowManyReg.match(question['question']):
                category = "literal"
                type = "number"                   
            elif inTheIsReg.match(question['question']):
                    category = "boolean"
                    type = "boolean"               
            elif  howManyReg.match(question['question']):
                category = "literal"
                type = "number"
            elif  inWhichReg.match(question['question']):
                if  inWhichYearReg.match(question['question']):
                    category = "literal"
                    type = "date"
                elif  inWhichCityReg.match(question['question']):
                    category = "resource"
                    type = []
                elif  inWhichCountryReg.match(question['question']):
                    category = "resource"
                    type = []
                else:
                    category = "resource"
                    type = []
            #test du matching avec How Many    
            
                    
            #test du matching avec Does 
            elif  doesReg.match(question['question']):
                category= "boolean"
                type = ["boolean"]
            elif  dateReg.match(question['question']):
                category= "date"
                type = ["date"]
            #test du matching avec Name    
            elif  nameReg.match(question['question']):
                if NameTheOf.match(question['question']):
                    category = "literal"
                    type = ["string"]
                else: 
                    category = "resource"
                    type = []
            #test du matching avec Did    
            elif  didReg.match(question['question']):
                category= "boolean"
                type = ["boolean"]
            #test du matching avec At what    
            elif  atWhatReg.match(question['question']):
                if atWhatPositionReg.match(question['question']):
                    category = "resource"
                    type = []
                elif atWhatAgeReg.match(question['question']):
                    category ="literal"
                    type = "number"
                else:
                    category = "literal"
                    type = "date"
            elif  wasReg.match(question['question']):
                if wasInOrReg.match(question['question']):
                    category = "boolean"
                elif wasOrReg.match(question['question']):
                    category= "resource"
                    type = []
                else:
                    category = "boolean"
                    type = "boolean"           
            
            elif  inWhatReg.match(question['question']):
                if  inWhatYearReg.match(question['question']):
                    category = "literal"
                    type = "date"
                else:
                    category = "resource"
                    type = []
            elif  doReg.match(question['question']):
                if doOrReg.match(question['question']):
                    category= "resource"
                    type = []
                else:
                    category = "boolean"
                    type = "boolean"
            elif  fromWhatReg.match(question['question']):
                category = "resource"
                type = []
            elif  howDidReg.match(question['question']):
                category = "resource"
                type = []
            elif extract_words(question['question']):
                category = "boolean"
                type = "boolean"
            #test du matching avec Is    
            elif  isReg.match(question['question']):
                if isTheOrExreg.match(question['question']):
                    category = "boolean"
                    type = "boolean"
                elif isInReg.match(question['question']):
                    category= "boolean"
                    type = "boolean"   
                elif isToOrReg.match(question['question']):
                    category = "boolean"
                    type = "boolean" 
                elif isOrReg.match(question['question']):
                    category= "resource"
                    type = []
                else:
                    category = "boolean"
                    type = "boolean"    
             
            elif theReg.match(question['question']):
                if theOfIsReg.match(question['question']):
                    category = "literal"
                    type = "literal"
                else:
                    category = "resource"
                    type = []
            elif countNumOfReg.match(question['question']):
                category = "literal"
                type = "number"
            elif  areReg.match(question['question']):
                category = "boolean"
                type = "boolean"
            elif  wereReg.match(question['question']):
                category = "boolean"
                type = "boolean"            
            else:
                category ="resource"
                type = []
            with open(fileResult, 'a' , encoding="utf8") as result:
                question['question'] = re.sub('\"|',"",question['question'])
                if qcount==counter :
                    result.write('{\n'+ '\t"id":' + str(question['id'])+ ',\n' +'\t"question":'+ '"'+str(question['question'])+'"' +',\n' + '\t"category":' + '"'+str(category)+ '"'+ ',\n'+'\t"type":' + '"'+str(type)+ '"'+ '\n'+ '}\n')
                else:
                    result.write('{\n'+ '\t"id":' + str(question['id'])+ ',\n' +'\t"question":'+ '"'+str(question['question'])+'"' +',\n' + '\t"category":' + '"'+str(category)+ '"'+ ',\n'+'\t"type":' + '"'+str(type)+ '"'+ '\n'+ '},\n')         
        with open(fileResult, 'a' , encoding="utf8") as result:
            result.write(']')

#test('types/AT_dbpedia_clean_literal_train_2022.json', 'types/AT_dbpedia_result_literal_train_2022.json')
#test('types/AT_dbpedia_clean_boolean_train_2022.json', 'types/AT_dbpedia_result_boolean_train_2022.json')
#test('types/AT_dbpedia_clean_ressource_train_2022.json', 'types/AT_dbpedia_result_ressource_train_2022.json')
test('clean-2022-dbpedia.json', 'result-dbpedia-2022.json')

def cleanTrain(TrainFile, cleanTrainFile):
    with open(TrainFile , 'r' , encoding='utf-8') as dirty:
        dirtiesQuestion = json.load(dirty)
        with open(cleanTrainFile, 'w' , encoding="utf8") as clean:
            for question in dirtiesQuestion:
                    question['question'] = re.sub('\"|',"",question['question'])
                    clean.write('{\n'+ '\t"id":' + str(question['id'])+ ',\n' +'\t"question":'+ '"'+str(question['question'])+'"' +'\n' + '},\n')

#cleanTrain('types/AT_dbpedia_ressource_train_2022.json',"types/AT_dbpedia_clean_ressource_train_2022.json")

def extract_words(str):
    Interrogate_words = ["which", "what", "whose", "when", "who", "whom", "where", "how", "why", "whether", "whatsoever", "whither", "whence", "whatever", "wherever"]
    for i in Interrogate_words:
        if i in str:
            return True
    return False

#print(extract_words("Mazhar Ul Haq High School, Beerwah is affiliated to Islamic Religion"))
