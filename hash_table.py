class hash_table:
    def __init__(self):
        self.seize=10000
        self.keys=[None]*self.seize
        self.values=[None]*self.seize
    def insert(self,key,data):
        index=self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index]==key:
                self.values[index]=data#update
                return
            index=index+1
        self.keys[index]=key
        self.values[index]=data
    def get(self,key):
        index=self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index]==key:
                print(self.values[index])
            index=index+1
        return None





    def hash_function(self,key):
        sum=0
        for i in range(len(key)):
            sum=sum+ord(key[i])
        return sum%self.seize

hash=hash_table()
hash.insert("anas",19)
hash.insert("imane",20)
hash.insert("marwa",10)
hash.get("anas")