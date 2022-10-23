
#arr = (1, 4, 4, 7, 8, 9, 9)
class mezo:
    arr = (1, 4, 4, 7, 8, 9, 9)
    def hasDuplicate():
     arr = (1, 4, 4, 7, 8, 9, 9)
     print(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
          if i != j and arr[i] == arr[j]:
              print(arr[i] == arr[j])
        else:
            print(arr[i] != arr[j])     