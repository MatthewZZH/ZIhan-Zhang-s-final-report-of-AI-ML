import numpy as np
import matplotlib.pyplot as plt

points = np.genfromtxt('data3.csv', delimiter=',')


x = points[:,0]
y = points[:,1]

plt.scatter(x,y)
plt.show()


def cost_function(w, b, points):
    total_const =
    m = len(points)
    for i in range(m):
        x = points[i,0]
        y = points[i,1]
        total_const += (y - w * x - b) ** 2
    return total_const / m


alpha = 0.0001
init_w = 0
init_b = 0
num_iter = 10


def grad_desc(points, init_w, init_b, num_iter):
    w = init_w
    b = init_b

    cost_list = []
    for i in  range(num_iter):
        cost_list.append(cost_function(w,b,points))
        w, b = step_grad_desc(w,b,alpha,points)
    return [w, b, cost_list]

def step_grad_desc(current_w, current_b, alpha, points):
    sum_grad_b = 0
    sum_grad_w = 0
    m = len(points)

    for i in range(m):
        x = points[i, 0]
        y = points[i, 1]
        sum_grad_w += (current_w * x + current_b - y) * x
        sum_grad_b += (current_w * x + current_b - y) ;

    grad_w = 2 / m * sum_grad_w
    grad_b = 2 / m * sum_grad_b

    update_w = current_w - alpha * grad_w
    update_b = current_b - alpha * grad_b

    return update_w, update_b


w, b, cost_list = grad_desc(points, init_w, init_b, num_iter)
cost = cost_function(w,b,points)

print("theta0 = ", w)
print("theta1 = ", b)
print("loss function = ", cost)
plt.plot(cost_list)
plt.show()


plt.scatter(x,y)
pred_y = (w * x) + b
plt.plot(x,pred_y,c='r')
plt.show()
