'''
Lets write some code to test collisions

Would it work to use a list instead of a set to keep track of what we've found? we can test it . V commonly can see timeouts bc youve used a list/array instead of a set. It works, but as it gets longer, its timing out bc of it. 

If we have 10,000 spots and we're assinging things randomly in them, collision is inevitable even tho chances are slim, its inevitable it will happen. With 10,000 things youre only using 1% of whole data stucture before you get a collision. It's a "when" chance not and "if"

SO what do we do to thix this? That's where LL chainging comes in

We can combine two data structures -- take our array, and instead of putting a number in it, our value -- 

'''
import random

def how_many_before_collision(buckets, loops=1):
    '''
    Roll random hashes indexes into buckets and print
    how many rolls before a collision

    Run loops times
    '''
    for i in range(loops):
        tries = 0
        tried = set()
        tried_list=[]

        while True:
            random_key = str(random.random())

            hash_index = hash(random_key) % buckets
        #change tried to tried_list to test list case
            if hash_index not in tried:
                tried.add(hash_index)
                # tried_list.append(hash_index)
                tries += 1

            else: 
                #we have found a collision
                break 
        #.1f is a python that says 1 decimal, floating point precision to use, formatting value to show 1 decimal
        print(f"{buckets} buckets, {tries} hashes before collision. ({tries/buckets * 100:.1f}%)")


# how_many_before_collision(1000000000, 1)
how_many_before_collision(100, 10)