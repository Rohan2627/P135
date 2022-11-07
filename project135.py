import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("profinal.csv")

star = df['Star Name'].tolist()
star.pop(0)

radius = df['Radius'].tolist()
radius.pop(0)

distance = df['Distance'].tolist()
distance.pop(0)

mass = df['Mass'].tolist()
mass.pop(0)

gravity = df['Gravity'].tolist()
gravity.pop(0)


plt.figure(figsize=(10,5))
plt.title("Star VS Mass")
plt.xlabel('Name')
plt.ylabel('Mass')
plt.bar(star[0:9], mass[0:9])


plt.figure(figsize=(10,5))
plt.title("Star VS radius")
plt.xlabel('Name')
plt.ylabel('radius')
plt.bar(star[0:9], radius[0:9])



plt.figure(figsize=(10,5))
plt.title("Star VS Distance")
plt.xlabel('Name')
plt.ylabel('Distance')
plt.bar(star[0:9], distance[0:9])



plt.figure(figsize=(10,5))
plt.title("Star VS Gravity")
plt.xlabel('Name')
plt.ylabel('Gravity')
plt.bar(star[0:9], gravity[0:9])

plt.show()

