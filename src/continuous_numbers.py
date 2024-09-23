# continuous_numbers.py

# from a list of numbers, how many numbers are needed to create a continues
# sequence of numbers?

input_list = [6, 3, 9, "a", 14, None, 4, 6, 9, 10, 11]

# expected
# [3, 4, 6, 9, 10, 11, 14]
# 14 - 3 = 11
# 7 - 1 = 6
# 11 - 6 = 5

# 1. Clear the list of junk data
# 2. Remove duplicates
# 3. identify highest and lowest numbers in list : get highest - lowest.
# 4. get number of list elements - 1
# 5. result from 3. - result from 4 gives number of values required.

def clear_junk(list) -> list:
  for item in list:
    if type(item) != int:
      list.remove(item)
  
  return list

def remove_duplicates(dupe_list) -> list:
  print(list(dict.fromkeys(dupe_list)))
  
  return(list(dict.fromkeys(dupe_list)))

def get_bounds_diff(unsorted_list) -> int:
  sorted_list = unsorted_list.copy()
  sorted_list.sort()
  
  return sorted_list[-1] - sorted_list[0]
    

def main(input_list: list) -> None:
  clean_list = remove_duplicates(clear_junk(input_list))
  exclusive_elements = len(clean_list) - 1
  
  print(f"Number of elements needed: {get_bounds_diff(clean_list) - exclusive_elements}")
  

#main(input_list)

