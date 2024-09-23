
your_list = [{"name": "James", "age": 21}, {"name": "Harriet", "age": 25}, {"name": "Bill", "age": 51}]
# print(next(item for item in your_list if item["age"] == 51))


# my_list = ["d", "c","a", "b", "c"]
# my_list.append("d")
# my_list.reverse()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)
# print(my_list.count("c"))


#your_list.append({"name": "Susan", "age": 30})
#print(your_list)

"""  
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)
print(list2)
list3 = list1.copy()
list3.append(5)
print("-----")
print(list1)
print(list3)
"""

"""
def remove_item_from_list(the_list, item):
  # ...
  the_list.remove(item)
  return the_list

print(remove_item_from_list([1, 2, 3], 2))  
"""

"""
def count_items_in_list(the_list, item):
  return the_list.count(item)

print(count_items_in_list([1, 2, 3, 2, 1, 2], 2))
"""

"""
def get_index_of_item(the_list, item):
  return the_list.index(item)

print(get_index_of_item([1, 2, 3, 2, 1, 2], 3))
"""

"""
def get_indices(element, lst):
  indices = []
  for i in range(len(lst)):
    if lst[i] == element:
      indices.append(i)
  return indices

my_list = [3, 5, 2, 3, 8, 3, 1]
element = 3
indices = get_indices(element, my_list)

print(indices)
"""

# def reverse_list(the_list):
#   list_copy = list(reversed(the_list))
#   print(list_copy)
#   return the_list

# print(reverse_list([1, 2, 3]))