def siberian_sort(arr):
    arr = arr.copy()
    round_number = 0

    while True:
        print(f"{round_number}: {arr}")

        if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
            return arr

        moscow = [arr[0]]
        siberian = []

        for x in arr[1:]:
            if x >= moscow[-1]:
                moscow.append(x)
            else:
                siberian.append(x)

        arr = siberian + moscow
        round_number += 1

arr = list(map(int, input().split()))
siberian_sort(arr)
