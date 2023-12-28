"""
实现优先级队列
实现一个队列,它能够以给定的优先级对元素排序,每次pop操作都会
返回优先级最高的那个元素
"""

import heapq

class PriorityQueue:

    def __init__(self) -> None:
        """
        变量 index 的作用是为了将具有相同优先级的元素以适当的顺序排列。
        通过维护一个不断递增的索引，元素将以它们入队列时的顺序来排列。
        """
        self._queue = []
        self._index = 0
        
    def push(self, item, priority):
        """
        proority取负值是为了让队列能够按元素的优先级从高到低的顺序排列

        Args:
            item (_type_): _description_
            priority (_type_): _description_
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    

class Item:
    def __init__(self, name) -> None:
        self.name = name
        
    def __repr__(self) -> str:
        return 'Item({!r})'.format(self.name)
    
    
pq = PriorityQueue()
pq.push(Item('foo'), 1)
pq.push(Item('bar'), 5)
pq.push(Item('spam'), 4)
pq.push(Item('grok'), 1)


# 优先级最高的最先弹出
print(pq.pop())
print(pq.pop())
print(pq.pop())
print(pq.pop())