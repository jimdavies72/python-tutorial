# simple_encoder_decoder.py

# pip install num2words
from num2words import num2words
# string manipulation methods
import string as s
# reg-ex methods
import re
#system methods
import sys

# app to create coded messages and then decode them
# this is a simple app so only characters will be encoded:
# numbers must be converted to words e.g. 36 -> thirty six
# punctuation must be removed.
# characters converted to hex (base-16).
# decode messages will not contain spaces as these will have been removed.

#test_input_string = "Hello agent-47, this is your mission No. 11."

def numbers_to_words(string: str):
  # find all occurances of numbers
  numbers = re.findall(r'\d+', string)
  
  for number in numbers:
    string = string.replace(str(number), num2words(number))
  
  return string

def remove_punctuation(string: str):
  # replace hyphens with spaces
  string = string.replace("-", " ")

  # remove all other punctuation
  for char in string:
    if char in s.punctuation:
      string = string.replace(char, "")

  # remove all spaces
  string = string.replace(" ", "")
  
  return string

def convert_to_hex(string: str):
  hex_string = ""
  
  for char in string:
    hex_string = hex_string + hex(ord(char))[2:] + " "
  
  return hex_string

def string_to_list(string) -> list:
  return list(string.split(" "))

def hex_to_char(list) -> list:
  ord_list = []
  
  for item in list:
    ord_list.append(chr(int(item, 16)))
  
  return ord_list

def code_message(input_string) -> str:
  # convert numbers to words first as these may contain hyphens
    words = numbers_to_words(input_string)
    clean_string = remove_punctuation(words)
    return convert_to_hex(clean_string)

def decode_message(input_string) -> str:
  coded_list = string_to_list(input_string)
  char_list = hex_to_char(coded_list)
  return "".join(char_list)

def main(input_string: str, code: str):
  if code == "code":
    print(f"Code: {code_message(input_string)}")
    
  elif code == "decode":
    print(f"Decoded: {decode_message(input_string)}")
    
  else:
    print("You must enter 'code' or 'decode' as the second argument")
 
run_state = False  

if len(sys.argv) > 2:
  if len(sys.argv[1]) >= 1:
    message = sys.argv[1]
    run_state = True
  else: 
    print("You must supply a message")
  code = sys.argv[2]
else:
  print("You must supply 2 arguments: <message> <code type>")

if run_state:
  main(message, code) # accepts argument supplied from the command line