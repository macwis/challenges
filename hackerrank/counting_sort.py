def counting_sort(arr):
    s = max(arr) + 1
    counts = [0] * s

    # calc appearences
    for a in arr:
        counts[a] += 1

    # accumulate
    for i in range(s):
        if i > 0:
            counts[i] += counts[i - 1]

    # shift 1-pos to right
    for i in range(1, s):
        counts[s-i] = counts[s-i-1]
    counts[0] = 0

    # read-out sorted array
    sorted = [0] * len(arr)
    for a in arr:
        sorted[counts[a]] = a
        counts[a] += 1

    return sorted

if __name__ == '__main__':
    arr = [0,9,2,6,8,7,3,5,0,9,3,1,7,5,2,4,9,2,4]
    #arr = [1,0,3,1,3,1]
    arr_sorted = counting_sort(arr)
    print(arr_sorted)
