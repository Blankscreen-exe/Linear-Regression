#4/9/2020
#Module for datapoint collection
#mainly X and Y values
# Key: !!   = code replacing
#      TODO = code purpose

#TODO: RANGE selection
def ObsRange():
    while True:
        ObservationRange = input('How many observations does your Data set have? ')
        global ObservationRange_convert
        #entry validation
        try:
            ObservationRange_convert = int(ObservationRange)
            #if isinstance(ObservationRange_convert,int):
                #!!confirmation to end the loop or re-enter
             #   return int(ObservationRange)
            if isinstance(ObservationRange_convert,int):
                #!!confirmation to end the loop or re-enter
                return int(ObservationRange)
        except:
            print('\n*************************************************')
            print('ERROR 001: Observation number MUST be an integer!') #!!error message to be varied with # of illegal responses
            print('*************************************************\n')
            continue

#TODO: Datapoint selection
def ObsEntry():       
    global X_VALS
    X_VALS = []
    for obsval in range(ObservationRange_convert):
        while True:
            x_input = input('Enter your X variable observation: ')
            #!! validation protocol needed to be fixed
            if isinstance(x_input,int) or isinstance(x_input,float):
                x_input_convert = eval(x_input)
                return x_input_convert
            try:
                x_input_convert = eval(x_input)
            except:
                print('\n*************************************')
                print('ERROR 002: X Value MUST be an number!') #!!error message to be varied with # of illegal responses
                print('*************************************\n')
        X_VALS.append(x_input_convert)
        print('Here is your updated list of X values:\n',X_VALS)
    
    global Y_VALS
    Y_VALS = []
    for i in range(ObservationRange_convert):
        y_input = eval(input('Enter your corresponding Y variable observation: '))
        Y_VALS.append(y_input)
        print('Here is your updated list of Y values:\n',Y_VALS)
        #!! validation protocol needed
    
    print('Following is a complete list of X values in correspondence to their Y values:\n',
          'X = ',X_VALS,'\n',
          'Y = ',Y_VALS,)

#TODO: Collect the value for scale gaps in x and y axis on graph
def ScaleGap():
    while True:
        x_gap = input('How many gaps do you want on your Y axis? ')
        #!!response validation required
        print(x_gap)
        try:
            x_gap_convert = int(x_gap)
            if isinstance(x_gap_convert,int):
                x_gap = int(x_gap)
                return  x_gap
                print(x_gap)
        except:
            print('\n*************************************')
            print('ERROR 003: X Value MUST be an INTEGER!') #!!error message to be varied with # of illegal responses
            print('*************************************\n')
    return x_gap
    
#TEST zone -- delete it after program finished
print(ObsRange())
ObsEntry()
print(ScaleGap())