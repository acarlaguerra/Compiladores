with open('Calc4.stk') as file:
    element_array = [line.rstrip() for line in file]
    # print(element_array)

show_tokens = True

operators = {
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'STAR',
    '/': 'SLASH'
}

def isNum(element):
        try:
            int(element)
            return True
        except:
            return False

def findToken(elem_array):
    tokens = []

    for element in elem_array:
        if isNum(element):
            tokens.append({
                'type': 'NUM',
                'lexeme': int(element)
            })
        elif element in operators:
            tokens.append({
                'type': operators[element],
                'lexeme': element
            })
        else:
            raise ValueError('Error: Unexpected character: ' + element)
        
    return tokens

def RPN(element_array) -> int:
    stack = []
    token_array = findToken(element_array)
        
    for elem in token_array:
        if elem['type'] == 'NUM':
            stack.append(elem['lexeme'])
        else:
            first_elem = stack.pop()
            last_elem = stack.pop()
            if elem['type'] == "PLUS":
                ans = last_elem + first_elem
            elif elem['type'] == "MINUS":
                ans = last_elem - first_elem
            elif elem['type'] == "STAR":
                ans = last_elem * first_elem
            elif elem['type'] == "SLASH":
                ans = int(last_elem / first_elem)

            stack.append(ans)

    return stack[-1]

try: 
    if show_tokens:
        tk_array = findToken(element_array)
        for each in tk_array:
            print("Token: ", each)
        print("Answer: ", RPN(element_array))
    else:
        print("Answer: ", RPN(element_array))
except ValueError as ve:
    print(ve)