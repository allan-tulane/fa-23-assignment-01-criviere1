"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if (x <= 1):
        return x
    else:
        return foo(x-1) + foo(x-2)
    pass


def longest_run(mylist, key):
    ### TODO
    j_max = 0
    j = 0
    for i in range(len(mylist)):
        if (mylist[i] == key):
            j += 1
            #print(j)
        else:
            if (j > j_max):
                j_max = j
            j = 0
    return j_max
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    if not mylist: # making sure the list isn't empty
        return 0
    if mylist[0] == key:
        count = 1
        while count < len(mylist) and mylist[count] == key:
            count += 1
        return max(count, longest_run_recursive(mylist[count:], key))

    return longest_run_recursive(mylist[1:], key)
    

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


