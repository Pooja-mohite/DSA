class Solution(object):
    def isValid(self, s):
        '''
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s= s.replace("{}", "")
        return s== ""
        '''
        stack = []
        for para in s:
            if para in "{[(":
                stack.append(para)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (para == ")" and top != "(") or \
                (para == "]" and top != "[") or \
                (para == "}" and top != "{"):
                    return False
        return len(stack) == 0


                







        