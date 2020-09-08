import numpy as np
import matplotlib.pyplot as plt
import control as c
import signal as sg

#tf = c.TransferFunction([51, 50], [40, 25])
tf = c.TransferFunction([2640, 8420, 4275], [1056, 3500, 2500])
mag, phi, w = c.bode(tf)
T, y_ir = c.impulse_response(tf)
T, y_sr = c.step_response(tf)
Impulse = np.zeros(T.shape);Impulse[0] = 1
Step = np.ones(T.shape)

plt.plot(w, mag, label = "Bode's Magnitude")
plt.legend()
plt.grid()
plt.savefig("./Varshit/figs2/Bode's Magnitude.jpg")
plt.close()

plt.plot(w, phi, label = "Bode's Phase")
plt.legend()
plt.grid()
plt.savefig("./Varshit/figs2/Bode's Phase.jpg")
plt.close()

plt.plot(T, y_ir, label = 'Impulse Response')
plt.plot(T, Impulse, label = 'Impulse')
plt.legend()
plt.grid()
plt.savefig('./Varshit/figs2/Impulse Response.jpg')
plt.close()

plt.plot(T, y_sr, label = 'Step Response')
plt.plot(T, Step, label = 'Step')
plt.legend()
plt.grid()
plt.savefig('./Varshit/figs2/Step Response.jpg')
