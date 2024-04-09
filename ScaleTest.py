import matplotlib.pyplot as plt
from PIL import Image
from mpldatacursor import datacursor

# Load the image
image_path = 'crw.png' 
img = Image.open(image_path)

# Convert the image to a NumPy array
img_array = plt.imread(image_path)

# Plot the image using Matplotlib
fig, ax = plt.subplots()
ax.imshow(img_array)

width, height = img.size
print(width, height)

# Use mpldatacursor to display coordinates on hover
datacursor(display='multiple', draggable=True)

# Show the plot
plt.show()
