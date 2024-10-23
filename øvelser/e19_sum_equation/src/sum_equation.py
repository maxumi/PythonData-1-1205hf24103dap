#!/usr/bin/env python3

def sum_equation(L: list):
    if not L:
        return "0 = 0"

    rtn_str = ""
    for i in range(len(L)):
        if i == len(L) - 1:
            rtn_str += f"{L[i]} = "
        else:
            rtn_str += f"{L[i]} + "
    
    sumNumb = sum(L)
    rtn_str += f"{sumNumb}"
    return rtn_str

def main():
    print(sum_equation([1,5,20,20,5]))
    pass

if __name__ == "__main__":
    main()
