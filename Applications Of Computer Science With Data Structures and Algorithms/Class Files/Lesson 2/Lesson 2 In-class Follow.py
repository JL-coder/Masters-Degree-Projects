# This has to be the first function in our programs EVERYTIME
def main():
    a, b, c = 3, 4, 5

    print(a)
    print(b)
    print(c)

    #Double quote example
    print("\"")
    print("\"This is fun\"")
    #Tab example
    print("\t""This is being tabbed")
    #Beeb/bell sound Only works on command prompt when making noise. Can also go to terminal to do this.
    print("\a" "Beep Boom!")
    #Backslash example
    print("This is a backslash""\\")
    #Jumps to next line
    print("\n")

    boolean_variable = True
    interger_variable = 1
    floating_point_variable =  1.0
    complex_variable = 1 +1j
    print(type(boolean_variable))
    

if __name__ == "__main__":
    main()