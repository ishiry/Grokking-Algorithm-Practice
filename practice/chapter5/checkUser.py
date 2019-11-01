#python hash table are called dict
#can be initialized two ways
#book = dict()
#book2 = {}


#create hash table
userDict = {}

def check_vote(name):
    if userDict.get(name):
        print ('kick {} out'.format(name))
    else:
        userDict[name] = True
        print ('welcome {} in'.format(name))


#test twice same name
check_vote('baba')
check_vote('baba')

#check twice diferent name
check_vote('baba2')
check_vote('baba3')