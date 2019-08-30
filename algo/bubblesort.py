def bubble_sort(array):
    if (len(array) < 2):
        return array
    else:
        sorted = False
        for i in range(1, len(array)):
            current = array[i]
            prev = array[i - 1]
            #if right < left element
            if (current < prev):
                sorted = True
                array[i] = prev
                array[i - 1] = current
        if (sorted):
            return bubble_sort(array)
        else:
            return array

#driver
print(bubble_sort([56665,1,4,8,2,3,7,8,229,223,124,123,0,1,4,-6674,-2,-1,-56]))
