class Solution:
    def isValid(self, s: str) -> bool:
        #def a funtion that takes a dtring and return T or F

        stack = []
        #an empty list that wil be used to keep track of opening braakets

        closetoOpen = {")": "(", "]": "[", "}": "{"}
        #cretes a dictionary that matched each closing bracket with the opening bracket that belongs to it 

        for c in s:
            #checks wheter the current charscter is a closing bracket
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    #make sure the stack is not empty and checks wheather the recent opening bracket matches the closing bracket
                    stack.pop()
                    #removes the matching opening bracket from the stack
                else:
                    return False 
                    # returns false only if the brackets is not vaild
            else:
                stack.append(c)
                #adds the opening bracket to the top of the stack 
        return True if not stack else False
        # Returns True if the stack is empty because every opening bracket has a matching closing bracket else would return false