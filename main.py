# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")




# must be in-place sort
def merge_sort(arr,cmp):
    if len(arr) > 1:
        m = len(arr)//2 # middle of array
        l = arr[:mid] # left of array
        r = arr[mid:] # right of array
        merge_sort(l,cmp) # recursion calls
        merge_sort(r,cmp)

        x = len(l)
        y = len(r)
        i = j = 0
        k = 0
        while x > i and y > j:
            if cmp(l[i], r[j]) < 0:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while x > i:
            arr[k] = l[i]
            i += 1
            k += 1

        while y > j:
            arr[k] = l[i]
            i += 1
            k += 1

# must be in-place sort
def quick_sort(arr,cmp):
    pass