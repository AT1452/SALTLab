from os import makedirs
import pandas as pd
import matplotlib.pyplot as plt, mpld3
from matplotlib.colors import hsv_to_rgb
from math import atan2, hypot, degrees
from matplotlib import collections as matcoll
from mpld3 import plugins
import numpy as np
import http.server
import socketserver

AUDict = {
  1: "Inner Brow Raise",
  2: "Outer Brow Raise",
  4: "Furrowed Brow",
  6: "Cheek Raiser",
  12: "Lip Corners Raised",
  15: "Lip Corners Depressed",
  20: "Lips Stretched",
  25: "Lips Parted"
}  

def drawAU(num):
  alphas = []
  for pt in data["AU" + str(num)]:
    if pt is 1:
      alphas.append(float(1))
    else:
      alphas.append(float(0))
  fig = plt.figure(figsize=(5, 2))
  plt.ylim([0.9, 1.1])
  plt.title(AUDict[num])
  plt.scatter(x = data['frames_ids'], y = data['AU' + str(num)], s = 7, marker="s", c = np.asarray([(0, 0, 1, a) for a in alphas]))
  mpld3.save_json(fig, "au" + str(num) + ".json")


data = pd.read_csv("./examples/multitask_preds.csv", delimiter=",")

# for pt in data["AU1"]:
#   if pt is 1:
#     alphas.append(float(1))
#   else:
#     alphas.append(float(0))
# fig = plt.figure(figsize=(5, 2))
# plt.ylim([0.9, 1.1])
# plt.scatter(x = data['frames_ids'], y = data['AU1'], s = 7, marker="s", c = np.asarray([(0, 0, 1, a) for a in alphas]))
# mpld3.save_json(fig, "au1.json")
drawAU(1)
drawAU(2)
drawAU(4)
drawAU(6)
drawAU(12)
drawAU(15)
drawAU(20)
drawAU(25)



 
# plt.figure(figsize=(10, 8))
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

# print(angles)


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
fig, ax = plt.subplots()
x = np.arange(0, len(magnitude))
(markers, stemlines, baseline) = plt.stem(magnitude, markerfmt=' ')
plt.setp(stemlines, linestyle="-", color=colors, linewidth=0.5 )
plt.xticks(np.arange(min(x), max(x)+1, 30), rotation=90)

# plt.show()
# plt.plot(x, y)
# fig.show()
# plugins.connect(fig, plugins.MousePosition)
mpld3.save_json(fig, "tester.json")

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as http:
    print("serving at port", PORT)
    http.serve_forever()