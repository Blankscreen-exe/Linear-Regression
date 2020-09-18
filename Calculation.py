#MODULE: Calculation
#AIM: To create formulae for linear regression calculation
#list of functions:
#Sxy(x,y)
#Sxx(x)
#a1(Sxx,Sxy)
#a0(x,y)
#y_Hat(x,y)
#axb(lst1,lst2)
#list_sum(lst)
#list_square(lst)
#list_mean(var)
#list_min(lst)
#list_max(lst)

#EXTRA FUNCTIONS
#R(x,y)
#SSE(x,y)
#SSR(x,y)  
#SST(y)
#BEGIN CODE_

#TODO: Returns a single "max" value. inputs list
def list_max(lst):
    maximum = -9999999
    for num in lst:
        if num>maximum:
            maximum = num
    return maximum

#TODO: Returns a single "min" value. inputs list
def list_min(lst):
    minimum = 9999999
    for num in lst:
        if num<minimum:
            minimum = num
    return minimum
            
#TODO: Returns a single value for Sxy. inputs list
def Sxy(x,y):
    n = len(x)
    result = list_sum(axb(x,y)) - n*list_mean(x)*list_mean(y)
    return result

#TODO: Returns a single value for Sxx. inputs list   
def Sxx(x):
    n = len(x)
    result = list_sum(list_square(x)) - n*(list_mean(x))**2
    return result

#TODO: returns a1 value. outputs single value 
def a1(Sxx,Sxy):
    a_sub_one = Sxy/Sxx
    return a_sub_one

#TODO: returns a0 value. outputs single value   
def a0(x,y):
    a_naught = list_mean(y) - (a1(Sxx(x),Sxy(x,y))*list_mean(x))
    return a_naught

#TODO: returns y hat value for a complete list. outputs list
def y_Hat(x,y):
    yhat = []
    for items in x:
        yhat.append((a1(Sxx(x),Sxy(x,y))*items) + a0(x,y))
    return yhat

#TODO: multiplies corresponding values of both list elements. Outputs list
def axb(lst1,lst2):
    result = []
    for itemsx, itemsy in zip(lst1,lst2):
        result.append(itemsx*itemsy)
    return result       

#TODO: subtracts corresponding values of both list elements. Outputs list
def a_b(lst1,lst2):
    result = []
    for itemsx, itemsy in zip(lst1,lst2):
        result.append(itemsx-itemsy)
    return result 

#TODO: returns sum of a whole list. outputs single value  
def list_sum(lst):
    result = 0
    for items in lst:
        result += items
    return result

#TODO: takes square of a list one by one. outputs list 
def list_square(lst):
    result = []
    for squared in lst:
        result.append(squared**2)
    return result

#TODO: Takes Mean in a single number variable
def list_mean(var):
    var_aux = 0
    for items in var:
        var_aux += items
    result = var_aux/len(var)
    return result
    
####################
#Extra Calculations#
####################

def R(x,y):
    n = len(x)
    result = ( n*list_sum(axb(x,y)) - list_sum(x)*list_sum(y) )/( ( n*list_sum(list_square(x)) - (list_sum(x))**2 )*( n*list_sum(list_square(y)) - (list_sum(y))**2 ) )**(1/2)
    return result

def SSE(x,y):
    result = list_sum( list_square( a_b( y,y_Hat(x,y) ) ) )
    return result

def SSR(x,y):
    sub = []
    for items in y_Hat(x,y):
        sub.append(items - list_mean(y))
    result = list_sum( list_square( sub ) )
    return result

def SST(y):
    sub = []
    for items in y:
        sub.append(items - list_mean(y))
    result = list_sum( list_square( sub ) )
    return result
    
####################
#    TEST AREA     #
####################
x = [0,1,2,3,4,5,6]
y = [0,2,2.75,3.2,3,4.2,5]
#print('='*90)
#print('Data-points for regression:\n',y_Hat(x,y))
#print('='*90)
#print('Correlation coefficient:\n',R(x,y),' ==>> ',R(x,y)*100,'%')
#print('='*90)
#print('Coefficient of determination:\n',R(x,y)**2,' ==>> ',(R(x,y)**2)*100,'%')
#print('='*90)
#print('SST   =   SSR   +   SSE')
#print(SST(y),'   =   ',SSR(x,y),'   +   ',SSE(x,y))
#print(SST(y),'   =   ',SSR(x,y)+SSE(x,y))