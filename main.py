#  __________    ___         __________   ____     ___   ___    __    
# |\   ____  \  |\  \       |\   ____  \ |\   '.  |\  \ |\  \ .' .'   
# \ \  \___\  \_\ \  \      \ \  \___\  \\ \    '.\ \  \\ \    .'     
#  \ \   _____  \\ \  \      \ \   ____  \\ \  \. '. \  \\ \    ''.   
#   \ \  \____\  \\ \  \______\ \  \__|\  \\ \  \'. '.\  \\ \  \'. '.  
#    \ \__________\\ \________\\ \__\ \ \__\\ \__\.'._____\\ \__\.'._'. 
#     \|__________| \|________| \|__|  \|__| \|__| '.|____| \|__| '|__| 
#                                                                                                                 ___ 
#  __________   _________   _________   _________   _________   ____     ___          _________       ___       .' .'| _________  
# |\   ______\ |\   _____\ |\   ___  \ |\   _____\ |\   _____\ |\   '.  |\  \        |\   _____\     |.  '.   .' .'.' |\   _____\ 
# \ \  \_____|_\ \  \____| \ \  \__\  \\ \  \___.| \ \  \___.| \ \    '.\ \  \       \ \  \___.|     '.'.  '.' .'.'   \ \  \___.| 
#  \ \_______  \\ \  \      \ \      __\\ \   __\   \ \   __\   \ \  \. '. \  \       \ \   __\        '.'.   ..'      \ \   __\  
#   \|.______\  \\ \  \______\ \  \. '.| \ \  \_|____\ \  \_|____\ \  \'. '.\  \   ___ \ \  \_|____      .' .  '.       \ \  \_|____ 
#     |\_________\\ \________\\ \__\'._'. \ \________\\ \________\\ \__\.'._____\ |\__\ \ \________\   .' .'.'.__'.      \ \________\
#     \|_________| \|________| \|__|'.|__| \|________| \|________| \|__| '.|____| \|__|  \|________| .' .'.' '.|__|       \|________| 
#                                                                                                  .'_.'.'             
#                                                                                                  |__|'                

#AIM: This program aims to take relevant inputs in order to plot a Linear-regression line
#using a matplotlib-based graph. Also To make user's lifa a living hell if they input the wrong stuff.
#For moe info read README.txt file
###############################
#Keys:
#TODO = type of function
#!!! = under construction
#-=-= = test line
#~ = inside TODO description
#BEGIN CODE_

#MODULE IMPORTING...
import Calculation as Calc
import Tools
import Graphmaker as Gm
import time

#introduction/welcome
print("#"*42)
print("################ WELCOME! ################\nThis program calculates linear regression")
print("#"*42)
print("IMPORTANT NOTICE: Try wrong input at your own risk.\nIt\'s your fault if I misbehave")

#QUESTIONAIRE START
print('Let\'s start collecting info!')

#TODO: Collecting Graph Credentials
Graph_creds = Tools.graphCreds()

#TODO: in order to change the Graph Credentials. if the user wants
#~error counting vairable and error message to be varied
errorCount1 = 0
errorMsg1 = 'ERROR 001: Please enter \"y\" or \"n\" as input'

while True:
    print("Following are your Graph Credentials:")
    print("Title        = ",Graph_creds['TITLE'],"\nX-axis Label = ",Graph_creds['X-LABEL'],"\nY-axis Label = ",Graph_creds['Y-LABEL'],"\nGraph text   = ",Graph_creds['DESC']) #!!!
    retryInput = input('Is this information correct? [y/n] ')
    if retryInput=='y' or retryInput=='Y':
        break
    elif retryInput=='n'  or retryInput=='N':
        Graph_creds = Tools.graphCreds()
    else:
        print('*'*len(errorMsg1))
        print(errorMsg1)
        print('*'*len(errorMsg1))
        errorCount1 += 1
        
    #~Varied error messages
    if errorCount1 == 1:
        errorMsg1 = 'ERROR 001: I support both, upper and lower case. :D'
    if errorCount1 == 2:
        errorMsg1 = 'ERROR 001: Are you stupid or something? XC'
    if errorCount1 == 7:
        errorMsg1 = 'ERROR 001: I\'m gonna shut down if you keep that attitude! B('
    if errorCount1 == 9:
        errorMsg1 = 'ERROR 001: FINAL WARNING! Do it again and I SHUT DOWN! I dare you.  >:)'
    if errorCount1 == 11:
        errorMsg1 = ''
        exit()

#TODO: Setting number of observations for the user's table
Num_o_obs = Tools.numOobs()

#TODO: in order to change the number of observations. if the user wants
errorCount3 = 0
errorMsg3 = 'ERROR 003: Please enter \"y\" or \"n\" as input'
while True:
    print("Very well... So there are a total of ",Num_o_obs,"Observations in your dataset")
    retryInput = input('Is this correct? [y/n] ')
    if retryInput=='y' or retryInput=='Y':
        break
    elif retryInput=='n'  or retryInput=='N':
        Num_o_obs = Tools.numOobs()
    else:
        print('*'*len(errorMsg3))
        print(errorMsg3)
        print('*'*len(errorMsg3))
        errorCount3 += 1
        
    #~Varied error messages
    if errorCount3 == 1:
        errorMsg3 = 'ERROR 003: I support both, upper and lower case. :D'
    if errorCount3 == 2:
        errorMsg3 = 'ERROR 003: Are you stupid or something? XC'
    if errorCount3 == 6:
        errorMsg3 = 'ERROR 003: You Bacon Head! You Stinky Wombat!'
    if errorCount3 == 8:
        errorMsg3 = 'ERROR 003: I\'m gonna shut down if you keep that attitude! B('
    if errorCount3 == 9:
        errorMsg3 = 'ERROR 003: FINAL WARNING! Do it again. I dare you.  >:)'
    if errorCount3 == 11:
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
errorCount5 = 0
errorMsg5 = 'ERROR 005: Please enter \"y\" or \"n\" as input'
print("="*45)
while True:
    #~Representing datapoints
    print("Following is the list of data set by you:")
    print('   X      -->     Y')
    for itemx,itemy in zip(X,Y):
        print('   ',round(itemx,5),'  -->  ',round(itemy,5))
    
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
        print('*'*len(errorMsg5))
        print(errorMsg5)
        print('*'*len(errorMsg5))
        errorCount5 += 1
        
    #~Varied error messages
    if errorCount5 == 1:
        errorMsg5 = 'ERROR 005: Enter \"y\" or \"n\". Simple isn\'t it? :V'
    if errorCount5 == 3:
        errorMsg5 = 'ERROR 005: You know what? I\'m done with you! >:P'
    if errorCount5 == 4:
        errorMsg5 = 'ERROR 005: You know I\'m a Mage that can send you into an Infinite time loop?'
    if errorCount5 == 5:
        errorMsg5 = 'ERROR 005: If you do that again I\'ll realy do it. Be afraid!'
    if errorCount5 == 6:
        errorMsg5 = 'ERROR 005: Aaaand done! You are trapped into my Infinite-time loop!'

#PROCESSING STARTS
#TODO: Making dictionary out of X and Y
print('Processing your inputs...')
print('Generating Regression line...\nPlease wait...')
time.sleep(2.5)

#~empty dictionary. to be filled with inputs
DTpt_Bind_Org = {}
DTpt_Bind_Reg = {}

#~Filling items into the empty dictionary "X" values and "Y HAT" values
for itemx,itemy in zip(X, Calc.y_Hat(X,Y)):
    DTpt_Bind_Reg[itemx] = itemy

#~Filling items into the empty dictionary "X" values and "Y" values
for itemx,itemy in zip(X,Y):
    DTpt_Bind_Org[itemx] = itemy

#~sorting and filling lists !!!
X = []
Y = []
for itemx, itemy in sorted(DTpt_Bind_Org.items()):
    X.append(itemx)
    Y.append(itemy)

#~Representing data in all it's glory!
print('    X   -->   Y=f(X)    ')
for key,val in sorted(DTpt_Bind_Reg.items()):
    print('   ',key,'  -->  ',val)

print("######################################")
print("############ INSTRUCTION #############")
print("Take a screenshot and CLOSE THE GRAPH\n   in order to proceed further")
print("######################################")
print("Graph is loading...")
time.sleep(1.7)
#TODO: Simple plain old Graph plot   !!!
Gm.daPlot(X,Y,
          Graph_creds['TITLE'],
          Graph_creds['X-LABEL'],
          Graph_creds['Y-LABEL'],
          Graph_creds['DESC'])

#TODO: ask for additional info
#!!! verification method needed
#~variable for inference loop activation
ASK = True

errorMsgs6 = 'ERROR 006: Please type \"y\" or \"n\"'
errorCount6 = 0
#~Promt for shutdown or more info
while True:
    adinfoQ = input('Would you like to see some additional inferences? [y/n] ')
    verification = Tools.verify(adinfoQ,typ="y/n")
    if verification == True:
        break
    elif verification == False:
        ASK = False
        break
    else:
        print('*'*len(errorMsgs6))
        print(errorMsgs6)
        print('*'*len(errorMsgs6))
        errorCount6 += 1
        
    #~Varied error messages
    if errorCount6 == 1:
        errorMsgs6 = 'ERROR 006: Enter \"y\" or \"n\". Simple isn\'t it? :V'
    if errorCount6 == 3:
        errorMsgs6 = 'ERROR 006: You somehow survived my Infinite-time loop. But this time you won\'t!'
    if errorCount6 == 4:
        errorMsgs6 = 'ERROR 006: You still think I\'m joking about that time loop spell?'
    if errorCount6 == 5:
        errorMsgs6 = 'ERROR 006: If you do that again I\'ll realy do it. Be afraid!'
    if errorCount6 == 6:
        errorMsgs6 = 'ERROR 006: Aaaand done! You are trapped into my Infinite-time loop!'

#TODO: ask for specific info
errorCount8 = 0
errorMsg8 = 'ERROR 008: Please type \"y\" or \"n\"' 
while ASK:
    print("#"*40)
    print('Following is a menu of all inferences you can select')
    print('1- Original Plots\n2- Regression line Plots\n3- Correlation Coefficient\n4- Coefficient of Determination\n5- Error analysis \n6- All inferences\n7- Exit')
    select = Tools.MenuSelection()

    #~specifying which number means what
    if select==1:
        Gm.Originalplots(DTpt_Bind_Org)
    elif select==2:
        Gm.Regressionplots(DTpt_Bind_Reg)
    elif select==3:
        Gm.CoffR(X,Y)
    elif select==4:
        Gm.CoffR2(X,Y)
    elif select==5:
        Gm.SumSqErr(X,Y)
    elif select==6:
        Gm.Originalplots(DTpt_Bind_Org)
        Gm.Regressionplots(DTpt_Bind_Reg)
        Gm.CoffR(X,Y)
        Gm.CoffR2(X,Y)
        Gm.SumSqErr(X,Y)
    elif select==7: 
        while True:
            exitQ = input("Are you sure you want to EXIT? [y/n] ")
            verification = Tools.verify(exitQ,typ="y/n")
            if verification == True:
                ASK = False
                break
            elif verification == False:
                break
            else:
                print('*'*len(errorMsg8))
                print(errorMsg8)
                print('*'*len(errorMsg8))
                errorCount8 += 1
                
            #~Varied error messages
            if errorCount8 == 1:
                errorMsg8 = 'ERROR 008: Come on! You should enter NUMBERS...'
            if errorCount8 == 3:
                errorMsg8 = 'ERROR 008: NUMBERS!! I tell you! Enter NUMBERS!!'
            if errorCount8 == 5:
                errorMsg8 = 'ERROR 008: Loooord! Gimme strength!'
            if errorCount8 == 6:
                errorMsg8 = 'ERROR 008: I smite you!'
            if errorCount8 == 7:
                errorMsg8 = 'ERROR 008: I smite you again! You have been smotten...'
            if errorCount8 == 13:
                errorMsg8 = 'ERROR 008: Ok I\'m tired of smiting you again and again...'
            if errorCount8 == 14:
                errorMsg8 = 'ERROR 008: I\'ll shut down now. But I\'ll give you just one last chance.'
            if errorCount8 == 15:
                exit()
    if ASK == False:
        break

#TODO: Total error message if you annoyed the program
ERRORS_CAUSED = errorCount1 + errorCount3 + errorCount5 + errorCount6 + errorCount8 + Tools.TotalErr_Tools()
 
if ERRORS_CAUSED > 0 and ERRORS_CAUSED <= 5:
    print("By the way, you were dumb enough to enter wrong inputs ",ERRORS_CAUSED," times\nBut still you could\'ve been more annoying.")
    time.sleep(1.5)
elif ERRORS_CAUSED > 5 and ERRORS_CAUSED <= 10:
    print("By the way, you really did a number on my processor by entering wrong inputs ",ERRORS_CAUSED," times\nYou really were hard to work with ... \nSorry but that\'s the sad truth.")
    time.sleep(1.5)
elif ERRORS_CAUSED > 10:
    print("I really want to mention this, \nbut I highly doubt that your pathetic little processor \nor whatever runs on the back-end of your visual-inputs will get it.")
    print("YOU ARE DUMB!")
    time.sleep(1.5)
    print("YOU ARE REALLY REALLY DUMB!")
    time.sleep(1.5)
    print("FOR REAL!")
    time.sleep(1)
    print(ERRORS_CAUSED," times you annoyed me!\n"+str(ERRORS_CAUSED)+"? Really?...\nEven after countless times I put up with your stupidity")
    time.sleep(1)
    print("Cursed you into an infinite-time loop...")
    time.sleep(1)
    print("Smote you...")
    time.sleep(1)
    print("Wished for you to have a seizure so that you would stop using me...")
    time.sleep(1)
    print("But you still ...")
    time.sleep(1.4)
    print("Bullying me...")
    time.sleep(1.4)
    print("Annoying me...")
    time.sleep(1.6)
    print("You really are the scum of the earth...")
    time.sleep(1.7)
    print("Please don\'t come back ever again!")
   
#TODO: Pay Respects
#~Lo and..
print("####################################################################################")
print("Since you are finished with the analysis, it\'s time I show you who my creator is...")
print("Wait for it...")

#~wait for it
time.sleep(2)

#~Behold the reckoning!
print(" __________     ___          __________     ____     ___     ___    __     ")  
print("|\   ____  \   |\  \        |\   ____  \   |\   '.  |\  \   |\  \ .' .'    ")  
print("\ \  \___\  \_ \ \  \       \ \  \___\  \  \ \    '.\ \  \  \ \    .'      ")  
print(" \ \   _____  \ \ \  \       \ \   ____  \  \ \  \. '. \  \  \ \    ''.    ") 
print("  \ \  \____\  \ \ \  \______ \ \  \__|\  \  \ \  \ . '.\  \  \ \  \ . '.  ") 
print("   \ \__________\ \ \________\ \ \__\ \ \__\  \ \__\.'._____\  \ \__\.'._'.")
print("    \|__________|  \|________|  \|__|  \|__|   \|__| '.|____|   \|__| '|__|")
print("                                                                                                                    ___               ")
print(" __________    _________    _________    _________    _________    ____     ___          _________      ___       .' .'| _________     ") 
print("|\   ______\  |\   _____\  |\   ___  \  |\   _____\  |\   _____\  |\   '.  |\  \        |\   _____\    |.  '.   .' .'.' |\   _____\    ")
print("\ \  \_____|_ \ \  \____|  \ \  \__\  \ \ \  \___.|  \ \  \___.|  \ \    '.\ \  \       \ \  \___.|    '.'.  '.' .'.'   \ \  \___.|    ")
print(" \ \_______  \ \ \  \       \ \      __\ \ \   __\    \ \   __\    \ \  \. '. \  \       \ \   __\       '.'.   ..'      \ \   __\     ")
print("  \|.______\  \ \ \  \______ \ \  \. '.|  \ \  \_|____ \ \  \_|____ \ \  \ . '.\  \   ___ \ \  \_|____     .' .  '.       \ \  \_|____ ")
print("    |\_________\ \ \________\ \ \__\ ._'.  \ \________\ \ \________\ \ \__\.'._____\ |\__\ \ \________\  .' .'.'.__'.      \ \________\ ")
print("    \|_________|  \|________|  \|__|'.|__|  \|________|  \|________|  \|__| '.|____| \|__|  \|________|.' .'.' '.|__|       \|________|")
print("                                                                                                     .'_.'.'                          ")
print("                                                                                                     |__|'                            ")

#~Still exiting...
print("###################################################################################")
print("TADAAAAA~")
print("Now please wait some more. I\'ll prepare for a suicide ... I mean shut myself down.")

#~wait before exiting
time.sleep(2)
exit()
