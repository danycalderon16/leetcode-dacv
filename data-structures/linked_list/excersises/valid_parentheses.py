import sys
sys.path.append("C:\\Users\\danyc\\Documents\\leetcode-dacv\\data-structures\\linked_list")
from stack import Stack, Node

class Validator:
    
    def __init__(self):
        self.elements = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
    
    def is_valid(string:str)->bool:
        stack = Stack()

        chars = list(string)
        
        for c in chars:
            if c == "(":
                stack.push(Node(")"))
            elif c == "{":
                stack.push(Node("}"))
            elif c == "[":
                stack.push(Node("]"))
            elif stack.is_empty():
                return False
            elif c == ")":
                if stack.pop().val != ")":
                    return False
            elif c == "}":
                if stack.pop().val != "}":
                    return False
            elif c == "]":
                if stack.pop().val != "]":
                    return False
        return True
    
if __name__ == "__main__":
    print(Validator.is_valid("()"))
    print(Validator.is_valid("()[]{}"))
    print(Validator.is_valid("(]"))
    print(Validator.is_valid("([)]"))
    print(Validator.is_valid("{[]}"))