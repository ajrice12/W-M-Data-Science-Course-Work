import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Write your def lines and functions below
#The def lines you create must match the specifications exactly
#You cannot change the names of the functions, the variables, or the default arguments
#Expect a large grade penalty if your def lines are not correct
#This file should not contain any function calls or any code that is not part of a function definition
#This means any code unindented besides a def line or the import lines at the top
def make_subset(df, region = None, vaccine = None, year = None):
    # the objective of this function is to make a copy/subset of the data provided by the user, and return only the information
    s = df.copy()#makes a subset
    if region != None:#info the is info being given by the user
        s = s.loc[s['Region'].isin(region)]# create new subset presenting only info relating to region
    if vaccine != None:#info the is info being given by the user
        s = s.loc[s['Vaccine'].isin(vaccine)]#create new subset presenting only info relating to Vaccine
    if year != None:#info the is info being given by the user
        s = s.loc[s['Year'].isin(year)]#create new subset presenting only info relating to Year
    return s # return the new subset

def make_plot(series_object, title ='', bar = True):
    if bar == True:# if the graph is a bar
        plot = sns.barplot(x = series_object.values, y = series_object.index, orient = 'h')#sets up the info in a bar graph
        plt.title(title)#sets up the title
    else:# makes it a line plot
        plot = sns.lineplot(x = series_object.index, y = series_object.values)#sets up the info into a line plot
        plt.xticks(rotation = 90)#changes rotation
        plt.title(title)#sets up title
    return plot# returns graphs