

def square(x):
    return x**2


def main():
    for i in range(10):
        print(i)


# If we write this if statement, the main funciton will only execute when we run this file
# This line of code is addedd if this file is supposed to be imported by another file to use its function
if __name__ == '__main__':
    main()
