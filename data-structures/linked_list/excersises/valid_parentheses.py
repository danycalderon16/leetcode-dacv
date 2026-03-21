import sys
sys.path.append("C:\\Users\\danyc\\Documents\\leetcode-dacv\\data-structures\\linked_list")
from stack import Stack, Node

class Validator:
    
    @staticmethod
    def is_valid(string:str)->bool:
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
    
        stack = Stack()

        for c in string:
            if c in pairs:
                stack.push(Node(pairs[c]))
            elif c in pairs.values():
                if stack.is_empty or c != stack.pop().val:
                    return false
        
        return stack.is_empty   
            
if __name__ == "__main__":
    print(Validator.is_valid("()"))
    print(Validator.is_valid("()[]{}"))
    print(Validator.is_valid("(]"))
    print(Validator.is_valid("([)]"))
    print(Validator.is_valid("{[]}"))