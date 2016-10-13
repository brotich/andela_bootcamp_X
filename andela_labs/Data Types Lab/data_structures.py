
def data_type(var):

  """
    Compare and return results, based on the 
    argument supplied to the function.
  """
  if type(var) == str:
    return len(var)
  elif var == None:
    return 'no value'
  elif type(var) == bool:
    return var
  elif type(var) == int:
    if var < 100:
      return "less than 100"
    elif var > 100:
      return "more than 100"
    elif var == 100:
      return "equal to 100"
  elif type(var) == list:
    if len(var) >= 3:
      return var[2]
    else:
      return None
