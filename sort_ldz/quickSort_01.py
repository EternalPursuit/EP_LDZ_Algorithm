def partition(arr,low,high):
    pivot = arr[(low+high)//2]
    while low < high:
        while low < high and arr[low] <= pivot:
            low += 1
        while low < high and arr[high] >= pivot:
            high -= 1
        if low < high:
            arr[low],arr[high] = arr[high],arr[low]
    return low

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
        
        
def partition(arr, low, high):
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[low], arr[high] = arr[high], arr[low]
    return low


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
        




list1 = [8, 5, 1, 3, 2, 10, 11, 4, 12, 20]
quickSort(list1,0,len(list1)-1)
print(list1)