import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sko.GA import GA
import matplotlib

def schaffer(p):
    '''
    This function has plenty of local minimum, with strong shocks
    global minimum at (0,0) with value 0
    '''
    x11, x21, x31, x41, x51, x61, x12, x22, x32, x42, x52, x62 = p
    return -(
            x11 * 23 + x12 * 23 + x21 * 31 + x22 * 31 + x31 * 15 + x32 * 15 + x41 * 27 + x42 * 27 + x51 * 30 + x52 * 30 + x61 * 19 + x62 * 19)


constraint_ueq1 = (lambda x: x[0] * 60 + x[1] * 83 + x[2] * 38 + x[3] * 71 + x[4] * 80 + x[5] * 52 - 120,
                   lambda x: x[6] * 60 + x[7] * 83 + x[8] * 38 + x[9] * 71 + x[10] * 80 + x[11] * 52 - 140,
                   lambda x: x[0] + x[6] - 1, lambda x: x[1] + x[7] - 1, lambda x: x[2] + x[8] - 1,
                   lambda x: x[3] + x[9] - 1, lambda x: x[4] + x[10] - 1, lambda x: x[5] + x[11] - 1)
num_iteration = 20
num_size_pop = 200
ga = GA(func=schaffer, n_dim=12, size_pop=num_size_pop, max_iter=num_iteration, prob_mut=0.001, lb=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ub=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        constraint_ueq=constraint_ueq1,
        precision=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
best_x, best_y = ga.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)


a = ga.all_history_Y
for i in range(num_iteration):
    a[i] = sum(a[i])/num_size_pop

#因为目标函数是取最小值 在此处要进行转换
for i in range(num_iteration):
    if a[i] < 0:
        a[i] = -a[i]

font = {"family": "Microsoft Yahei", "size": "10"}
matplotlib.rc("font", **font)

# 设置图片大小和清晰度
fig = plt.figure(figsize=(15, 8), dpi=80)
plt.xlabel("迭代次数")
plt.ylabel("每一代种群平均适应度")
plt.xticks(range(1,num_iteration+1))
plt.plot(list(range(1, num_iteration+1)), a, color='orange',linewidth = 4)
plt.show()
