

#Make our own array class

class DynamicArray:
    #initialize array, make a constructor
    #must track capacity and count, how many we're using inside array, 
    #need place to store or data - emulate allocating memory by allocating spaces or buckets in a python list
    #capacity is number of empty spots
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    
    def __len__(self):
        return self.count

    #inserting into an array, what 2 things are relevant - value and place
    #insert is non destrictuve, doesnt just overwrite, but check a few things before moving everything over
    #check to make sure we have in the first place capacity/open space/ index in range
    #
    def insert(self, index, value):
        #make sure we have open space
        if self.count >= self.capacity:
            #TO DO : make array dynamically resize
            self.double_size()
        #make sure index is in range
        if index > self.count:
            print("ERROR: Index out of range")
            return

        #shift everything over to right
        #start with the last one, move it to the right, do a backwards for loop to start at end and go neative
        for i in range(self.count, index, -1):
            #self storage at i becomes w/e is to left of it 
            self.storage[i] = self.storage[i-1]


        #insert our value
        self.storage[index] = value
        self.count +=1
    
    def append(self, value):
        self.insert(self.count, value)
    
    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]

        #replace self.storage with new storage
        self.storage = new_storage




#Where is the initial value, we're initializing with Capacity, so we're doing my_array[4]

my_array = DynamicArray(4)

#index of 0
print(my_array.storage)
my_array.insert(0, 1)
my_array.insert(0, 2)
my_array.insert(1, 3)
my_array.insert(1, 3)
my_array.insert(0, 5)
my_array.append(20)

print(my_array.storage)


#[2, 3, 1, 4]



# after adding double capacity:
# [5, 2, 3, 1, 4, 20, None, None]