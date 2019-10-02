#ngram_Chinese.py

#This program can be used to identify nGrams in Chinese texts.
#(Most nGram programs do not work with Chinese because there no spaces between
# words.)

import re, os

def ngram_search(length, string):
    """This searches for and counts ngrams of a given length in a string."""
    char_list = list(string) #Break string into list of characters 
    base_index = 0 #Initialize
    end_index = length + base_index
    ngrams = {}
    for i in char_list [0:len(char_list) - length]:
        char_slice = slice(base_index, end_index)#ngrams are slices of char_list
        base_index, end_index = base_index + 1, end_index + 1 #Increment index
        ngram = ''.join(char_list[char_slice]) #Use slice as ngram
        ngrams.setdefault(ngram, 0) #Initial new ngrams at 0
        ngrams[ngram] = ngrams[ngram] + 1 #Increment ngram count by one 
    return ngrams

def avoid_low_values (d, min_val):
    """Loops over dict, returns a new dict without values below a threshold."""
    """Assumes values are integers, such as counts in ngram dictionary."""
    new_dict = {}
    for k in d:
        if d.get(k, 0)>= min_val:
            new_dict[k] = d[k]
    return new_dict

def avoid_non_Hanzi(string):
    """Removes all chars except Chinese characters from str.
    Requires import re"""
    new_string = re.sub(r'[^\u4E00-\u9FA5]','', string)
    return new_string        

#Get the file from the user to supply a string
file_location = input('Input your file location:  ')
while os.path.isfile(file_location)==False:
    file_location = input('Carefully check and re-enter the full path for your file:  ')
input_file = open(file_location, encoding='utf-8')
string = input_file.read()
input_file.close()
string = avoid_non_Hanzi(string)

#Set length.  Run ngram search
length = int(input('Enter the length of ngrams to search for using numeric keys:  '))
ngrams = ngram_search(length, string)

#Set minimum number of occurences to include in spreadsheet.
min_val = int(input('Enter the lowest number of occurences to record:  '))
ngrams = avoid_low_values(ngrams, min_val)

#Create a CSV file to store the data.
#Extract the fileName from the file_location.
base_name = os.path.basename(file_location)
#Returns file name with extension.
split_base_name = os.path.splitext(base_name)
#Returns a tuple with the file name and extension
new_file_name = split_base_name[0]
folder = os.path.dirname(file_location)
new_file_path = os.path.join(folder, new_file_name + '_N' + str(length) +'_MIN_' + str(min_val)  + '.csv')
output_file = open(new_file_path, 'w', encoding = 'utf-8')

#Write each key-value pair in ngrams as a comma-separated pair.
for k in ngrams:
    output_file.write(k + ', ' + str(ngrams[k]) + '\n')
output_file.close()
print('Results saved as ' + str(new_file_path))

