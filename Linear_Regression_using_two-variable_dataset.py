#AIM: This program aims to take relevant inputs in order to plot a Linear-regression line
#using a character-based graph.
#For moe info read README.txt file
###############################
#Keys:
#TODO = type of function
#!!! = under construction
#-=-= = test line
#~ = inside TODO description
#BEGIN CODE_

#MODULE IMPORTING...
import Calculation
import Tools
#import CharGraph #!!!

#introduction/welcome
print("#"*42)
print("################ WELCOME! ################\nThis program calculates linear regression")
print("#"*42)

#QUESTIONAIRE START
Num_o_obs = Tools.numOobs()

#TODO: in order to change the number of observations. if the user wants
errorCount = 0
errorMsg2 = 'ERROR 002: Please enter \"y\" or \"n\" as input'
while True:
    print("Very well... So there are a total of ",Num_o_obs,"Observations in your dataset")
    retryInput = input('Is this correct? [y/n] ')
    if retryInput=='y' or retryInput=='Y':
        break
    elif retryInput=='n'  or retryInput=='N':
        Num_o_obs = Tools.numOobs()
    else:
        print('*'*len(errorMsg2))
        print(errorMsg2)
        print('*'*len(errorMsg2))
        errorCount += 1
    #~Varied error messages
    if errorCount == 1:
        errorMsg2 = 'ERROR 002: I support both, upper and lower case. :D'
    if errorCount == 2:
        errorMsg2 = 'ERROR 002: Are you stupid or something? XC'
    if errorCount == 7:
        errorMsg2 = 'ERROR 002: I\'m gonna shut down if you keep that attitude! B('
    if errorCount == 9:
        errorMsg2 = 'ERROR 002: FINAL WARNING! sissy. Do it again. I dare you.  >:)'
    if errorCount == 11:
        errorMsg2 = ''
        exit()

#TODO: take input upto the number of set observations
#~Datapoint inputs
print('='*45)
print('Number of set of observation = ',Num_o_obs,' --> Acknowledged')
print('Start entering datapoints for \"X\"')
X = Tools.DTpt(Num_o_obs,"X")
print('Start entering datapoints for \"Y\"')
Y = Tools.DTpt(Num_o_obs,"Y")

#TODO: To confirm input for datapoints
errorCount = 0
errorMsg4 = 'ERROR 004: Please enter \"y\" or \"n\" as input'
print("="*45)
while True:
    #~Representing datapoints
    print("Following is the list of data set by you:")
    print('X    -->   Y')
    for itemx,itemy in zip(X,Y):
        print(itemx,'  -->  ',itemy)
    
    #~Confirming if user wants to change the datapoints
    retryInput = input('Is this correct? [y/n] ')
    if retryInput=='y' or retryInput=='Y':
        break
    elif retryInput=='n'  or retryInput=='N':
        print('Start entering datapoints for \"X\"')
        X = Tools.DTpt(Num_o_obs,"X")
        print('Start entering datapoints for \"Y\"')
        Y = Tools.DTpt(Num_o_obs,"Y")
    else:
        print('*'*len(errorMsg4))
        print(errorMsg4)
        print('*'*len(errorMsg4))
        errorCount += 1
    #~Varied error messages
    if errorCount == 1:
        errorMsg4 = 'ERROR 004: Enter \"y\" or \"n\". Simple isn\'t it? :V'
    if errorCount == 3:
        errorMsg4 = 'ERROR 004: You know what? I\'m done with you! >:P'
    if errorCount == 4:
        errorMsg4 = 'ERROR 004: Oh Lord! Smite this human who tormenteth moi'
    if errorCount == 6:
        errorMsg4 = 'ERROR 004: Do that again and I\'ll Shutdown on your pathetic face! X('
    if errorCount == 8:
        errorMsg4 = ''
        exit()

#TODO: Making dictionary out of X and Y
print('Converting your input into dictionary format...')
print('Sorting...\nPlease wait...')
#~empty dictionary. to be filled with inputs
DTpt_compendium = {}               
#~Filling items into the empty dictionary
for itemx,itemy in zip(X,Y):
    DTpt_compendium[itemx] = itemy
#~Representing data in all it's glory!
print('    X   -->   Y=f(X)    ')
for key,val in sorted(DTpt_compendium.items()):
    print('   ',key,'  -->  ',val)

#TODO: nAow fo the THING y'all 'ave bin waitin' foUr ... CHAracter GRAAAAAAPH! *Rock music plays*

#TODO: ask for additional info

#TODO: ask for specific info
print('='*90)
print('Data-points for regression line:\n')
reg = Calculation.y_Hat(X,Y)
for i in reg:
    print(i)
print('='*90)
print('Correlation coefficient:\n',Calculation.R(X,Y),' ==>> ',Calculation.R(X,Y)*100,'%')
print('='*90)
print('Coefficient of determination:\n',Calculation.R(X,Y)**2,' ==>> ',(Calculation.R(X,Y)**2)*100,'%')
print('='*90)
print('SST   =   SSR   +   SSE')
print(Calculation.SST(Y),'   =   ',Calculation.SSR(X,Y),'   +   ',Calculation.SSE(X,Y))
print(Calculation.SST(Y),'   =   ',Calculation.SSR(X,Y)+Calculation.SSE(X,Y))
    
#ask to shut the program down + errorCount message
