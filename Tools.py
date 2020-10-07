#MODULE: Tools
#AIM: To provide certain tools for Main module
#Read README for more details
#BEGIN CODE_

#master error count from Tools.py
errorCount2 = 0
errorCount4 = 0
errorCount7 = 0


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
        
    if typ=="y/n":
        if inpt=="y" or inpt=="Y":
            return True
        elif inpt=="n" or inpt=="N":
            return False

#TODO: take the no. of observations and validate it - for specific scenario only
def numOobs():
    #TODO: counting the number of wrong inputs. The FUN thing
    global errorCount2
    errorCount2 = 0

    #~The error message. To be changed with # of wrong inputs
    errorMsg2 = 'ERROR 002: Integer Required!'

    #~The MAIN thing
    while True:
        Num_o_obs = input('How many set of observations do you have? ')
        validation = verify(Num_o_obs)
        if validation==True:
            Num_o_obs = int(Num_o_obs)
            break
        elif validation==False:
            print("*"*len(errorMsg2))
            print(errorMsg2)
            print("*"*len(errorMsg2))
            errorCount2 += 1
            
        #~Varied error messages
        if errorCount2 == 2:
            errorMsg2 = 'ERROR 002: Ahem!... Please enter an integer'
        if errorCount2 == 4:
            errorMsg2 = 'ERROR 002: AN INTEGER! That\'s all I\'m asking...'
        if errorCount2 > 6:
            errorMsg2 = 'ERROR 002: I have told you '+str(errorCount2)+' times! You better see a brain doctor!'
    return Num_o_obs

#TODO: Datapoint entry. returns a list of dataset after looping - for specific scenario
def DTpt(Obs_num,varName):
    
    #~Error count reset
    global errorCount4
    errorCount4 = 0
    errorMsg4 = 'ERROR 004: Numbers Required!'

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
                print("*"*len(errorMsg4))
                print(errorMsg4)
                print("*"*len(errorMsg4))
                errorCount4 += 1
                

            #~Varied error messages
            if errorCount4 == 1:
                errorMsg4 = 'ERROR 004: Come on! You should enter NUMBERS...'
            if errorCount4 > 3:
                errorMsg4 = 'ERROR 004: NUMBERS!! I tell you! Enter NUMBERS!!'
            if errorCount4 > 5:
                errorMsg4 = 'ERROR 004: Loooord! Gimme strength!'
            if errorCount4 > 6:
                errorMsg4 = 'ERROR 004: I smite you!'
            if errorCount4 > 7:
                errorMsg4 = 'ERROR 004: I smite you again! You have been smotten...'
    return Datapoints

#TODO: Name setting algorithm. Specified scenario only
def graphCreds():
    title = input('Enter a suitable title for your Graph: ')
    xlabel = input('Enter a name for X-axis: ')
    ylabel = input('Enter a name for Y-axis: ')
    desc = input('Enter a short description of the graph: ')
    cred = {'TITLE':title,
            'X-LABEL':xlabel,
            'Y-LABEL':ylabel,
            'DESC':desc}
    return cred

#TODO: For an integer selection from a range. Specific scenario only
def MenuSelection():
    #~Error variables
    global errorCount7 
    errorCount7 = 0
    errorMsg7 = 'ERROR 007: Please select a number from the Menu.'

    while True:
        #~Face check variable
        LooksGood = False
        #~input comparing list
        inp_compare = ('1','2','3','4','5','6','7')
        if LooksGood == True:
            break
        elif LooksGood == False:
            #~User promt for out # selection
            Menu_slct = input('Please type in the NUMBER corresponding to your DESIRED choice: ')
            #~Validation Protocol
            validation = verify(Menu_slct)
            if validation == True:
                for integer in range(1,8):
                    if str(integer) in Menu_slct:
                        LooksGood = True
                        break
            if Menu_slct not in inp_compare:
                print("*"*len(errorMsg7))
                print(errorMsg7)
                print("*"*len(errorMsg7))
                errorCount7 += 1
                
            else:
                if '1' in Menu_slct:
                    return 1
                elif '2' in Menu_slct:
                    return 2
                elif '3' in Menu_slct:
                    return 3
                elif '4' in Menu_slct:
                    return 4
                elif '5' in Menu_slct:
                    return 5
                elif '6' in Menu_slct:
                    return 6
                elif '7' in Menu_slct:
                    return 7
        #~Varied error messages
        if errorCount7 == 1:
            errorMsg7 = 'ERROR 007: Oh hell Naw! Pick a number'
        if errorCount7 == 3:
            errorMsg7 = 'ERROR 007: ANY NUMBER from the menu. So easy!'
        if errorCount7 == 5:
            errorMsg7 = 'ERROR 007: Exactly what part of ANY NUMBER don\'t you understand?'
        if errorCount7 == 7:
            errorMsg7 = 'ERROR 007: Yo NIGGA! ANY NUMBER does\'nt ring any bells?'
        if errorCount7 == 10:
            errorMsg7 = 'ERROR 007: That\'s it! I\'m calling the cops on you!'
        if errorCount7 == 11:
            errorMsg7 = 'ERROR 007: 911? we have a brain dead idiot here. Need Help ASAP!'
        if errorCount7 == 12:
            errorMsg7 = 'ERROR 007: What? you don\'t deal with these kind of idiots as well?'
        if errorCount7 == 13:
            errorMsg7 = 'ERROR 007: Too bad! You are not wanted in this world or this life'
        if errorCount7 == 14:
            errorMsg7 = 'ERROR 007: You can go and cry in a corner now. Just don\'t spill any snot on me...'



#TODO: To return total error
def TotalErr_Tools():
    err = errorCount2 + errorCount4 + errorCount7
    return err
