import string
import inspect

word_list = ["hello!", "my.", "name,", "is", "james!"]

def remove_punctuation1(word_list):
  
  for i in range(len(word_list)):
    word_list[i] = word_list[i].translate(str.maketrans("", "", string.punctuation)) 

  print(word_list)

#remove_punctuation1(word_list)

frequency_data = "this is a to list that a to is like to a make"

def get_frequency(frequency_data):
  word_list = frequency_data.split()
  
  frequency = {}
  
  for word in word_list:
    if word not in frequency:
      frequency[word] = 1
    else:
      frequency[word] += 1
  
  return frequency

#print(get_frequency(frequency_data))

def is_result_even(num_a, num_b):
  if (num_a * num_b) % 2 == 0:
    return True
  
  return False
 
#print(is_result_even(2, 3))

number_list = [1, 2, 3, 4, 5, 6, 8]

def remove_last_n_numbers(number_list, n):
  result = number_list[: len(number_list) - n]
  
  return result

#print(remove_last_n_numbers(number_list, 3))

def is_equal(a, b):
  return a == b

equality_list = ["7, 7", "1, 1", "12, 12", "1, 2", "3, 3", "4, 4"]

def check_equality(equality_list: list):
  i = 0
  
  while i < len(equality_list):
    items_list = equality_list[i].split(", ")   
    print(is_equal(int(items_list[0]), int(items_list[1])))
    
    i +=1

#check_equality(equality_list)

def continue_while_equal(equality_list):
  # should stop processesing at the first unequal element
  equal = True
  
  for element in equality_list:
    number_list = element.split(", ")
    print(number_list)
    equal = is_equal(number_list[0], number_list[1])
    if not equal:
      break

#continue_while_equal(equality_list)

lines = [
    "hello",
    "is",
    "it",
    "me",
    "your",
    "looking for"
  ]

def summary_lines(lines: list) -> str:
  # turns a list into text. " ".join() will create a readable stream.
  # "\n".join() will create a readable list
  return "\n".join(lines)

#print(summary_lines(lines))

def add_value(number_list: list, value: int):
  
  # for i in range(0, len(number_list)):
  #   number_list[i] += value

  for i, element in enumerate(number_list):
    if element == 5 or element == 3:
      number_list[i] += value
        
  return number_list

# print(add_value([1, 5, 17, 3, 99], 100))

def negs_to_pos(number_list):
  for i, element in enumerate(number_list):
    if element < 0:
      number_list[i] = abs(element) 
  
  return number_list

#print(negs_to_pos([-1, 2, -3, -4, 5, 6, -7]))

#print(6 // 2) 

def error_test():
  try:
    
    x = 1 / 0
  
  except Exception as e:
    print(f"Exception: {e} occured in {inspect.stack()[0][3]}()")

#error_test()


mystring = "283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796"

def count_4(mystring):
  count = 0
  for i in range(0, len(mystring)):
    if mystring[i] == "4":
      count += 1
      
  print(count)


count_4(mystring)
 
  