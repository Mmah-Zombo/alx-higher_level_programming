def main():
    # Assign values to variables a and b
    a = 1
    b = 2
    
    # Import the add function from the add_0 module
    from add_0 import add
    
    # Print the result of the addition using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()
