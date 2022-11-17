def main():
  eggs = int(input("Enter The Number of Eggs Purchased: "))
  numegg = eggs * 12
  priceperdozen = 0.0
  if numegg range(12: 48):
    priceperdozen = 0.50
  elif numegg range(48: 72):
    priceperdozen = 0.45
  elif numegg range(72: 132):
    priceperdozen = 0.40
  elif numegg >= 132:
    priceperdozen = 0.35
  else:
     print("Error!")

  print("Bill is: ", str(priceperdozen))

  pass

if __name__ == "__main__":
  main()
