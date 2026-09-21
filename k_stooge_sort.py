def k_stooge_sort(arr, k, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if k < 3:
        raise ValueError("k는 3 이상으로 설정하는 것을 권장합니다.")

    # 원소가 0~1개
    if left >= right:
        return

    # Stooge Sort 기본 동작
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]

    length = right - left + 1

    if length <= 2:
        return

    # 전체의 약 1/k만큼 제외
    cut = max(1, length // k)

    # 앞/뒤 (k-1)/k 구간을 번갈아 k번 호출
    for i in range(k):
        if i % 2 == 0:
            # 앞쪽 약 (k-1)/k
            k_stooge_sort(arr, k, left, right - cut)
        else:
            # 뒤쪽 약 (k-1)/k
            k_stooge_sort(arr, k, left + cut, right)

arr = list(map(int, input().split()))
k = int(input("몇-Stooge? "))

k_stooge_sort(arr, k)

print(arr)
