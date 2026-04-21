class Solution(object):
    def isValid(self, s):
        #brute force
        """while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        return s == "" """
        
        # stack
        stack = []
        for para in s:
            if para in "([{":
                stack.append(para)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (para == ")" and top != "(") or \
                   (para == "]" and top != "[") or \
                   (para == '}' and top != "{"):
                   return False
        return len(stack) == 0
        
        