def weight_on_planets():
   # write your code here
   eweight = int(input("What do you weigh on earth? "))
   mweight = eweight * 0.38
   jweight = eweight * 2.34
   print(f"\nOn Mars you would weigh {mweight} pounds.\nOn Jupiter you would weigh {jweight} pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()