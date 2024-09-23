import inspect
# consts
RED = '\033[1;31m'
GREEN = '\033[1;32m'
NC = '\033[0m'

def is_clear_of_hyphens(word) -> bool:
  try:
    if '-' in word:
      return False
    
    return True
    
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")

def get_long_words(words) -> list:
  try:
    clean_list = []
    for word in words:
      if len(word) > 10:
        if is_clear_of_hyphens(word):
          clean_list.append(word)
        
    return clean_list
  
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")

def shorten_words(words) -> list:
  try:
    short_list = []
    for word in words:
      if len(word) > 15:
        word = word[0:15] + "..."
      short_list.append(word)
        
    return short_list
  
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")
    
def create_output(list) -> str:
  try:
    
    output = ", ".join(list)
    
    return f"{RED}These words are quite long: {GREEN}{output}{NC}"
    
    
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")

def main(data) -> None:
  try:
    short_list = shorten_words(get_long_words(data))
    print(create_output(short_list))
    
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")  



data_list = [
  'hello',
  'nonbiological',
  'Kay',
  'this-is-a-long-word',
  'antidisestablishmentarianism'
]
main(data_list)