#Imports
import numpy as np
from PIL import Image
import json_lines

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.pth_to_file = annotation_file
        self.trnsfrm = transforms
        self.data = []
        with open(annotation_file, 'r') as read_file:
            for line in json_lines.reader(read_file):
                self.data.append(line)

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.data)

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_png_ann: the segmentation annotation image (in the form of a numpy array) (shape: (1, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image, png segmentation and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the arrays would be (3, H, W) and (1, H, W), respectively.
            3. Scale the values in the arrays to be with [0, 1].
            4. Perform the desired transformations on the image.
            5. Return the dictionary of the transformed image and annotations as specified.
        '''
        img_jpg_pth = "data/" + self.data[idx]["img_fn"]
        img_png_pth = "data/" + self.data[idx]["png_ann_fn"]

        jpg_img = Image.open(img_jpg_pth).convert("RGB")
        # jpg_img.show()
        png_img = Image.open(img_png_pth)
        # jpg_img.show()


        # i = 0
        for object in self.trnsfrm: # Applying transforms
            jpg_img = object(jpg_img)
            # jpg_img.save(f"output/{i}.png")
            # i += 1

        arr_jpg_img = np.asarray(jpg_img)
        arr_jpg_img = np.transpose(arr_jpg_img, (2, 0, 1))
        arr_jpg_img = arr_jpg_img/255

        arr_png_img = np.asarray(png_img)
        arr_png_img = arr_png_img/255
        hgt, wdt = arr_png_img.shape
        arr_png_img = np.reshape(arr_png_img, (hgt, wdt, 1))
        arr_png_img = np.transpose(arr_png_img, (2, 0, 1))


        ans = {}
        ans["image"] = arr_jpg_img
        ans["gt_png_ann"] = arr_png_img
        ans["gt_bboxes"] = []

        for i in self.data[idx]["bboxes"]:
            ans["gt_bboxes"].append([i["category"]] + i["bbox"])

        return ans

if __name__ == '__main__':
    obj = Dataset("Python_DS_Assignment\\data\\annotations.jsonl")
    for i in obj.data:
        print(i["png_ann_fn"])
    print(type(obj.data))
    print(obj[0])