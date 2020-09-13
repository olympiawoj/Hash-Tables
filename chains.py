import random


def longest_linked_list_chain(keys, buckets, loops=10):
    '''
    Roll keys number of keys into buckets number of random buckets and count collisions
    loops is # of times we want to test this 

    Let's use a dict - python's implementatio of a hash table
    '''

    for i in range(loops):
        key_counts = {}

        for i in range(buckets):
            # fill dict with one number for each possible index
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            #module by length of array or buckets
            hash_index = hash(random_key)% buckets
            #whatever index came up, add 1 to it
            key_counts[hash_index] +=1

        largest_n = 0
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]
            
        print(f"Longest linked list chain for {keys} keys in {buckets} buckets (Load Factor: {keys/buckets:.2f}): {largest_n}")



#whats the worst LL chain going to be? 
#5 items in 10 buckets, longest chain will be 2/3
#whats the time complexity to look up somethig in a LL? to find it something is there? --> O(n), not that bad
#whats our best case scenario to find if a certain value is on our hash  table? O(1)
#worse case scenaior is O(n) but how likley are we to get worst wrost case scenario? Its possible, but low probabilty
#why these are great - worst case scenario is O(n) but avg is only slightly worse than O(1) which is normally roudned to O(1)
#by using LL, memory efficient, we improve memory efficiency of it 

longest_linked_list_chain(50, 100, 5)


