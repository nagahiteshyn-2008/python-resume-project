def bubble_sort(arr):
    n = len(arr)
    # Outer loop tracks passes over the array
    for i in range(n):
        # Inner loop compares adjacent elements
        # (n - i - 1 prevents checking already sorted elements at the end)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [64, 34, 25, 12, 22]
bubble_sort(numbers)
print("Sorted array:", numbers)
print("=== My Calculator ===")
a = int(input("First number: "))
b = int(input("Second number: "))
print(f"Add: {a+b} | Sub: {a-b} | Mul: {a*b}")