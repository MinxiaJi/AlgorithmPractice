def Longest(a):
    # check every possible palindromic and remeber the index for head and tail, save them to a list
    longest = []
    for i,item in enumerate(a):
        current_letter = item
        following_str = a[i+1:]
        for j, letter in enumerate(following_str):
            if letter == current_letter:
                longest.append([j+i+1,i])
    # compute length of each possible palindromic and save it to a dictionary.
    # Key is length while value is index of head and tail
    index_longest = {}
    # find the maximum length and return its correspoinding index pair
    for k in longest:
        index_longest[k[0]-k[1]]=k
    head_tail = index_longest[max(index_longest)]
    head_index = head_tail[1]
    tail_index = head_tail[0]
    return a[head_index:tail_index+1]