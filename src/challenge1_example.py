import inspect
# consts
RED = '\033[1;31m'
GREEN = '\033[1;32m'
NC = '\033[0m'

# * Gets rid of junk data
# * Converts negative integers to positive numbers
# * Creates a graph of how frequently each number shows up

def negs_to_pos(numbers: int) -> list:
  try:
    pos_data = []
    
    for number in numbers:
      if number < 0:
        number = -number 
              
      pos_data.append(number)
    
    return pos_data

  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")
    
def clear_junk(data) -> list:
  try:
    for x in data:
      if type(x) != int:
        data.remove(x)
    return data 
  
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")
    
def create_data_frequency(data) -> dict:
  try:
    graph = {}

    for x in data:
      if x not in graph:
        graph[x] = 1
      else:
        graph[x] += 1
      
    return graph 
  
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}") 

def generate_graph(data) -> str:
  try:
    graph=""
    for x in data:
      graph += f"{x}: { "X" * data[x]}\n"
     
    return graph 
   
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")

def main(data) -> None:
  try:
    # print(f"Input Data: {data}")
    cleaned_data = negs_to_pos(clear_junk(data))
    # print(f"Cleaned Data: {cleaned_data}") 
    frequency_data = create_data_frequency(cleaned_data)
    # print(f"Frequency Data: {frequency_data}")
    
    print(f"{RED}Frequncy Data:")
    print(f"______________{NC}")
    graph = generate_graph(frequency_data)
    print(f"{GREEN}{graph}{NC}")
    
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")  
  

# represents data that may have been returned from an ETL job for example
input_data = [1, 2, 3, 5, None, -4, -3, None, -2, -1, 1, -1]
main(input_data)
  