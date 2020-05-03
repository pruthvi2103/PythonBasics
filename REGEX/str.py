def process(mul,Str):
    print("\t \t passed",Str)
    ans = ''
    for w in range(len(Str)):
        if Str[w] == '(':
            ans+=process(int(Str[w-1]),Str[w+1:])
        
        elif Str[w] == ')':
            print(ans*mul)
            return(ans*mul)
            
        elif Str[w].isdigit:
            pass
        else:
            print(ans)
            ans+=Str[w]
    return ans

N = int(input())
for x in range(N):
    S = input()
    print(process(1,S))
