  if ((n == 0) or (n == 1)):
    return 1
  else:
    return n * fact_rec(n - 1)


number = int(input("enter the Value:"))
res = fact_rec(number)
print("The Factorial of {} is {}.".format(number, res))
