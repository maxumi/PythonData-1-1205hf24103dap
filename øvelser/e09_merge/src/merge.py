#!/usr/bin/env python3

def merge(L1: list, L2: list):
    l = []
    l1, l2 = 0, 0 # for case where the two lists are not the exact length
    
    # Run while both are are not finished
    while l1 < len(L1) and l2 < len(L2):
        if L1[l1] <= L2[l2]:
            l.append(L1[l1])
            l1 += 1
        else:
            l.append(L2[l2])
            l2 += 1

    # If L1 is not finished then add remaining
    while l1 < len(L1):
        l.append(L1[l1])
        l1 +=1 # update until its up to length

    # If L2 is not finished then add remaining
    while l2 < len(L2):
        l.append(L2[l2])
        l2 +=1 # update until its up to length
    
    return l

def main():
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    result = merge(L1, L2)
    print("Merged list:", result)

if __name__ == "__main__":
    main()
