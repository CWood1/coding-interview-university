#!/usr/bin/env python3

from copy import copy

class Vector:
    def __init__(self):
        self.array = [0] * 16
        self.length = 0

    def _resize(self, new_capacity):
        if new_capacity < self.length:
            raise IndexError
    
        old = copy(self.array)
        self.array = [0] * new_capacity

        for i in range(0, self.length):
            self.array[i] = old[i]

    def size(self):
        return self.length

    def capacity(self):
        return len(self.array)

    def is_empty(self):
        return self.length == 0

    def at(self, index):
        if index >= self.length:
            raise IndexError

        return self.array[index]

    def push(self, item):
        if type(item) is not int:
            raise TypeError

        if self.length == len(self.array):
            self._resize(len(self.array) * 2)

        self.array[self.length] = item
        self.length += 1

    def insert(self, index, item):
        if type(item) is not int:
            raise TypeError

        if self.length == len(self.array):
            self._resize(len(self.array) * 2)

        for i in reversed(range(index, self.length)):
            self.array[i + 1] = self.array[i]

        self.array[index] = item
        self.length += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        if self.length == 0:
            raise IndexError
        
        self.length -= 1
        old = self.array[self.length]

        if self.length <= len(self.array) / 4:
            self._resize(int(len(self.array) / 2))

        return old

    def delete(self, index):
        if index >= self.length:
            raise IndexError
        
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

        self.length -= 1

        if self.length <= len(self.array) / 4:
            self._resize(int(len(self.array) / 2))

    def find(self, item):
        if type(item) is not int:
            raise TypeError
        
        for i in range(0, self.length):
            if self.array[i] == item:
                return i

        return -1

    def remove(self, item):
        index = self.find(item)

        while index != -1:
            self.delete(index)
            index = self.find(item)

if __name__ == "__main__":
    vector = Vector()

    assert vector.size() == 0, "Vector is not initialised to 0 length"
    assert vector.capacity() == 16, "Vector is not initialised to capacity 16"
    assert vector.is_empty(), "Vector is not initialised empty"

    try:
        vector.at(0)
        assert False, "Vector does not throw an error when accessing nonexistent values"
    except IndexError:
        pass
    except Exception:
        assert False, "Vector does not throw an IndexError when accessing nonexistent values"

    try:
        vector.pop()
        assert False, "Vector successfully pops item when empty"
    except IndexError:
        pass
    except Exception:
        assert False, "Vector does not throw IndexError when popping on empty"

    try:
        vector.delete(0)
        assert False, "Vector successfully deletes nonexistent item"
    except IndexError:
        pass
    except Exception:
        assert False, "Vector does not throw IndexError when deleting nonexistent items"

    vector.push(3)
    try:
        assert vector.at(0) == 3, "Vector does not store values with correct value"
    except Exception:
        assert False, "Vector does not store values at all"

    try:
        assert vector.pop() == 3, "Vector does not correctly pop values"
    except Exception:
        assert False, "Vector errors when popping existing value"

    assert vector.size() == 0, "Vector does not decrement length on pop"

    vector.push(1)
    vector.push(3)
    vector.insert(1, 2)

    assert vector.size() == 3, "Vector does not update length on insert"

    try:
        assert vector.pop() == 3, "Vector does not insert correctly - expected 3"
        assert vector.pop() == 2, "Vector does not insert correctly - expected 2"
        assert vector.pop() == 1, "Vector does not insert correctly - expected 1"
    except Exception:
        assert False, "Vector errors when popping value after install"

    vector.push(2)
    vector.prepend(1)

    try:
        assert vector.at(0) == 1, "Vector does not prepend correctly"
        assert vector.pop() == 2, "Vector prepend pop returns incorrect value"
        assert vector.pop() == 1, "Vector prepend pop returns incorrect second value"
    except Exception:
        assert False, "Vector errors after prepend"

    vector.push(1)
    vector.push(2)

    try:
        vector.delete(0)
        assert vector.at(0) == 2, "Vector does not delete correctly"
        vector.delete(0)
        assert vector.size() == 0, "Vector does not update length on insert"
    except Exception:
        assert False, "Vector errors on delete that should work"

    vector.push(1)
    vector.push(1)
    vector.push(1)
    vector.push(2)
    vector.push(1)

    try:
        assert vector.find(1) == 0, "Vector does not correctly find elements"
        vector.remove(1)
        assert vector.find(1) == -1, "Vector does not correctly indentify missing elements to find"
        assert vector.size() == 1, "Vector does not update length on remove"
        assert vector.pop() == 2, "Vector did not pop correctly after delete"
    except Exception:
        assert False, "Vector should not error on remove"

    vector.push(1)
    vector.push(2)
    vector.push(3)
    vector.push(4)
    vector.push(5)
    vector.push(6)
    vector.push(7)
    vector.push(8)
    vector.push(9)
    vector.push(10)
    vector.push(11)
    vector.push(12)
    vector.push(13)
    vector.push(14)
    vector.push(15)
    vector.push(16)
    vector.push(17)

    assert vector.capacity() == 32, "Vector capacity not kept up to date as double after reaching capacity"

    vector.pop() # 16
    vector.pop() # 15
    vector.pop() # 14
    vector.pop() # 13
    vector.pop() # 12
    vector.pop() # 11
    vector.pop() # 10
    vector.pop() # 9
    vector.pop() # 8
    
    assert vector.capacity() == 16, "Vector capacity not updated after reaching a quarter usage"
    
