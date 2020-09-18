========================================
AIM/Objective
========================================
This program aims to take relevant inputs in order to plot a Linear-regression using a character-based graph.

========================================
Program Specs
========================================
This program is writen in Python 3.7.7

========================================
Symbology
========================================
Original points will be shown by "X" symbol
Regression points will be shown by "@" symbol

========================================
Basic algorithm followed by the program
========================================
1-Input will be taken for observation range
2-List will be made for all "x" inputs
3-List will be made for all "y" inputs
4-User will be presented with the final table of both "x" and "y" values
5-Input will be taken for the scale "values" and "gaps"
6-A character-based graph will be shown to the user plotting the regression line and original values
7-User will be asked if they want to see additional information
8-If yes, Correlation coefficient and Coefficient of determination will be shown with comments.
  Also, The equation of SST=SSE+SSR will be shown

========================================
MODULE: Calculations
========================================
list of functions:
#Sxy(x,y)
#Sxx(x)
#a1(Sxx,Sxy)
#a0(x,y)
#y_Hat(x,y)
#axb(lst1,lst2)
#list_sum(lst)
#list_square(lst)
#list_mean(var)

EXTRA FUNCTIONS:
#R(x,y)
#SSE(x,y)
#SSR(x,y)  
#SST(y)