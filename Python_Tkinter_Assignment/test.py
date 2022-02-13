from calendar import c
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.model import InstanceSegmentationModel
from my_package.analysis import plot_visualization
from my_package.data.transforms import BlurImage, RotateImage, RescaleImage, FlipImage, CropImage
from PIL import ImageTk
from PIL import Image as imgshw
import numpy as np
from tkinter import *
from tkinter import filedialog

# img_a = imgsf.open("./data/imgs/0.jpg")
# img_a.show()
root = Tk()
root.title("To test")
# root.geometry("400X400")
root.minsize(100, 100)
label = Label(root)

def open1():
    global root
    global image_1
    global img_label
    global my_btn3

    filename = filedialog.askopenfilename(initialdir="./data/imgs/", title="select a file", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("all filese", "*.*")))
    lbl = Label(root, text="some text").grid(row=1, column=0)
    image_1 = ImageTk.PhotoImage(imgshw.open(filename))
    my_btn3 = Button(root, text="process", command=prcss, state=NORMAL).grid(row=0, column=2, padx=3, pady=1)
    img_label = Label(image=image_1).grid(row=2, column=1)

def prcss():
    global root
    global drop_box
    global label
    global clicked
    
    label = Label(root)
    label.destroy()
    
    if drop_box.get() == "segmentor":
        label = Label(root, text=drop_box.get()+" is selected").grid(row=2, column=1)
    else:
        label = Label(root, text=drop_box.get()+" is selected").grid(row=2, column=1)

options = ["segmentor", "boundary boxes"]
drop_box = StringVar()
drop_box.set(options[0])
filename = None

my_btn1 = Button(root, text="open a file", command=open1).grid(row=0, column=0, padx=3, pady=1)


drop = OptionMenu(root, drop_box, *options).grid(row=0, column=1, padx=3, pady=1)

# label = Label(root, text="The selected text is printed here").grid(row=2, column=1)
# my_btn2 = Button(root, text="segmentor").grid(row=0, column=5, padx=3, pady=1)
my_btn3 = Button(root, text="process", command=prcss, state=DISABLED).grid(row=0, column=2, padx=3, pady=1)

my_btn4 = Button(root, text="exit", command=root.quit).grid(row=1, column= 1, padx=3, pady=1)

root.mainloop()

# annotation_file = r"C:\4th SEM\SOFTWARE ENGINEERING LAB\lab-4\Python_Tkinter_Assignment\data\annotations.jsonl"
# transforms = []

# # Instantiate the segmentor model.
# segmentor = InstanceSegmentationModel()
# # Instantiate the dataset.
# dtset = Dataset(annotation_file, transforms=transforms)
# # Iterate over all data items.
# # img_fr_sgmnt = []
# # for i in range(len(dtset)):
# #     img =  dtset[i]["image"]
# #     img_fr_sgmnt.append(img)

# img_tst1 = dtset[1]["image"]
# # Get the predictions from the segmentor.
# # seg_img = []
# # for i, item in enumerate(img_fr_sgmnt):
# #     seg_img.append(segmentor(item))
# #     print(f"Segmentation of image {i} is completed\n")

# seg_img_tst = segmentor(img_tst1)
# # Draw the segmentation maps on the image and save them.
# # for i, item in enumerate(seg_img):
# #     # item = list(item)
# #     # print(item)
# #     # item = sorted(item, key=lambda x:x[3])
# #     bbox = item[0]
# #     mask = item[1]
# #     classes = item[2]
# #     img_arr = img_fr_sgmnt[i]*255
# #     img_arr = np.transpose(img_arr, (1, 2, 0))
# #     img1, img2 = plot_visualization(img_arr, bbox, classes, mask)
# #     img1.show()
# #     img2.show()

# bbox_tst = seg_img_tst[0]
# mask_tst = seg_img_tst[1]
# class_tst = seg_img_tst[2]
# img_arr_tst = img_tst1*255
# img_arr_tst = np.transpose(img_arr_tst, (1, 2, 0))
# img1_tst, img2_tst = plot_visualization(img_arr_tst, bbox_tst, class_tst, mask_tst)
# img1_tst.show()
# img2_tst.show()
#     # print(f"Masking of image {i} is completed\n")