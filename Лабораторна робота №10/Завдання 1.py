import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 8)
y = 5*np.sin(10*x)*np.sin(3*x)/(x**x)
plt.plot(x,y,label = 'Y(x)=5*sin(10*x)*sin(3*x)/(x^x), x=[0...8]', color = 'purple', linewidth = 2)
plt.title('Function', fontsize = 20)
plt.xlabel('x', fontsize = 20)
plt.ylabel('y', fontsize = 20)
plt.legend(loc = 'best', fontsize = 10)
plt.show()