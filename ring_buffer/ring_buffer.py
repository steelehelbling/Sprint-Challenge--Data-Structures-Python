class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity #max number
        self.arry = []     #empty arry to keep arry
        self.len = 0
        self.oldest_position = 0  #oldest_item position

    def __len__(self):
        return self.len

    def append(self, item):
        if self.len < self.capacity:#chesks if there is room 
            self.len = self.len + 1
            self.arry.append(item)#theres more room add it to the end in the newest slotes
        if self.len >= self.capacity:
            self.arry.pop(self.oldest_position)#deletes oldest item
            self.arry.insert(self.oldest_position, item)#inserts new value into the oldest slot 
        if self.oldest_position +1 != self.capacity:#checkes if you replased all new values
            self.oldest_position = self.oldest_position + 1#keeping track of oldest value 
        else:#replaced all the old values 
            self.oldest_position = 0#set new oldest value

    def get(self):
        return self.arry#grabs array

ring = RingBuffer(4)
ring.append('q')
ring.append('w')
print(ring.get())
ring.append('y')
print(ring.get()) 
ring.append('u')
print(ring.get())  
ring.append('i')
print(ring.get())  