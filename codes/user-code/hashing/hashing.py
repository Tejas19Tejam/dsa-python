
# Hashing
ar = [1,2,3,2,7, 4, 2, 6, 7, 4, 3,10, 11, 2, 5, 6]
    
def main(ar, k):
    hashTable = [0] * 13
    
    for key in range(0, len(ar)):
        hashTable[ar[key]] = hashTable[ar[key]]+1
    
    print(f'The number {k} appears in array for {hashTable[k]} times')
    

if __name__ == "__main__":
    main(ar, 3)
    main(ar, 4)
    main(ar, 2)


