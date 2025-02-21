def menu(**kwargs):
    while True:
        option_string = " or ".join(kwargs.keys())
        choice = input(f'Enter an option: {option_string} : ')
        if choice in kwargs.keys():
            return kwargs[choice]()

        print("Error: Not a valid option")

