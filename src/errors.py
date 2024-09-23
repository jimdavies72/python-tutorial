import inspect

def this_should_fail() -> None:
  try:
    print(x)
    
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")
    

this_should_fail()