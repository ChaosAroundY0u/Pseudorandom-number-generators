import numpy as np
import matplotlib.pyplot as plt

points = [[24, 7], [20, 2], [10, -3], [5, 5], [-2, 0], [0, -3], [30, -30], [15, -15], [7, 7], [2, -4]]
points2 = np.array(points)
x = points2[:, 0]
y = points2[:, 1]

def rotate(A,B,C):
  return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])

plt.figure(1)
plt.scatter(x, y)
plt.grid(True)

def graham(A):
    n = len(A)
    P = list(range(n))
    for i in range(1, n):
        if A[P[i]][0] < A[P[0]][0]:
            P[i], P[0] = P[0], P[i]
            
    for i in range(2, n):
        j = i
        while j > 1 and (rotate(A[P[0]], A[P[j-1]], A[P[j]]) < 0):
            P[j], P[j-1] = P[j-1], P[j]
            j -= 1
            
    S = [P[0], P[1]]
    
    for i in range(2, n):
        while rotate(A[S[-2]], A[S[-1]], A[P[i]]) < 0:
            del S[-1]
        S.append(P[i])
    return S

numbers = graham(points2)
sorted_points = []
for i in range(len(numbers)):
    sorted_points.append(points[numbers[i]])
sorted_points.append(points[numbers[0]])
sorted_points = np.array(sorted_points)
print(sorted_points)
x_p = sorted_points[:, 0]
y_p = sorted_points[:, 1]

plt.scatter(x_p, y_p, color = "r")
plt.plot(x_p, y_p, color = "green")

plt.grid(True)
