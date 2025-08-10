def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")

    userDetails = [name,age,address]
    
    print(f"Name: {userDetails[0]}",f"\nAge: {userDetails[1]}",f"\nAddress: {userDetails[2]}")
    
    updateAge = int(input("\nEnter the number of years to add to your age: "))
    userDetails[1] += updateAge

    print ('New Info \n')
    print(f"Name: {userDetails[0]}",f"\nAge: {userDetails[1]}",f"\nAddress: {userDetails[2]}")
    

if __name__ == '__main__':
    main()