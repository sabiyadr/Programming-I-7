def main():
  weight = int(input("Enter Package Weight in Kilograms: "))
  length = int(input("Enter Package Length in Centimeters: "))
  width = int(input("Enter Package Width in Centimeters: "))
  height = int(input("Enter Package Height in Centimeters: "))
  cubicmeters = length * 0.01 * width * 0.01 * height * 0.01

  if cubicmeters > 0.1:
    print("Package is Too Large")
  if weight > 27:
    print("Package is Too Heavy")

  pass

if __name__ == "__main__":
  main()
