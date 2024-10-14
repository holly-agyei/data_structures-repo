def check_pairs(s)->str:
    stack = []
    pairs = {'(':')','{':'}','[':']'}

    for char in s:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if stack and pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False
    return not stack

s = "(([]){"
print(check_pairs(s))