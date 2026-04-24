class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #brute force
        """
        # create graph
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for pair in prerequisites:
            course = pair[0]
            pre = pair[1]
            graph[course].append(pre)

        def dfs(course, visiting):

            if course in visiting:
                return False
            
            #mark visiting
            visiting.add(course)
            #check all prerequisites
            for pre in graph[course]:
                result = dfs(pre, visiting)

                if result == False:
                    return False

            #remove from visiting
            visiting.remove(course)

            return True
        
        for i in range(numCourses):
            visiting = set()

            if dfs(i, visiting) == False:
                return False

        return True
        """
        #optimized
        #create graph
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for pair in prerequisites:
            course = pair[0]
            pre = pair[1]
            graph[course].append(pre)

            #state array
            state = [0] * numCourses

            def dfs(course):
                #if visiting -> cycle
                if state[course] == 1:
                    return False

                #if already visited
                if state[course] == 2:
                    return True

                #mark visiting
                state[course] = 1

                #check all prerequisites
                for pre in  graph[course]:

                    if dfs(pre) == False:
                        return False

                #mark visited(safe)
                state[course] = 2
                return True

            for i in range(numCourses):
                if dfs(i) == False:
                    return False

        #no cycle
        return True


        