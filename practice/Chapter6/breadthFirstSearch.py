#create a graph
#then, search graph for those who are mango seller
#mango seller have prefix _m added to their name

graph = {}
def createGraph(user, neighbour):

    if (type(neighbour) == list) & (type(user) == str):
        graph[user] = neighbour
    elif (type(neighbour) == str) & (type(user) == str):
        graph[user] = [neighbour]
    elif (type(user) != str):
        print('user should be string')

    else:
        print ('neighbour should be string or list')
    return graph


#find user
#import requirements
from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def findMangoSeller(graph,main_user):
    search_queue = deque()
    search_queue += graph[main_user]
    searched = []
    #print(graph[main_user])

    while search_queue:
       person = search_queue.popleft()
       print(search_queue)
       if not person in searched:
           if person_is_seller(person):
               print( person + " is a mango seller")
               return True
           else:
               search_queue += graph[person]
               searched.append(person)
    return False


#create graph
user = 'eis'
neighbour = ['mages','gana','jega']
createGraph(user,neighbour)

user = 'mages'
neighbour = ['temple_fren', 'kindy_fren','gana']
createGraph(user,neighbour)

user = 'temple_fren'
neighbour = []
createGraph(user,neighbour)

user = 'kindy_fren'
neighbour = []
createGraph(user,neighbour)

user = 'jega'
neighbour = ['mommy', 'bro', 'long_lost']
createGraph(user,neighbour)

user = 'mommy'
neighbour = []
createGraph(user,neighbour)

user = 'bro'
neighbour = []
createGraph(user,neighbour)

user = 'long_lost'
neighbour = ['log_m']
createGraph(user,neighbour)

user = 'log_m'
neighbour = []
createGraph(user,neighbour)

user = 'gana'
neighbour = []
createGraph(user,neighbour)
graphy = createGraph(user,neighbour)

print(graphy)
findMangoSeller(graphy,'eis')

