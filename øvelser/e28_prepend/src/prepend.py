#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, string:str):
        self.start_string = string

    def write(self,string:str):
        print(self.start_string+string)
    
    # Add the methods of the class here
def main():
    prepend = Prepend("+++ ")
    prepend.write("Hello")
    pass

if __name__ == "__main__":
    main()
