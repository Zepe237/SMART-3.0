import json 
import re 
def eval (file1, file2):
    mySolution = []
    realSolution = []
    positivCpt =0
    negativCpt =0
    with open(file1, 'r', encoding="utf8") as file1:
        mySolution = json.load(file1)
        print(len(mySolution))
    with open(file2 ,'r', encoding="utf-8") as file2:
        realSolution = json.load(file2)
        print(len(mySolution))
    with open('mistake.json', 'w' , encoding="utf8") as result:
        result.write('[\n')
        for i in range(len(realSolution)):
            if mySolution[i]['category']==realSolution[i]['category']:
                positivCpt+=1
            elif  mySolution[i]['category']!=realSolution[i]['category']:
                    negativCpt+=1
                    print('\n \t question :{},\n \t category :{}    {}'.format(realSolution[i]['question'],realSolution[i]['category'],mySolution[i]['category']))
                    mySolution[i]['question'] = re.sub('\"|',"",mySolution[i]['question'])
                    if realSolution[i]['category']=="literal":
                        result.write('{\n'+ '\t"id":' + str(mySolution[i]['id'])+ ',\n' +'\t"question":'+ '"'+str(mySolution[i]['question'])+'"' +',\n' + '\t"category":' + '"'+str(mySolution[i]['category'])+ '"'+ ',\n'+ '\t"solution":' + '"'+str(realSolution[i]['category'])+ '"'+ '\n'+ '},\n')
        result.write('\n]\n')
    print('le compteur positif est {}'.format(positivCpt))
    print('le compteur negatif est {}'.format(negativCpt)) 
    print('le nombre totale de question est {}'.format(positivCpt+negativCpt))
    print('L\'accuracy est donc de : {}'.format(positivCpt/len(realSolution)))

eval('result-dbpedia-2022.json','smart-2022-datasets-main/smart-2022-datasets-main/AT_answer_type_prediction/dbpedia/SMART2022-AT-dbpedia-train.json')
#eval('result-wikidata-2022.json','smart-2022-datasets-main/smart-2022-datasets-main/AT_answer_type_prediction/wikidata/SMART2022-AT-wikidata-train.json')
#eval('re"id"sult-wikidata-2022.json','smart-2022-datasets-main/smart-2022-datasets-main/AT_answer_type_prediction/wikidata/SMART2022-AT-wikidata-train.json')


        