def binarySearch(elements, search_el):
    n_elements = len(elements)
    low = 0
    high = n_elements - 1

    # iteration continues as soon as low and high converge or equal
    while low <= high:
        # always calculate mid
        mid = (low + high) // 2
        if elements[mid] == search_el:
            # if search el is at mid, return mid
            return mid
        elif elements[mid] > search_el:
            # if seach el is less than mid, then probably element is
            # present in the lower half. So high will be 1 less than mid
            high = mid - 1
        elif elements[mid] < search_el:
            # if seach el is greater than mid, then probably element is
            # present in the upper half. So low will be 1 greater than mid
            low = mid + 1
    return -1  # if element is not found


def main():
    elements = []
    n_elements = int(input("enter number of elements: "))

    for i in range(0, n_elements):
        elements.append(int(input()))

    search_el = int(input("Enter the element to be searched: "))
    print("Element is found at ", binarySearch(elements, search_el))


if __name__ == "__main__":
    main()
