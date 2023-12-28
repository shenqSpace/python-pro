"""
保留最后N个元素
在迭代或是其他形式的处理过程中对最后几项记录做一个有限的历史记录
"""

from collections import  deque

def search(lines, pattern, history=5):
    """deque(max=N)自动创建一个固定长度的队列，当有新记录加入时，自动移除最老的那条记录"""
    previous_lines = deque(max=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
        
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
            
