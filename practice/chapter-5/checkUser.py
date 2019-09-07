#python hash table are called dict
#can be initialized two ways
#book = dict()
#book2 = {}


#create hash table
userDict = {}

def checkVote(name):
    if userDict.get(name):
        print ('kick {} out'.format(name))
    else:
        userDict[name] = True
        print ('welcome {} in'.format(name))


#test twice same name
checkVote('baba')
checkVote('baba')

#check twice diferent name
checkVote('baba2')
checkVote('baba3')