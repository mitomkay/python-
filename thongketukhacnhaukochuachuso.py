n = int(input())
m = {}
for k in range(n) :
    s = ''
    for i in input().lower() + ' ' :
        if not(i.isalpha()) :
            if(s != '') :
                if s in m : m[s] += 1
                else : m[s] = 1
                s = ''
        else : s += i
m = sorted(m.items(), key = lambda x: (-x[1], x[0]))
for i in m :
    print(i[0], i[1])