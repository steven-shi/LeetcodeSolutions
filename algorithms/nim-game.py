''' You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

Hint:

    If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?
'''

class Solution(object):
    def __init__(self):
        self.cache = {}
        
    def canWinNim(self, n):
        return n%4!=0
    
    def canWinNim_recusive(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        if n == 4:
            return False
        if n in self.cache:
            return self.cache[n]
        n_1 = self.cache[n-1] if n in self.cache else self.canWinNim(n-1)
        n_2 = self.cache[n-2] if n in self.cache else self.canWinNim(n-2)
        n_3 = self.cache[n-3] if n in self.cache else self.canWinNim(n-3)
        if not n_1 or not n_2 or not n_3:
            self.cache[n] = True
            return True
        else:
            self.cache[n] = False
            return False