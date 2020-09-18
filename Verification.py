#MODULE: Input Verification
#PURPOSE: To verify users input if it is the desired one or not.
#By default verification of integer is set.
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