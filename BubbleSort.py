# first method
def bubble(l):
    count = 0
    while count != len(l)-1:
        index = 0
        count = 0
        while index < len(l)-1:
      
            if l[index] <= l[index+1]:
                count+=1
            else:
                smaller = l[index+1]
                l[index+1] = l[index]
                l[index]=smaller
            index+=1
    return l


# second method: recursion
def bb(l):
    if len(l) > 1:
        index = 0
        while index <len(l)-1:
            if l[index]<=l[index+1]:
                pass
            else:
                s = l[index+1]
                l[index+1] = l[index]
                l[index] = s
            index += 1
        return bb(l[:-1])+[l[-1]]
    return l