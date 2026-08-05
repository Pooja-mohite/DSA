class Solution(object):

    def isHappy(self, n):
        # traverse all digit of the number
        #take last didgit and square it
        # add that square

        """summ = 0
        hashset = set()
        while n not in hashset:
            if n == 1:
                return True
            else:
                hashset.add(n)
            summ = 0
            while n > 0:
                lastd = n% 10
                square = lastd * lastd
                summ = summ + square
                n = n // 10
            n = summ
        return False"""

        # take last digit and square it
        # slow = n and fast = n
        # slow 1 step and fast take 2 steps till fast not equal to 1

        slow = n
        fast = n
        while fast!= 1:
            slow = self.fun(slow)
            fast = self.fun(fast)
            fast = self.fun(fast)
            if slow == fast and slow != 1:
                return False
        return True
    def fun(self,n):
        summ = 0
        while n>0:
            d = n % 10
            n = n // 10
            summ = summ + (d * d)
        return summ




        
        

        
        