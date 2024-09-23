
from helper_functions import box_text

# i = 0 # We call this the counter variable
# while i < 10:
#   print(box_text(f"The number is now {i + 1}"))
#   i += 1


# def add_cats_repeatedly(word_list, count):
#   i = 0
#   while i < count:
#     word_list.append("cats")
#     i += 1
    
#   return word_list

# animals = add_cats_repeatedly(["dogs", "birds"], 3)
# for animal in animals:
#   print(animal)


# for letter in ["a", "b", "c", "d"]:
#  print(letter)

# for number in range(0, 10):
#   print(number)


# x = range(6)
# for number in x:
#   print(number)



# == Summarising ==

# lines = [
#   "My King,",
#   "I need another five years.",
#   "Then your crab will be ready.",
#   "Sincerely,",
#   "Chuang-tzu"
# ]

# text = "\n".join(lines)
# print(text)

# text = ""
# for line in lines:
#   text += line + "\n"
  
# print(text)


# def add_up_numbers(numbers_list):
#   total = 0
#   for number in numbers_list:
#     total += number
#   return total

# print(add_up_numbers([1, 2, 3, 4, 5, 6]))

# print(sum([1, 2, 3, 4, 5, 6, 7]))


# == Mapping ==

"""
words = ['I', 'need', 'another', 'five', 'years']

first_letters = [] # This is our accumulator again

for word in words: # We go through each word
  first_letter = word[0] # Get the first letter
  # And append it to our accumulator list:
  first_letters.append(first_letter)

print(words)
print(first_letters)
"""

# def add_one_hundred_to_numbers(numbers):
#   for number in numbers:
#     numbers[number - 1] += 100

#   return numbers

# print(add_one_hundred_to_numbers([1, 2, 3, 4, 5]))


# def add_one_hundred_to_numbers(numbers):
#   for number in range(0, len(numbers)):
#     numbers[number] += 100

#   return numbers

# print(add_one_hundred_to_numbers([1, 2, 3, 4, 5]))


# def get_names(people_list):
#   ages = []
#   for person in people_list:
#     ages.append(person["name"])
#   return ages

your_list = [{"name": "James", "age": 21}, {"name": "Harriet", "age": 25}, {"name": "Bill", "age": 51}]

# print(get_names(your_list))



# === Filtering ===


def get_under_ages(people_list):
  under_age_list = []
  for person in people_list:
    if person["age"] < 30:
      under_age_list.append(person)
  return under_age_list

print(get_under_ages(your_list))