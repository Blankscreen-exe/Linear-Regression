#MODULE: Tools
#PURPOSE: To provide certain tools for Main module
#Read README for more details
#BEGIN CODE_

#TODO: Returns True if the parameter is the desired input type. Else returns False
def verify(inpt,typ="int"):
    if typ=="int":
        try:    
            inpt = int(inpt)
            if isinstance(inpt,int):
                return True
            else:
                return False
        except:
            return False
        
    if typ=="float":
        try:
            inpt = float(inpt)
            if isinstance(inpt,float):
                return True
            else:
                return False
        except:
            return False
        
    if typ=="str":
        try:    
            if isinstance(inpt,str):
                return True
            else:
                return False
        except:
            return False
        
    if typ=="num":
        try:
            inpt = eval(inpt)
            if isinstance(inpt,float) or isinstance(inpt,int):
                return True
            else:
                return False
        except:
            return False

#TODO: take the no. of observations and validate it - for specific scenario
def numOobs():
    #TODO: counting the number of wrong inputs. The FUN thing
    errorCount = 0

    #~The FUN thing
    errorMsg1 = 'ERROR 001: Integer Required!'

    #~The MAIN thing
    while True:
        Num_o_obs = input('How many set of observations do you have? ')
        validation = verify(Num_o_obs)
        if validation==True:
            Num_o_obs = int(Num_o_obs)
            break
        elif validation==False:
            print("*"*len(errorMsg1))
            print(errorMsg1)
            print("*"*len(errorMsg1))
            errorCount += 1
            
        #~The FUN thing
        if errorCount == 1:
            errorMsg1 = 'ERROR 001: Ahem!... Please enter an integer'
        elif errorCount > 2:
            errorMsg1 = 'ERROR 001: I have told you '+str(errorCount)+' times! You better see a brain doctor!'
    return Num_o_obs

#TODO: Datapoint entry. returns a list of dataset after looping - for specific scenario
def DTpt(Obs_num,varName):
    
    #~Error count reset
    errorCount = 0
    errorMsg2 = 'ERROR 003: Numbers Required!'

    #~Datapoint inputs
    Datapoints = []

    for obsEntry in range(Obs_num): #!!!
        #~The MAIN thing
        while True:
            entry = input('Enter '+str(varName)+' value '+str(obsEntry+1)+': ')
            validation = verify(entry,typ="num")
            if validation==True:
                entry = eval(entry)
                Datapoints.append(entry)
                break
            elif validation==False:
                print("*"*len(errorMsg2))
                print(errorMsg2)
                print("*"*len(errorMsg2))
                errorCount += 1

            #~Varied error messages
            if errorCount == 1:
                errorMsg2 = 'ERROR 003: Come on! You should enter NUMBERS...'
            if errorCount > 3:
                errorMsg2 = 'ERROR 003: NUMBERS!! I tell you! Enter NUMBERS!!'
            if errorCount > 5:
                errorMsg2 = 'ERROR 003: Loooord! Gimme strength!'
    return Datapoints
