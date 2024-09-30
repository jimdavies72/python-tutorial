# Python - Basic Tutorial

This is the work I undertook as a result of a short online 'introduction to Python' course that I did as part of a job application process. Its a bit of a mixed bag of stuff and I have tried to explain what there is here:

- challenge1_example.py

  creates a graph of the frequency of integers found in a list. none integers a removed and negative integers are converted to their positive counterparts.
- challenge1_exercise.py

  takes a list of words as input and extracts all words that are 15 characters or more in length. These words are then truncated to 15 chars and concatonated with "...".
- continuous_numbers.py

  takes a list of unsorted integers (and other junk to be removed) and establishes how many numbers would be needed to create a continuous list between its lowest and highest integers: e.g. \[5, 8, 3, 9, 2\] -&gt; answer is 3.
- continuous_numbers_v2.py 

  same as continuous_numbers.py (above) except refactored to perfrom this in a much more efficient way.
- dictionaries.py

  introduction to python dictionary data-structure.
- errors.py

  introduction to basic exception handling.
- list_modification.py

  introduction to the python list data-structure.
- list_to_json_output.py

  program that accepts 2 lists: list a represents column header from a spreadsheet, list b represents the data that fits the columns in list a. the program takes these lists and converts them to JSON objects and outputs them to a file.
- loops.py

  introduction to while and for loops
- simple_encoder_decoder.py

  a program that takes a message as input and converts this message into hex characters and outputs the stream to the terminal. The program removes punctuation and converts numbers to their word representations (e.g. 37 -&gt; Thirty-Seven) using the num2word python package.

  This hex stream can them be used as an input back into the program to be converted back into readable ASCII.
- word_frequency.py
- takes a string of words and outputs the frequency of each of the words used. punctuation ins removed and the words are converted into padded fixed length strings to create a more readable output on screeen.
