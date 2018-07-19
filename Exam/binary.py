def bin_search(list, n, x):
    start = 0
    end = n - 1

    while (start <= end):
        mid = (start + end) / 2
        if (x == list[mid]):
            return mid
        elif (x < list[mid]):
            end = mid - 1
        else:
            start = mid + 1

    return 1

print "*"*13
print "BINARY SEARCH"
print "*"*13
n = input("Enter the size of the list: ")

list = []

for i in range(n):
    list.append(input("Enter element: "))

x = input("Enter the element to search: ")
position = bin_search(list, n, x)

if (position != 1):
    print("Entered number %d is present at position: %d" % (x, position+1))
else:
    print("Entered number %d is not present in the list" % x)
