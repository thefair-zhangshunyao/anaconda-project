def erfenSort(targe,list):
    left = 0
    right = len(list)
    while left < right:
        mid = (left + right)//2
        if targe == list[mid]:
            return mid
        elif targe < list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return right+1
list=[1,3,5,7,11,16,23,30]
print(erfenSort(26,list))

