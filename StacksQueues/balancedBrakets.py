def is_matched(expression):
    if len(expression) % 2 != 0:
        return False

    opening = [expression[0]]

    for i in range(1, len(expression)):
        if(expression[i] == '[' or expression[i] == '{' or expression[i] == '('):
            opening.append(expression[i])
        else:
            if((len(opening) == 0) or ((expression[i] == '}' and opening[-1] != '{') or (expression[i] == ']' and opening[-1] != '[') or (expression[i] == ')' and opening[-1] != '('))):
                return False
            else:
                opening = opening[0:-1]

    return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
