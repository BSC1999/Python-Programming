def printParenthesis(str, n):
    if(n > 0):
        _printParenthesis(str, 0,n, 0, 0)
    else:
        print("Enter a valid number")
    return
def _printParenthesis(str, pos, n,open, close):
    if(close == n):
        for i in str:
            print(i, end="")
        print()
        return
    else:
        if(open > close):
            str[pos] = ')'
            _printParenthesis(str, pos + 1, n,open, close + 1)
        if(open < n):
            str[pos] = '('
            _printParenthesis(str, pos + 1, n, open + 1, close)
 
n = int(input("Enetr a number "))
str = [""] * 2 * n
printParenthesis(str,n)
