
# coding: utf-8

# In[16]:

def QuickSort(l):
    if len(l) > 1:
 
        pivot = l[-1]
        # index of pivot
        i_p = len(l)-1
        # index of current first element used to compare with pivot
        cur = 0
        for i in l:
            if l[cur]<=pivot:
                # if compared number less or equal than pivot, it should belong to the position where it is
                cur+=1
            else:
                # change orders
                l[i_p]=l[cur]
                l[cur] = l[i_p-1]
                l[i_p-1] = pivot
                i_p-=1
        # recursively sort 
        return QuickSort(l[:i_p])+[pivot]+QuickSort(l[i_p+1:])
    # else return l for length of l == 1 or l is empty
    return l



def test():
    print QuickSort([2,1,4,8,0,3])

test()

