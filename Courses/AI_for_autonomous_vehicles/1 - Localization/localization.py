# 5-9
p = [0.2,0.2,0.2,0.2,0.2] # Uniform distribution
# Z = 'red'   # 24
# Z = 'green' # 25

# p = [0, 1, 0, 0, 0]
world = ['green','red','red','green','green']
measurements = ['red', 'red'] # 26
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
motion = [1,1]
#  We have built the measurement update function 16-24
def sense(p, Z):
    q=[]
    
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i]*(hit*pHit + (1-hit)*pMiss))
    s = sum(q)

    for i in range(len(p)):
        q[i] = q[i]/s
    
    return q

# for k in range(len(measurements)):
#     p = sense(p, measurements[k])

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + (pOvershoot * p[(i-U-1) % len(p)])
        s = s + (pUndershoot * p[(i-U+1) % len(p)])
        q.append(s)
    return q

pos = 1 
p = move(p,pos)
# p = move(p,pos)
# p = move(p,pos)
# p = move(p,pos)
# p = move(p,pos)
# p = move(p,pos)
# p = move(p,pos)
# p = move(p,pos) # 45

# 46 - Essence of google's localization code
for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motion[k])

print(p)
