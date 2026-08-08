class MyHashMap:

    # Using only nested lists and list operations
    # def __init__(self):
    #     self.hashmap = []

    # def put(self, key: int, value: int) -> None:
    #     for i in range(len(self.hashmap)):
    #         if self.hashmap[i][0]==key:
    #             self.hashmap[i][1]=value
    #             break
    #     else:
    #         self.hashmap.append([key,value])
        
    # def get(self, key: int) -> int:
    #     for i in range(len(self.hashmap)):
    #         if self.hashmap[i][0]==key:
    #             return self.hashmap[i][1]
    #     return -1

    # def remove(self, key: int) -> None:
    #     for i in range(len(self.hashmap)):
    #         if self.hashmap[i][0]==key:
    #             self.hashmap.pop(i)
    #             break

    # Using extra _hash method for hashing the values into buckets to reduce time
    def __init__(self):
        self.size = 769
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return

        bucket.append((key, value))      # Insert new key

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)