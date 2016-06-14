'''
Created on Jun 14, 2016

@author: Giuij
'''

class Underscoree(object):

    def __init__(self, *arg):
        '''
        Constructor
        '''
    def mapp(self,list,iteratee):
        aa=[iteratee(a) for a in list]
        return aa
            
    def reducee(self,list,iteratee,memo):
        for a in list:
            memo= iteratee(a,memo)
        return memo      
             
    def findd(self,list, predicate):
        for a in list:
            if predicate(a)==True:
                return a
                break

    def filterr(self,list,predicate): 
        aa=[a for a in list if (predicate(a)==True)]
        return aa
#         arr=[]
#         for a in list:
#             if predicate(a)==True:
#                 arr.append(a)
#         return arr
#         
    def rejectt(self,list,predicate):
        aa=[a for a in list if (predicate(a)==False)]
        return aa

# _ = Underscoree()
# evens = _.mapp([1, 2, 3, 4, 5, 6], lambda x: x*3)
# 
# _ = Underscoree()
# evens = _.reducee([1, 2, 3, 4, 5, 6], lambda x,y: x+y,0)

# _ = Underscoree() # 
# evens = _.findd([1, 2, 3, 4, 5, 6], lambda x: x%2==0) 

# _ = Underscoree() # yes we are setting our instance to a variable that is an underscore
# evens = _.filterr([1, 2, 3, 4, 5, 6], lambda x: x%2==0)

# _ = Underscoree() # yes we are setting our instance to a variable that is an underscore
# evens = _.rejectt([1, 2, 3, 4, 5, 6], lambda x: x%2==0)
print evens