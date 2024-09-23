from collections import Counter

# === Dictionaries ===

# my_dictionary = {
#   "String": "A sequence of characters",
#   "List": "A sequence of any item",
#   "Dictionary": "An object of key value pairs"
# }

# print("A String is:")
# print("  " + my_dictionary["String"])

# print("A List is:")
# print("  " + my_dictionary["List"])

# print("A Dictionary is:")
# print(" " + my_dictionary["Dictionary"])


# text = "the quick brush jumped over the lazy crab"
# letter_counts = {}

# for letter in text:
#   if letter not in letter_counts:
#     letter_counts[letter] = 1
#   else:
#     letter_counts[letter] = letter_counts[letter] + 1

# print(letter_counts)


# def count_words_by_length(words):
#   word_counts = {}
#   for word in words:
#     if len(word) not in word_counts:
#       word_counts[len(word)] = 1
#     else:
#       word_counts[len(word)] = word_counts[len(word)] + 1 

#   return word_counts

# print(count_words_by_length(["hat", "cat", "I", "bird"]))


# # Using Counter()
# counter = Counter(["a", "b", "c", "a", "b", "b"])
# print(counter)

# counter = Counter(a=3, b=4, c=2)
# print(counter)


# def get_person_by_name(list, name):
#   return next((item for item in list if item["name"] == name), {})

# my_dict_list = [
#   {
#     "name": "James",
#     "age": 21,
#     "city": "London"
#   },
#   {
#     "name": "Harriet",
#     "age": 25,
#     "city": "Paris"
#   },
#   {
#     "name": "Bill",
#     "age": 51,
#     "city": "New York"
#   }
# ]

# print(get_person_by_name(my_dict_list, "Harriet"))


# your_list = [
#   {"name": "James", "age": 21}, 
#   {"name": "Harriet", "age": 25}, 
#   {"name": "Bill", "age": 51},
#   {"name": "Susan", "age": 30}
# ]

# def count_people_by_age(people_list):
#   age_counts = {}
#   for person in people_list:
#     if person["age"] not in age_counts:
#       age_counts[person["age"]] = 1
#     else:
#       age_counts[person["age"]] = age_counts[person["age"]] + 1
#   return age_counts

# print(count_people_by_age(your_list))