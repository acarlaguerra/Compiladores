with open('Calc3.stk') as file:
    elem_array = [line.rstrip() for line in file]


def RPN(elem_array) -> int:
    stack = []

    def isNum(element):
        try:
            int(element)
            return True
        except:
            return False
        
    for elem in elem_array:
        if isNum(elem):
            stack.append(int(elem))
        else:
            first_elem = stack.pop()
            last_elem = stack.pop()
            if elem == "+":
                ans = last_elem + first_elem
            elif elem == "-":
                ans = last_elem - first_elem
            elif elem == "*":
                ans = last_elem * first_elem
            elif elem == "/":
                ans = int(last_elem / first_elem)

            stack.append(ans)

    return stack[-1]

print(RPN(elem_array))

