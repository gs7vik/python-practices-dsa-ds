import numpy as np
a=[2,0,0]
b=[2,0,0]

def cosine_sim(a,b):
    cal_dot = np.dot(a,b)
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)
    sim = cal_dot / (mag_a*mag_b)
    print(sim)
    return sim
    
x = cosine_sim(a,b)
cosine_dis = 1 - x
print(cosine_dis)
    