def checking_the_number(a, b):
  
  for i in range(10):
    if a == int(b):
      print("YOU WON!!\nit tooks only", i+1, "times")
      break
    else:
      print("Wrong!, You have ", 9-i, "times left.\n")
      b = input("Enter a number: ")
