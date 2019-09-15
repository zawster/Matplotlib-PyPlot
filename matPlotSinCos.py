import matplotlib.pyplot as plt

S = np.sin(X)
print(S)

plt.figure()
plt.plot(X, C)
plt.plot(X, S)

plt.figure()
plt.plot(X, C, label='cos')
plt.plot(X, S, label='sin')
plt.xlabel('x')
plt.ylabel('sin(x)/cos(x)')
plt.legend()
