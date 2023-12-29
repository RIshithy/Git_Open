def mergesort(array):
    debug_print(array=array)
    if len(array) <= 1:
        return array

    m = len(array) // 2
    debug_print(m=m)

    left = mergesort(array[:m])
    right = mergesort(array[m:])
@@ -21,6 +23,8 @@ def mergesort(array):


def merge(left, right):
    debug_print(debug_msg="Merging...", left=left, right=right)

    merged = []

    while len(left) > 0 and len(right) > 0:
@@ -34,12 +38,16 @@ def merge(left, right):
    else:
        merged += right

    debug_print(merged=merged)
    return merged


if _name_ == "_main_":
    input_str = input("Enter numbers, separated by ',': ")

    input_list = input_str.split(",")
    debug_print(input_list=input_list)

    value_list = []
    for x in input_list:
        try:
@@ -48,5 +56,7 @@ def merge(left, right):
            print("Invalid input.")
            quit(1)

    debug_print(value_list=value_list)

 sorted_list = mergesort(value_list)
    print(sorted_list)
