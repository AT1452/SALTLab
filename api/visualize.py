from os import makedirs
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
# plt.scatter(x, y)
# plt.xlabel('Valence'); plt.ylabel('Arousal')

av_coords = []
angles = []
colors = []
magnitude = []


for (v, a) in zip(data['valence'], data['arousal']):
  if(np.isnan(v) or np.isnan(a)):
    continue
  else:
    av_coords.append((v, a))
    magnitude.append(hypot(v, a))
    deg = (degrees(atan2(a, v)) + 360) % 360;
    angles.append(deg)

for angle in angles:
  colors.append(hsv_to_rgb([angle/360, 1, 1]))


# plt.vlines(x=0, ymin=-1, ymax=1, 
#            colors='red', linewidth=2)
# plt.hlines(y=0, xmin=-1, xmax=1,
#            colors='red', linewidth=2)

# plt.grid(True)
# x = np.arange(0, len(magnitude))
# lines = []
# for i in range(len(x)):
#     pair=[(x[i],0), (x[i], magnitude[i])]
#     lines.append(pair)

# # linecoll = matcoll.LineCollection(lines)
# # fig, ax = plt.subplots()
# # ax.add_collection(linecoll)
# fig, ax = plt.subplots()
# fig.subplots_adjust(bottom=0.2)
# plt.xticks(rotation=90) 
# ax.stem(x, magnitude, markerfmt=' ', linefmt=colors)

# plt.scatter(x,magnitude,c=colors)

# plt.xticks(x)
# plt.ylim(0,30)
x = np.arange(0, len(magnitude))
(markers, stemlines, baseline) = plt.stem(magnitude, markerfmt=' ')
plt.setp(stemlines, linestyle="-", color=colors, linewidth=0.5 )
plt.xticks(np.arange(min(x), max(x)+1, 30), rotation=90)

plt.show()