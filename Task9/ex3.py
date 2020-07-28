def f(x, y):
    return (-x**2+y**2)

x = torch.linspace(-6, 6, 30)
y = torch.linspace(-6, 6, 30)
X, Y = torch.meshgrid(x,y )
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.scatter(X, Y, Z,c=Z.flatten(),cmap='viridis', linewidth=0.5);
plt.axis('off');