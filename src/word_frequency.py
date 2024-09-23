# word_frequency.py
import string

# return the frequency of words used in a given passage.
# numbers and words containing hyphens (-) are not included.
# punctuation mut also be removed - " , . : ; !
# display frequency data in a graph

words = "Mary-Berry has to taken 6 humble to ingredients and elevated them to and create this and hearty, vegetarian cheesy pie! Topped feels with golden puff pastry that feels like a real treat."

# 1. clear junk 
# 2. create word frequency dictionary
# 3. print out data in graph


def remove_punctuation(words_list):
  for i in range(len(words_list)):
    words_list[i] = words_list[i].translate(str.maketrans('', '', string.punctuation))
    
  return words_list

def clear_junk(words: str) -> list:
  # create list from words
  word_list = list(words.split(" "))
  
  for word in word_list:
    if "-" in word:
      word_list.remove(word)
    elif word.isnumeric():
      word_list.remove(word)
  
  return word_list

def word_frequency(words_list) -> dict:
  word_count ={}
  
  for word in words_list:
    if word not in word_count:
      word_count[word] = 1
    else:
      word_count[word] += 1
  
  return word_count

def pad_word(word, to_length):
  pad = to_length - len(word)
  word = word + (" " * pad)
  
  return word

def display(frequency_data, max_length): 
  
  display = ""
  for item in frequency_data:
    display += f"{pad_word(item, max_length)}: {"X" * frequency_data[item]} ({frequency_data[item]})\n"
  
  return display

def main(words):
  clean_words = remove_punctuation(clear_junk(words))
  max_length = len(max(clean_words, key=len)) + 1 # include " "
  
  frequency = word_frequency(clean_words)
  #print(frequency)
  print(display(frequency, max_length))


main(words)