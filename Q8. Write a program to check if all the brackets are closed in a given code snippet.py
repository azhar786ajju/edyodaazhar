#!/usr/bin/env python
# coding: utf-8

# In[1]:


def areBracketsClosed(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 

if __name__ == "__main__":
    expr = "{{()}}[]"
 
    # Function call
    if areBracketsClosed(expr):
        print("Closed")
    else:
        print("Not Closed")

