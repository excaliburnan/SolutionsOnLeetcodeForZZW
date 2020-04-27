# 哈希表 + 动态数组

from random import choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
        last, idx = self.list[-1], self.dict[val]
        self.list[idx], self.dict[last] = last, idx     # 此时val的list位置被last对应覆盖， 把dict中val的索引赋予last
        self.list.pop()                                 # 此时 list[-1] 和 dict[val] 对应的不正确，但是不重要，删除即可
        del self.dict[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()