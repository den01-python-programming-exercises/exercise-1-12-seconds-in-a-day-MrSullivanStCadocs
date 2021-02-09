def main():
    #write your code below this line
    number_in_days = int(input("How many days would you like to convert into seconds? "))
    number_in_seconds = (((number_in_days * 24) * 60) * 60)
    print(number_in_seconds)

if __name__ == '__main__':
    main()
