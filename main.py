import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
print(a)
print(b)

boxes = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
sold_boxes = np.array([4, 2, 3, 4, 7, 3, 1])

plt.plot(boxes, sold_boxes, marker='o', color='blue')
plt.title("Boxes Sold Per Day")
plt.xlabel("Day")
plt.ylabel("Boxes Sold")
plt.show()