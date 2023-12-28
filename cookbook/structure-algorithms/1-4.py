"""
找到最大或最小的N个元素
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

"""
在此基础上可以添加一个参数key,以支持更复杂的工作
"""
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22}, 
    {'name': 'FB', 'shares': 200, 'price': 21.09}, 
    {'name': 'HPQ', 'shares': 35, 'price': 31.75}, 
    {'name': 'YHOO', 'shares': 45, 'price': 16.35}, 
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# key 是指定字段作为筛选条件
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
cheap = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

"""
如果集合中有很多元素,你要找的N个元素很少,以下函数性能更好.
这些函数首先将底层数据转化成列表,元素以堆的顺序排列.
堆最重要的特性就是heap[0]总是最小那个元素
"""
nums2 = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums2)
heapq.heapify(heap)
print(heap)
# 通过heappop()弹出前3个最小的元素
for _ in range(3):
    print('弹出', heapq.heappop(heap))

"""
如果只想找单个最大或最小的值,直接用min()或max()即可
如果要找的元素个数N和集合本身差不多大,最好先将集合排序,然后通过切片获取元素
sorted[items][:N]
"""
