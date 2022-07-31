def reverse_integer(n):
  y = str(abs(n))
  y = y.strip()
  y = y[::-1]
  y = int(y)
  if n >= 2** 31 -1 or n <= -2** 31:
    return ("overflow")
  elif n < 0:
    return (-1 * y)
  else:
    return (y)
if __name__ == "__main__":
  to_rev = int(input("Input an integer [123456]: ") or 123456) 
  reversed = reverse_integer(to_rev)
  print (reversed)