import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.colors import hsv_to_rgb
from math import atan2, hypot, degrees
from matplotlib import collections as matcoll
import numpy as np



data = pd.read_csv("./examples/multitask_preds.csv", delimiter=",")

data.plot(x='frames_ids')
 
plt.figure(figsize=(10, 8))
#  xy 
x, y = data['valence'], data['arousal']
plt.scatter(x, y)
plt.xlabel('Valence'); plt.ylabel('Arousal')

av_coords = []
angles = []
colors = []
magnitude = []
for (x, y) in zip(data['valence'], data['arousal']):
  av_coords.append((x, y))
  magnitude.append(hypot(x, y))
  deg = (degrees(atan2(y, x)) + 360) % 360;
  angles.append(deg)

for angle in angles:
  colors.append(hsv_to_rgb([angle/360, 1, 1]))



plt.vlines(x=0, ymin=-1, ymax=1, 
           colors='red', linewidth=2)
plt.hlines(y=0, xmin=-1, xmax=1,
           colors='red', linewidth=2)

# plt.grid(True)
# x = np.arange(0, )

# lines = []
# for i in range(len(x)):
#     pair=[(x[i],0), (x[i], y[i])]
#     lines.append(pair)

# linecoll = matcoll.LineCollection(lines)
# fig, ax = plt.subplots()
# ax.add_collection(linecoll)

# plt.scatter(x,y)

# plt.xticks(x)
# plt.ylim(0,30)

plt.show()