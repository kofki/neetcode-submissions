class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # n log(n) = merge sort
        def sortPartition(arr, l, r):
            if l >= r:
                return
            m = (r+l)//2
            sortPartition(arr, l, m)
            sortPartition(arr, m + 1, r)
            merge(arr, l, m, r)


        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1
            while j < len(left):
                arr[i] = left[j]
                i+=1
                j += 1
            while k < len(right):
                arr[i] = right[k]
                i+=1
                k +=1
    
        sortPartition(nums, 0, len(nums))
        return nums
    