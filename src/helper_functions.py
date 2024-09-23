RED = '\033[1;31m'
GREEN = '\033[1;32m'
NC = '\033[0m'

def box_text(text):
  long_edge = "*" * (len(text) + 4)
  string = f"{GREEN}{long_edge} \n* {RED}{text} {GREEN}*\n{long_edge}{NC}"
  
  return string
  
# print(box_text("Just another day on the beach"))