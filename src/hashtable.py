# '''
# Linked List hash table key/value pair
# '''

#
'''
LinkedPair is a fully complete LL - this is all we need for chaining (dont need doubly LL )

WHy two functions for something that can be done with a single line of code - why not just calling _hash_mod ?
Why did our colleague put this here? readability, re use, and so you can change it out later. You are future proofing this and abstracting away bc might decide later on you dont want to use python's hash method  = ABSTRACTION 

Use LinkedPAIR to save BOTH KEY AND VALUE 

'''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table / how many things we can fit into hash table
        self.storage = [None] * capacity #Emulating functionality of allocating memory by using python list

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # return hashlib.sha256(key.encode())
        return hash(key)

    #Leading underscore means DONT USE IT outside of the class, private
    #In python unlike other languages, is there anything preventing u from using it outside of a class? No
    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.


        '''
        #1) Find the index ->  take key and hash it to turn it into an index in our array 
        index = self._hash_mod(key)

        #2) Check of an error
        if self.storage[index] is not None:
            print("ERROR: Key in use")
        else:
            #put it there
            self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        if self.storage[index] is not None:
            self.storage[index] = None 
        else:
            print("WARNING: Key not found")
        
     

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        return self.storage[index]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.

        What to do to resize? What is similar to? the double function
        When we modulus  hash of key, we'll get new numbers. We need to rehash everything when we resize, otherwise everything will be in the wrong place 
        '''
        # old_storage = self.storage.copy() - so its not pointing to the same address
        old_storage = self.storage
        #double capacity
        self.capacity = self.capacity * 2
        #make new storage
        self.storage = [None] * self.capacity
        #old storage is an array with no key or value, 
        for bucket_item in old_storage:
            #places everything in new 
            self.insert(bucket_item.key, bucket_item.value)



##no collision handling 
if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
