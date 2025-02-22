import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({'font.size': 18, 'font.family': 'serif', 'font.serif': ['Times New Roman']})
plt.rcParams['mathtext.default'] = 'regular'

plt.figure(figsize=(10, 8))

# 创建数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 绘制等高线图
contour = plt.contourf(X, Y, Z, levels=20, cmap='viridis')
cbar = plt.colorbar(contour)
cbar.set_label('$ J/m^2 $')
plt.title('Contour Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
