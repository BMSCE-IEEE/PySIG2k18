# Author: K Nitesh Srivats
import numpy as np

# import cv2
# image = cv2.imread(input("Enter Image Name: "))


image = np.load("Image.npy")
print(image.shape, len(image))
width, height = map(int, input("Resolution Required: ").split(", "))
wr = image.shape[0] / width
hr = image.shape[1] / height
resized = np.empty((width, height, 3), dtype='uint8')
grayscale = np.empty((width, height), dtype='uint8')

for i in range(width):
    for j in range(height):
        cells = image[int(i * wr): int((i + 1) * wr),
                int(j * hr): int((j + 1) * hr), :]
        for k in range(3):
            resized[i][j][k] = int(
                np.sum(cells[:, :, k]) / (cells.shape[0] * cells.shape[1]))
        grayscale[i][j] = int(resized[i][j][0] * 0.1140 +
                              resized[i][j][1] * 0.5870 +
                              resized[i][j][2] * 0.2989)

# R * 0.2989 + G * 0.5870 + B * 0.1140
# cv2.imshow("Image", resized)
# cv2.waitKey()
