class Hashmap:
    def __init__(self):
        self.size = 10
        self.arr = [[] for x in range(self.size)]

    def getHash(self, key):
        asciiVal = 0
        for char in key:
            asciiVal += ord(char)
        hashVal = asciiVal % self.size
        return hashVal

    def __setitem__(self, key, value):
        hashVal = self.getHash(key)
        flag = False
        for index, element in enumerate(self.arr[hashVal]):
            if element[0] == key:
                self.arr[hashVal][index] = (key, value)
                flag = True
        if not flag:
            self.arr[hashVal].append((key, value))

    def __delitem__(self, key):
        hashVal = self.getHash(key)
        for index, element in enumerate(self.arr[hashVal]):
            if element[0] == key:
                del self.arr[hashVal][index]

h1 = Hashmap()
h1['march 6'] = 320
h1['march 7'] = 65
h1['march 8'] = 111
h1['march 17'] = 424
print(h1.arr)
del h1['march 7']
print(h1.arr)
del h1['march 6']
print(h1.arr)