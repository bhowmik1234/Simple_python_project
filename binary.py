L = [4,2,6,11,12,89,21,3]
L = sorted(L)
num = int(input("Enter the search Number: "))

low = 0
high = len(L) - 1


while(low<=high):
    mid = int((low+high)/2)
    if(L[mid] == num):
        print(f"found at index: {mid}")
        break
    elif (L[mid] > num):
        high = mid - 1
    elif (L[mid] < num):
        low = mid + 1

if(low > high):
    print(f"{num} not found")