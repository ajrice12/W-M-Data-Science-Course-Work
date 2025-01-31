
def process_text(text, punct = '.,;:"?!.'): #do not change def line
    text = text.replace('#',' #')#For these two lines, i used the replace method so that words with # or @ in front of them are properly added to the list
    text = text.replace('@', " @")
    text = text.translate(text.maketrans('','',punct)).split()#here is where i translate the input so that it removes all the variables from punct and then tokenizes them to make it into a list
    return(text)
   
def get_features(text_list, feature): #do not change def line
    #debug the line below - you must leave it as list comprehension
    return [item for item in text_list if feature in item]


def feature_extract(filename, feature = '#'): #do not change def line
    with open(filename,'r', encoding = 'UTF8') as data:#here i open the file and set it to read so it can take in the data
        text = data.read()# then it turns the data into a variable
        word = process_text(text)#here it used the first function to convert the text variable into a list
        word_2 = get_features(word, feature)#then i call the 2nd function so that it properly makes a list of the words with #s and @s
        #print(word_2)
        result = {}#empty dict
        #print(result)
        for item in word_2:#here, i made a for loop to the dictionary to add key value pairs to the dictionary and increment the values if there are several of the same key
            if item not in result:
                result[item] = 1
            else:
                result[item] = result[item]+1
    return(result)#then it returns the dictionary to the main
