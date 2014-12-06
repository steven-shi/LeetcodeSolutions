from random import randint

class Sorts():
    def selection_sort(self, array):
        for i in range(0,len(array)-1):
            imin = i
            for j in range(i+1, len(array)):
                if array[j] < array[imin]:
                    imin = j
            array[i],array[imin] = array[imin], array[i]
        return array

    def bubble_sort(self, array):
        for i in range(0, len(array)-1):
            flag = False
            for j in range(0, len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    flag= True
            if flag==False:
                break
        return array

    def insertion_sort(self, array):
        for i in range(1, len(array)):
            for j in range(i-1, 1, -1):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
        return array

    def merge_sort(self,array):
        def merge(left, right, array):
            n = len(array)
            i, j, k = 0, 0, 0
            while(i < len(left) and j < len(right)):
                if left[i] <= right[j]:
                    array[k] = left[i]
                    i = i + 1
                else:
                    array[k] = right[j]
                    j = j + 1
                k = k + 1
            if i == len(left):
                array[k:] = right[j:]
            if j == len(right):
                array[k:] = left[i:]
            return array
        n = len(array)
        if n == 1:
            return [array[0]]
        left = self.merge_sort(array[:n/2])
        right = self.merge_sort(array[n/2:])
        return merge(left, right, array)

    def quick_sort(self, array):
        def partition(array):
            pivot = array[-1]
            idx =len(array) - 1
            for i in range(0, idx):
                if array[i] > pivot:
                    array.append(array[i])
                    del array[i]
                    idx = idx -1
            return idx

        if len(array) > 1:
            idx = partition(array)
            left = self.quick_sort(array[:idx])
            right = self.quick_sort(array[idx+1:])
            return left + [array[idx]] + right
        else:
            return array

    def heap_sort(self, array):
        def shift_down(root, end):
            while True:
                child = root*2+1
                if child > end:
                    break
                # left leaf < right leaf then child is right
                if child + 1 <= end and array[child+1] > array[child]:
                    child += 1
                if array[child] > array[root]:
                    #print 'swap'
                    array[root], array[child] = array[child], array[root]
                    root = child # go head to child, because child number's children might be able to go up as well
                else:
                    break

        for i in range((len(array)-1)/2, -1, -1):
            shift_down(i, len(array) -1)

        for j in range(len(array)-1, 0, -1):
            array[0], array[j] = array[j], array[0]
            shift_down(0, j-1)
        return array

def gen_rand():
    r = []
    for i in range(15):
        r.append(randint(1, 100))
    return r

test=gen_rand()
test=[98, 88, 97, 47, 71, 32, 89, 40, 27, 59, 62, 57, 87, 48, 32]
print 'test data\t%s'%test
print '================================================================'
s=Sorts()

print 'selection sort\t%s'%s.selection_sort(test)
print 'bubble sort\t%s'%s.bubble_sort(test)
print 'insertion sort\t%s'%s.insertion_sort(test)
print 'merge sort\t%s'%s.merge_sort(test)
print 'quick sort\t%s'%s.quick_sort(test)
print 'heap sort\t%s'%s.heap_sort(test)