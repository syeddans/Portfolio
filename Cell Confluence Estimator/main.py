import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import measure
import pandas as pd

img = cv2.imread("1.200165.jpg", 0)
plt.imshow(img)
canny = cv2.Canny(img,10,40)
plt.imshow(canny)

blur = cv2.GaussianBlur(canny, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
plt.imshow(thresh)
#
# n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh, connectivity=4)
#
# colours = np.random.randint(0, 255, size=(n_labels,3), dtype=np.uint8)
# colours[0] = [0,0,0]
# false_colours= colours[labels]
# plt.imshow(false_colours)
#
#
# MAX_AREA = 10000
# false_colours_area_filtered = false_colours.copy()
# for i, centroid in enumerate(centroids[1:],start=1):
#     area = stats[i,4]
#     if area > MAX_AREA:
#         cv2.drawMarker(false_colours_area_filtered, (int(centroid[0]),int(centroid[1])), color=(255, 255, 255), markerType=cv2.MARKER_CROSS)
#
#
# plt.imshow(false_colours_area_filtered)
# plt.show()
#
#
#
# props = measure.regionprops_table(labels, intensity_image=img,
#                               properties=['label',
#                                           'area', 'equivalent_diameter',
#                                           'mean_intensity', 'solidity'])
# df = pd.DataFrame(props)
# total_area= 0
# for x in range(len(df)):
#     if df.iloc[x]['area'] < MAX_AREA:
#         total_area = total_area + df.iloc[x]['area']
#         print(df.iloc[x]['area'])


contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
total_area = 0
for cnt in contours:
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    if area < 50000:
        total_area = total_area + area + perimeter
        img1 = cv2.drawContours(img, [cnt], -1, (255, 0, 0), 3)
    else:
        img1 = cv2.drawContours(img, [cnt], -1, (0, 0, 0), 3)
        bigarea = area
        print(area)

plt.imshow(img1)
plt.show()

from PIL import Image


width, height = Image.open("1.100164.jpg").size
imagearea = width*height


print(total_area)
print(imagearea)
print(bigarea+total_area)
print((total_area/imagearea)*100)