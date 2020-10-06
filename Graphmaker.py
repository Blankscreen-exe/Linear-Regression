#MODULE: Graphmaker
#AIM: Togenerate a graph using "matplotlib" and to output inferences obtained from analysis
#Moe info in README file
#BEGIN CODE_

#Imports
import Calculation as Calc
from matplotlib import pyplot as plt
from matplotlib import style
#Graph style setting
style.use("fivethirtyeight")

#TODO: plotting using matplotlib
def daPlot(x,y,TITLE,XLABEL,YLABEL,TEXT):
    #~plotting
    fig = plt.figure()

    plt.plot(x,y,'go',label='Original Plots',linewidth=2)
    plt.plot(x,y,'#707070',linewidth=1)
    plt.plot(x,Calc.y_Hat(x,y),'r',label='Regression Line',linewidth=1)
    plt.title(TITLE)
    plt.ylabel(YLABEL)
    plt.xlabel(XLABEL)
    plt.legend(loc="upper right")
    fig.set_figheight(10)
    fig.set_figwidth(10)

    fig.text(.5, 0.87, TEXT, ha='center', va='top')
    plt.show()    

#TODO: Displays original plots
def Originalplots(Bind):
    #~Display
    print('==================================')
    print('Following are your ORIGINAL PLOTS:')
    print('==================================')
    print('      X      --|-->  Y=f(X)     ')
    print('--------------------------------')
    for itemsx, itemsy in sorted(Bind.items()):
        print('  ',round(itemsx,6),' ---> ',round(itemsy,6))
    

#TODO: Displays regression plots    
def Regressionplots(Bind):
    #~Display
    print('==================================')
    print('Following are your ORIGINAL PLOTS:')
    print('==================================')
    print('      X      --|-->  Y\' = f(X) ')
    print('--------------------------------')
    for itemsx, itemsy in sorted(Bind.items()):
        print('  ',round(itemsx,6),'   --->  ',round(itemsy,6))
    

#TODO: Displays Correlation coefficient "R"
def CoffR(X,Y):
    Corr = Calc.R(X,Y)
    #~Display
    print('==============================================')
    print("Following is your Correlation Coefficient (R):")
    print('==============================================')
    print("    R = ",round(Corr,6))
    if Corr > 0:
        if Corr <= 0.25:
            print("\nValue of R shows NEGLIGIBLE strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr > 0.25 and Corr <= 0.35:
            print("\nValue of R shows WEAK strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr > 0.35 and Corr <= 0.49:
            print("\nValue of R shows MODERATE strength of relationship \nbetween the Regression line and Original Plots.\nBut more inclined towards WEAKNESS")
        elif Corr > 0.49 and Corr <= 0.51:
            print("\nValue of R shows MODERATE strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr > 0.51 and Corr <= 0.65:
            print("\nValue of R shows MODERATE strength of relationship \nbetween the Regression line and Original Plots.\nBut more inclined towards STRENGTH")
        elif Corr > 0.65 and Corr <= 0.8:
            print("\nValue of R shows STRONG strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr > 0.8 and Corr <= 0.96:
            print("\nValue of R shows VERY STRONG strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr > 0.96 and Corr <= 0.99:
            print("\nValue of R shows VERY STRONG strength of relationship \nbetween the Regression line and Original Plots.\nIt is almost touching +100%")
        elif Corr > 0.99 and Corr <= 1:
            print("\nValue of R shows COMPLETE strength of relationship \nbetween the Regression line and Original Plots. It is approximately +100%")
        print("The direction of linear relationship is POSITIVE(+)")
    elif Corr == 0 :
        print("\nValue of R shows NO strength of relationship \nbetween the Regression line and Original Plots.")
        print("There is NO direction for this relationship")
        print("Perhaps re-evaluation on the user\'s side may help...")
    elif Corr < 0:
        if Corr >= -0.25:
            print("\nValue of R shows NEGLIGIBLE strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr < -0.25 and Corr >= -0.35:
            print("\nValue of R shows WEAK strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr < -0.35 and Corr >= -0.49:
            print("\nValue of R shows MODERATE strength of relationship \nbetween the Regression line and Original Plots.\nBut more inclined towards WEAKNESS")
        elif Corr < -0.49 and Corr >= -0.51:
            print("\nValue of R shows MODERATE strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr < -0.51 and Corr >= -0.65:
            print("\nValue of R shows MODERATE strength of relationship \nbetween the Regression line and Original Plots.\nBut more inclined towards STRENGTH")
        elif Corr < -0.65 and Corr >= -0.8:
            print("\nValue of R shows STRONG strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr < -0.8 and Corr >= -0.96:
            print("\nValue of R shows VERY STRONG strength of relationship \nbetween the Regression line and Original Plots.")
        elif Corr < -0.96 and Corr >= -0.99:
            print("\nValue of R shows VERY STRONG strength of relationship \nbetween the Regression line and Original Plots.\nIt is almost touching -100%")
        elif Corr < -0.99 and Corr >= -1:
            print("\nValue of R shows COMPLETE strength of relationship \nbetween the Regression line and Original Plots. It is approximately -100%")
        print("The direction of linear relationship is NEGATIVE(-)")
    

#TODO: Displays Coefficient of Determination "R-square"
def CoffR2(X,Y):
    Coff = (Calc.R(X,Y))**2
    #~Display
    print('====================================================')
    print("Following is your Correlation Coefficient (R-Square):")
    print('====================================================')
    print("    R^2 = ",round(Coff,6),"  --->  ",round(Coff*100,6),"%")
    if Coff > 0:
        if Coff <= 0.25:
            print("\nValue of R-square shows NEGLIGIBLE strength of prediction \non the Regression line towards Original Plots.")
        elif Coff > 0.25 and Coff <= 0.35:
            print("\nValue of R-square shows WEAK strength of prediction \non the Regression line towards Original Plots.")
        elif Coff > 0.35 and Coff <= 0.49:
            print("\nValue of R-square shows MODERATE strength of prediction \non the Regression line towards Original Plots.\nBut more inclined towards less predicted outputs")
        elif Coff > 0.49 and Coff <= 0.51:
            print("\nValue of R-square shows MODERATE strength of prediction \non the Regression line towards Original Plots.")
        elif Coff > 0.51 and Coff <= 0.65:
            print("\nValue of R-square shows MODERATE strength of prediction \non the Regression line towards Original Plots.\nBut more inclined towards more predicted outputs")
        elif Coff > 0.65 and Coff <= 0.8:
            print("\nValue of R-square shows STRONG strength of prediction \non the Regression line towards Original Plots.")
        elif Coff > 0.8 and Coff <= 0.96:
            print("\nValue of R-square shows VERY STRONG strength of prediction \non the Regression line towards Original Plots.")
        elif Coff > 0.96 and Coff <= 0.99:
            print("\nValue of R-square shows VERY STRONG strength of prediction \non the Regression line towards Original Plots.\nIt is almost touching +100%")
        elif Coff > 0.99 and Coff <= 1:
            print("\nValue of R-square shows COMPLETE strength of prediction \non the Regression line towards Original Plots. It is approximately +100%")
    elif Coff == 0 :
        print("\nValue of R-square shows NO strength of prediction \non the Regression line towards Original Plots.")
        print("Perhaps re-evaluation on the user\'s side may help...")    
    
#TODO: Displays Error analysis
def SumSqErr(X,Y):
    SSE = Calc.SSE(X,Y)
    SST = Calc.SST(Y)
    SSR = Calc.SSR(X,Y)
    #~Display
    print("============================================================")
    print("Following is the Error analysis of regression line generated")
    print("============================================================")
    print("Summation of squared Total:      ",SST)
    print("Summation of squared Error:      ",SSE)
    print("Summation of squared Regression: ",SSR)
    print("Verification...\n    ",round(SST,6)," = ",round(SSR,6)," + ",round(SSE,6),"\n     SST     =     SSR     +     SSE")
    if SSE > SSR:
        print("\nError seems to be less than the probability of prediction")
    elif SSR < SSE:
        print("\nError seems to be more than the probability of prediction")
    if round(SST,3) != round(SSR+SSE,3):
        print("Seems like I was unable to calculate the true equation. Tell my creator he will be able to help\n Im sure of it! He is a very kind person. He'll listen to you.")
    if round(SST,3) == round(SSR+SSE,3):
        print("True Equation found!")
    
    
    
    