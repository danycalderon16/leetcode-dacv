class Solution:
    def isValid(self, s: str) -> bool:
        # stack_braces = []
        # stack_brackets = []
        # stack_parentheses = []

        # for char in s:
        #     if char == "(":
        #         stack_parentheses.append(char)
        #     if char == "[":
        #         stack_brackets.append(char)
        #     if char == "{":
        #         stack_braces.append(char)
        #     if char == ")":
        #         if len(stack_parentheses) == 0:
        #             return False
        #         stack_parentheses.pop()
        #     if char == "]":
        #         if len(stack_brackets) == 0:
        #             return False
        #         stack_brackets.pop()
        #     if char == "}":
        #         if len(stack_braces) == 0:
        #             return False
        #         stack_braces.pop()

        # return stack_braces == [] and stack_brackets == [] and stack_parentheses == []

        stack = []

        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            
            if c == ")":
                if len(stack) == 0:
                    return False
                if stack.pop() != ")":
                    return False
            
            if c == "]":
                if len(stack) == 0:
                    return False
                if stack.pop() != "]":
                    return False
            
            if c == "}":
                if len(stack) == 0:
                    return False
                if stack.pop() != "}":
                    return False
        
        return len(stack) == 0

if __name__ == "__main__":
    solution = Solution()
    
    string = "{[()}"

    print(solution.isValid(string))