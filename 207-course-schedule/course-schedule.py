class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        #brute force
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        for coursepair in prerequisites:
            course = coursepair[0]
            pre = coursepair[1]
            graph[course].append(pre)
        def dfs(course, visiting):
            if course in visiting:
                return False
            visiting.add(course)

            for pre in graph[course]:
                isprecomplete = dfs(pre, visiting)
                if isprecomplete == False:
                    return False
            visiting.remove(course)
            return True
        for i in range(numCourses):
            visiting = set()
            if dfs(i, visiting) == False:
                return False
        return True
        """
        # optimized
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for coursepair in prerequisites:
            course = coursepair[0]
            pre = coursepair[1]
            graph[course].append(pre)
        statearray = [0] * numCourses
        def dfs(course):
            if statearray[course] == 1:
                return False
            if statearray[course] == 2:
                return True
            statearray[course] = 1
            for pre in graph[course]:
                if dfs(pre) == False:
                    return False
            statearray[course] =2
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True






                


            

        

                  


       