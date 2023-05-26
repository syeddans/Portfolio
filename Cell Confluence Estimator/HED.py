import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
from datetime import datetime
from datetime import timedelta


class CropLayer(object):
    def __init__(self, params, blobs):
        # initialize our starting and ending (x, y)-coordinates of
        # the crop
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0

    def getMemoryShapes(self, inputs):
        # the crop layer will receive two inputs -- we need to crop
        # the first input blob to match the shape of the second one,
        # keeping the batch size and number of channels
        (inputShape, targetShape) = (inputs[0], inputs[1])
        (batchSize, numChannels) = (inputShape[0], inputShape[1])
        (H, W) = (targetShape[2], targetShape[3])

        # compute the starting and ending crop coordinates
        self.startX = int((inputShape[3] - targetShape[3]) / 2)
        self.startY = int((inputShape[2] - targetShape[2]) / 2)
        self.endX = self.startX + W
        self.endY = self.startY + H

        # return the shape of the volume (we'll perform the actual
        # crop during the forward pass
        return [[batchSize, numChannels, H, W]]

    def forward(self, inputs):
        # use the derived (x, y)-coordinates to perform the crop
        return [inputs[0][:, :, self.startY:self.endY,
                self.startX:self.endX]]

def load_HED_and_preproccess(microscope_cell_image):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    # Define the paths to the Caffe model files
    protoPath = "deploy.prototxt"
    modelPath = "hed_pretrained_bsds.caffemodel"

    # Load the Caffe model from the files and Register a custom layer named "Crop" using the CropLayer class so that it is properly aligned
    net = cv2.dnn.readNetFromCaffe(protoPath, modelPath)
    cv2.dnn_registerLayer("Crop", CropLayer)
    img = cv2.imread(microscope_cell_image)
    plt.imshow(img)
    # plt.show()

    # Get the dimensions of the image and Calculate the mean pixel values of the image
    (H, W) = img.shape[:2]
    mean_pixel_values = np.average(img, axis=(0, 1))
    blob = cv2.dnn.blobFromImage(img, scalefactor=0.7, size=(W, H),
                                 mean=(mean_pixel_values[0], mean_pixel_values[1], mean_pixel_values[2]),
                                 swapRB=False, crop=False)

    # View the preprocessed image (blob)
    blob_for_plot = np.moveaxis(blob[0, :, :, :], 0, 2)
    plt.imshow(blob_for_plot)
    plt.show()


    net.setInput(blob)
    hed = net.forward()
    hed = hed[0, 0, :, :]
    hed = (255 * hed).astype("uint8")
    plt.imshow(hed, cmap='gray')
    plt.show()
    blur = cv2.GaussianBlur(hed, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    plt.imshow(thresh)
    plt.show()

    area = H*W
    return (thresh, area)

def calculate_Confluence(threshed_image):
    count = cv2.countNonZero(threshed_image[0])
    percent_confluence = 100-((count/(threshed_image[1]))*100)

    return percent_confluence

def timing(current_conflence, splitOrSeed):
    avg_doubletime = 18
    if splitOrSeed == "Split":
        goal_confluence = 60
    else:
        goal_confluence = 80

    timeToGoal = math.log((goal_confluence/current_conflence),2)* avg_doubletime

    return [timeToGoal, avg_doubletime, splitOrSeed, current_conflence]

def output(timing_list):
    current_time = datetime.now()
    time = current_time.strftime("%d/%m/%Y %H:%M")
    ideal_time = current_time + timedelta(hours=timing_list[0])
    ideal_time_format = ideal_time.strftime("%d/%m/%Y %H:%M")
    print(f"If the current cells' state is represented by the given image as of now ({time}),\n"
          f"the confluence is estimated to be: %.2f percent\n"
          f"Assuming a doubling time of {timing_list[1]}hrs, the ideal time the cells will be ready to {timing_list[2]} would be in %.2f hrs,\n"
          f"which would be {ideal_time_format}" % (timing_list[3],timing_list[0]))

output(timing(calculate_Confluence(load_HED_and_preproccess("1.200165.jpg")),"Seed"))









