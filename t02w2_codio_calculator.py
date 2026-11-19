def get_iterations():
  iterations = int(input('How many calculations do you want to do?'))
  return iterations

def get_user_input():
  user_input = input('What do you want to calculate?')
  for symbol in operations:
    if symbol in user_input:
      left, right = user_input.split(symbol)
      a = int(left)
      b = int(right)
      operator = symbol
      return a, b, operator

def addition(a, b):
  return a + b, None

def subtraction(a, b):
  return a - b, None

def multiplication(a, b):
  return a * b, None

def division(a, b):
  return a / b, None

def divide_with_remainder(a, b):
  integer_division = a // b
  remainder = a % b
  return integer_division, remainder

operations = { #seemed like a good time to use a dict instead of long if/elif chains
  "+" : addition,
  "-" : subtraction,
  "*" : multiplication,
  "/" : division,
  "~" : divide_with_remainder,
}

def main():
  print("Welcome to the Python calculator!")
  iterations = get_iterations()
  for iteration in range(iterations):
    a, b, operator = get_user_input()
    if operator in operations:
      chosen_operation = operations[operator]
      result, remainder = (chosen_operation(a, b))
    print(f"The answer is {result}")
    if remainder:
      print('The remainder is ', remainder)

if __name__ == "__main__":
  main()