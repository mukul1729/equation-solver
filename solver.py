class tree:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

token = input("Enter the equation Ex:((2*1)+(3*7)): ")
s = []
for t in token:
    if t in '+*-/':
        s.append(t)
    elif t not in '()':
        s.append(tree(t,None,None))
    elif t == ')':
        right = s.pop()
        op = s.pop()
        left = s.pop()
        s.append(tree(op,left,right))

def evaluate(s):
    if s.left == None and s.right == None:
        return int(s.data)
    else:
        op = s.data
        left = s.left
        right = s.right
        if op == '/':
            return evaluate(left)/evaluate(right)
        elif op == '*':
            return evaluate(left)*evaluate(right)
        elif op == '-':
            return evaluate(left)-evaluate(right)
        else:
            return evaluate(left)+evaluate(right)

print(evaluate(s.pop()))






























