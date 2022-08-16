def binarySearch(elements, search_el):
    n_elements = len(elements)
    low = 0
    high = n_elements - 1

    while low <= high:
        mid = (low + high) // 2
        if elements[mid] == search_el:
            return mid
        elif elements[mid] > search_el:
            high = mid - 1
        elif elements[mid] < search_el:
            low = mid + 1
    return -1


def main():
    elements = []
    n_elements = int(input("enter number of elements: "))

    for i in range(0, n_elements):
        elements.append(int(input()))

    search_el = int(input("Enter the element to be searched: "))
    print("Element is found at ", binarySearch(elements, search_el))


if __name__ == "__main__":
    main()
