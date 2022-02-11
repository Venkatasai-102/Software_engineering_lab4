from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.model import InstanceSegmentationModel
from my_package.analysis import plot_visualization
from my_package.data.transforms import BlurImage, RotateImage, RescaleImage, FlipImage, CropImage
from PIL import Image
import numpy as np

annotation_file = r"C:\4th SEM\SOFTWARE ENGINEERING LAB\lab-4\Python_Tkinter_Assignment\data\annotations.jsonl"
transforms = []

# Instantiate the segmentor model.
segmentor = InstanceSegmentationModel()
# Instantiate the dataset.
dtset = Dataset(annotation_file, transforms=transforms)
# Iterate over all data items.
# img_fr_sgmnt = []
# for i in range(len(dtset)):
#     img =  dtset[i]["image"]
#     img_fr_sgmnt.append(img)

img_tst1 = dtset[0]["image"]
# Get the predictions from the segmentor.
# seg_img = []
# for i, item in enumerate(img_fr_sgmnt):
#     seg_img.append(segmentor(item))
#     print(f"Segmentation of image {i} is completed\n")

seg_img_tst = segmentor(img_tst1)
# Draw the segmentation maps on the image and save them.
# for i, item in enumerate(seg_img):
#     # item = list(item)
#     # print(item)
#     # item = sorted(item, key=lambda x:x[3])
#     bbox = item[0]
#     mask = item[1]
#     classes = item[2]
#     img_arr = img_fr_sgmnt[i]*255
#     img_arr = np.transpose(img_arr, (1, 2, 0))
#     img1, img2 = plot_visualization(img_arr, bbox, classes, mask)
#     img1.show()
#     img2.show()

bbox_tst = seg_img_tst[0]
mask_tst = seg_img_tst[1]
class_tst = seg_img_tst[2]
img_arr_tst = img_tst1*255
img_arr_tst = np.transpose(img_arr_tst, (1, 2, 0))
img1_tst, img2_tst = plot_visualization(img_arr_tst, bbox_tst, class_tst, mask_tst)
img1_tst.show()
img2_tst.show()
    # print(f"Masking of image {i} is completed\n")