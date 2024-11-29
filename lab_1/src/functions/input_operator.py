from functions.check_operator import check_operator

def input_operator():
  operator = input("Введіть знак: ")
  operator = check_operator(operator)

  return operator