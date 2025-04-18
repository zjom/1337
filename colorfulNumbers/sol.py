'''
A number can be broken into sub-sequences.

3245 can be broken in to subseqs:
- 3
- 2
- 4
- 5

- 32
- 24
- 45

- 324
- 245

  1   1   1  1 
3   2   4   5
  6   8   20
   24   40


This number is colorful, since product of every digit of a sub-sequence are different.
That is:

3*2 = 6
2*4 = 8
4*5= 20
3*2*4 = 40

But 326 is not a colorful number as it generates:
- 3
- 2
- 6
- 32
- 26

and 3*2=6
'''

def isColorful(n:int)->bool:
    seen:set[int] = set()
    digits:list[int] = []
    stack:list[tuple[int,int]] = []
    for i,c in enumerate(str(n)):
        seen.add(int(c))
        digits.append(int(c))
        if i <len(str(n))-1:
            stack.append((i,int(c)))

    while stack:
        next:list[tuple[int,int]] = []
        for i in range(len(stack)):
            idx,n = stack.pop()
            print(idx,n)
            if idx >= len(digits)-1:
                continue
            num = n*digits[idx+1]
            if num in seen:
                return False
            seen.add(num)
            next.append((idx+1,num))
        stack = next
    return True


isColorful(326)
isColorful(3245)
