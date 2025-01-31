from Project_3 import *


#Create and print a dictionary containing all of the hashtags from the Tortoise data set. Be sure to assign a variable name to this dictionary.
Dictionary_1 = feature_extract("tortoise_tweets.txt", feature = "#")#dictionary 1 that collects allthe hashtags for the tortoise set
#print(Dictionary_1)
#Create and print a dictionary containing all of the hashtags from the Umbrella data set. Be sure to assign a variable name to the dictionary.
Dictionary_2 = feature_extract("umbrella_tweets.txt", feature = "#")#dictionary 2 that collects all the hashtags for the umbrella set
#print(Dictionary_2)
#Create and print a dictionary containing all of the mentions from the Tortoise data set. Be sure to assign a variable name to this dictionary.
Dictionary_3 = feature_extract('tortoise_tweets.txt', feature = "@")#dictionary 3 that collects all the mentions for the tortoise set
#print(Dictionary_3)
#Create and print a dictionary containing all of the mentions from the Umbrella data set. Be sure to assign a variable name to the dictionary.
Dictionary_4 = feature_extract('umbrella_tweets.txt', feature = "@")#dictionary 4 that collects all the mentions for the umbrella set
#print(Dictionary_4)
#Find and print all of the mentions that are shared by the two data sets (i.e. the mentions that can be found in both). Print these out.
D3_set = set(Dictionary_3)#Here i turn the dictionaries into sets so that I could use the intersection method but could not figure out why it would print set()
D4_set = set(Dictionary_4)
shared = D3_set.intersection(D4_set)
print(shared)
#Find all of the hashtags that are in the Tortoise data set but not the Umbrella data set. Print these out.
D1_set = set(Dictionary_1)#Here i made a two more sets so that i could get the difference between the two data sets
D2_set = set(Dictionary_2)
print(D1_set.difference(D2_set))#then i print them out here