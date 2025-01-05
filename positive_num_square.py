def check(n):
    if __name__ == '__main__':
      for i in range (n):
        print(i**2)

pinput=input("Enter:").strip()

if pinput.isdigit():
   n=int(pinput)
   check(n)
else:
   print("enter a positive integer")   