import hashlib


n=10
#b turns into a byte string instead of python object, in python there's metadata that wont let it be hashed bc if we hash diff data we get a diff hash

key = b"my_value"
key2 = "string".encode()
key3 = b"lunchtime"

#A string in Python is an object. It has meta data in it.
# What's crazy is that mathematically, there are an infinite number of inputs that will produce a given hash value... it's just that there is a much, much larger infinite number of inputs that do not produce that hash.
# The odds of guessing the input for a hash is like winning the lottery billions of billions of times in a row.
#all diff class functions that ar ebuilt into it
#For our hash function to work, give a string of just the bites which is what the b part does
# everytime we run it, in python it uses a diff sudo random seed so it's salting the values - within memory or one program execution it'll be consistent but it'll happen differently each time you're debugging it
# Keep in mind
# Can use ssh56 which we can import 
#hexdigest lets us print a value



# hash/mod --> we go and
# my_value, 72
# take value, run through has, and then put it there
# 


index = hash(key)%8
index2 = hash(key2)%8
index3 = hash(key3)%8
print(index)
print(index2)
print(index3)

#WHO GOT COLLISIONS? TRY TO PUT 2 THINGS IN THE SAME INDEX?




# for i in range(n):
#     print(hash(key))
#     print(hashlib.sha256(key).hexdigest())

# for i in range(n):
#     print(hash(key))


# for i in range(n):
#     print(hash(key2))

