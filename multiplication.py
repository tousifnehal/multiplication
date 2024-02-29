# Importing Modules

import os

# Multiplication Function 

def mul():
    # Getting range From User
    range1= int(input("➡  Enter The First Range To Start The Multiplication \n"))
    range2 = int(input("➡  Enter The Last Range To Start The Multiplication \n"))
    
    if range2 < range1 :
        print("❌ Last Range Must Be Higher Than The First")
    # Range File Gen Loop 
    for x in range(range1, range2+1):
        # Multiplication For 0-10 Loop
        for i in range(11):
            # Name Of The File For Every Multiplication Value
            file = f"{x}.txt"
            # 1 * 1 = 1
            mul = x * i
            #Creating Files and Writing The Value  
            with open(file, "a") as filex:
                filex.write(f"{x} x {i} = {mul} \n")
            print(f"{x} x {i} = {mul}")
            # If Multiplication Value Done Break the loop and continue for next one
            if i == 10:
                print("-" * 10)
                break
            
# Folder Creation
          
filename = input("➡  Your File Name To Store The Multiplication Table \n")

# If Folder Exists

if os.path.exists(filename) == True :
    os.chdir(filename)
    print("⚠ The Path Already Exists ignoring the cretaion")
    mul() 
    print("✅ Operation Successful")    

# If Folder Doesn't Exist

else :
    os.makedirs(filename)
    os.chdir(filename)
    mul()
    print("✅ Operation Successful")             