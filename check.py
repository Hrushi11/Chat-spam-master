try:
    import pynput
    print("module 'pynput' is installed")
except ModuleNotFoundError:
    print("module 'pynput' is not installed")
    # or
    install("pynput") # the install function from the question
