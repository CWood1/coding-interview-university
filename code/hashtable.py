#!/usr/bin/env python3

from hashlib import md5

class HashTable:
    def __init__(self):
        self.table = [(None,None)] * 65536
        self.idx_size_bytes = 2

    def _hash(self, k, m):
        """Computes a hash for key k, of size m bytes, for a table 256^m entries large"""
        h = md5()
        h.update(k.encode())
        digest = h.hexdigest()[:2*m]

        idx = int(digest, 16)

        return idx

    def exists(self, k):
        idx = self._hash(k, self.idx_size_bytes)

        while self.table[idx][0] is not None and self.table[idx][0] != k and idx < 65536:
            idx += 1

        if idx == 65536:
            raise Exception
            
        if self.table[idx][0] is None:
            return False
        elif self.table[idx][0] == k:
            return True

    def add(self, k, v):
        idx = self._hash(k, self.idx_size_bytes)

        while self.table[idx][0] is not None and self.table[idx][0] != k and idx < 65536:
            idx += 1

        if idx == 65536:
            raise Exception
    
        self.table[idx] = (k, v)

    def get(self, k):
        idx = self._hash(k, self.idx_size_bytes)

        while self.table[idx][0] is not None and self.table[idx][0] != k and idx < 65536:
            idx += 1

        if idx == 65536:
            raise Exception
            
        if self.table[idx][0] is None:
            return None
        elif self.table[idx][0] == k:
            return self.table[idx][1]
        

    def remove(self, k):
        idx = self._hash(k, self.idx_size_bytes)

        while self.table[idx][0] is not None and self.table[idx][0] != k and idx < 65536:
            idx += 1

        if idx == 65536:
            raise Exception

        self.table[idx] = (None, None)
        # We may overwrite values here which don't already exist, this isn't a problem at all

        if self.table[idx + 1][0] is not None:
            # We need to scan through and see if anything can be moved up
            # This is done by rehashing every key, and the first one to hash
            # to less than or equal to the one just removed gets moved up
            new_idx  = idx + 1

            while self.table[new_idx][0] is not None:
                actual_idx = self._hash(self.table[new_idx][0], self.idx_size_bytes)

                if actual_idx <= idx:
                    self.table[idx] = self.table[new_idx]
                    self.table[new_idx] = (None, None)

                    idx = new_idx

                new_idx += 1
                
if __name__ == "__main__":
    h = HashTable()
    
    assert (not h.exists("Not yet")), "Key should not exist in an empty hash table"
    h.add("First", 13)
    assert h.exists("First"), "Key should exist after having been added"
    assert (h.get("First") == 13), "Key should contain correct value after having been added"
    h.add("First", 14)
    assert (h.get("First") == 14), "Key did not update"
    h.remove("First")
    assert (not h.exists("First")), "Key should not exist after having been removed"
    
