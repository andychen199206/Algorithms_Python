#01.Detect first repeated character in a string: Solution1
def first_repeat(str):
    for index, ch in enumerate(str):
      if str[:index+1].count(ch)>1:
        return ch
    return '\0'
first_repeat('iloveindeedindeed')

#01.Detect first repeated character in a string: Solution2
def first(str):
    h={}
    for ch in str:
      if ch in h:
        return ch
      else:
        h[ch]=0
    return'\0'
first('iloveindeed')

#02.Detect a position in a list to make the sum of the right equals to the sum of the left:
def position(li):
    for i in range(len(li)):
        left = li[:i]
        right= li[i+1:]
        lsum = sum(left)
        rsum = sum(right)
        if lsum == rsum:
            return i
    return 'N'
position([1,2,1,1,2])

#03.Longest common subsquence
def lcs(a,b):
    if len(a)==0 or len(b)==0:
        return ' '
    elif a[-1]==b[-1]:
        return lcs(a[:-1],b[:-1])+a[-1]
    else:
        sol_a = lcs(a[:-1],b)
        sol_b = lcs(a,b[:-1])
        if len(sol_a)>len(sol_b):
            return sol_a
        else:
            return sol_b        
k = 'abcdfkc'
j = 'badfkcc'
lcs(k,j)