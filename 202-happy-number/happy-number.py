class Solution(object):
    def isHappy(self, n):
        # traverse all digit of the number
        #take last didgit and square it
        # add that square

        summ = 0
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
        return False



        
        

        
        