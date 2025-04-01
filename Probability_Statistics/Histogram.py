import matplotlib.pyplot as plt

data = list(map(int, input().split()))
plt.his(data, bins=5, color='green')
plt.show()
