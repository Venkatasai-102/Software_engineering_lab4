####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.model import InstanceSegmentationModel
from my_package.analysis import plot_visualization
from my_package.data.transforms import BlurImage, RotateImage, RescaleImage, FlipImage, CropImage
from PIL import Image as imgshow

####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from tkinter import *
from functools import partial
from PIL import ImageTk
from tkinter import filedialog
import numpy as np
import warnings
warnings.filterwarnings("ignore")
# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, dataset, segmentor):

	####### CODE REQUIRED (START) #######
	# This function should pop-up a dialog for the user to select an input image file.
	# Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
	# Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
	# Once the output is computed it should be shown automatically based on choice the dropdown button is at.
	# To have a better clarity, please check out the sample video.
	global file_path
	global root
	global image_segmented
	global image_boundary_boxes
	global original_image
	global img1, img2, img3
	global img_lbl1, img_lbl2

	file_path = filedialog.askopenfilename(initialdir="./data/imgs/", title="select a file", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("jpeg files", "*.jpeg"), ("all files", "*.*")))

	original_image = imgshow.open(file_path)

	img_arr = np.asarray(original_image)/255
	img_arr = np.transpose(img_arr, (2, 0, 1))

	sgmnt = segmentor(img_arr)

	bboxes = sgmnt[0]
	masks = sgmnt[1]
	classes = sgmnt[2]
	img_arr = np.transpose(img_arr, (1, 2, 0))*255
	img_list = list(plot_visualization(img_arr, bboxes, classes, masks))
	image_segmented = img_list[0]
	image_boundary_boxes = img_list[1]
	img1 = ImageTk.PhotoImage(original_image)
	img2 = ImageTk.PhotoImage(image_boundary_boxes)
	img3 = ImageTk.PhotoImage(image_segmented)
	
	if clicked.get() == "Segmentation":
		img_lbl1 = Label(image=img1).grid(row=2, column=0)
		img_lbl2 = Label(image=img3).grid(row=2, column=1)
	else:
		img_lbl1 = Label(image=img1).grid(row=2, column=0)
		img_lbl2 = Label(image=img2).grid(row=2, column=1)

	print("Image processing is completed")
	####### CODE REQUIRED (END) #######

# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):

	####### CODE REQUIRED (START) #######
	# Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
	# Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
	# Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.
	global file_path
	global original_image
	global image_segmented
	global image_boundary_boxes
	global root
	global img1, img2, img3
	global img_lbl1, img_lbl2

	if file_path == "":
		print("Please select a file to process.")
		return
	
	# original_image.show()
	# image_segmented.show()
	# image_boundary_boxes.show()

	img1 = ImageTk.PhotoImage(original_image)
	img2 = ImageTk.PhotoImage(image_boundary_boxes)
	img3 = ImageTk.PhotoImage(image_segmented)
	
	if clicked.get() == "Segmentation":
		img_lbl1 = Label(image=img1).grid(row=2, column=0)
		img_lbl2 = Label(image=img3).grid(row=2, column=1)
	else:
		img_lbl1 = Label(image=img1).grid(row=2, column=0)
		img_lbl2 = Label(image=img2).grid(row=2, column=1)
	####### CODE REQUIRED (END) #######

# `main` function definition starts from here.
if __name__ == '__main__':

	####### CODE REQUIRED (START) ####### (2 lines)
	# Instantiate the root window.
	# Provide a title to the root window.
	root = Tk()
	root.title("Image Segmentation and Bounding Boxes")
	root.minsize(200, 100)
	####### CODE REQUIRED (END) #######

	# Setting up the segmentor model.
	annotation_file = './data/annotations.jsonl'
	transforms = []

	# Instantiate the segmentor model.
	segmentor = InstanceSegmentationModel()
	# Instantiate the dataset.
	dataset = Dataset(annotation_file, transforms=transforms)

	
	# Declare the options.
	options = ["Segmentation", "Bounding-box"]
	clicked = StringVar()
	clicked.set(options[0])

	e = Entry(root, width=30)
	e.grid(row=0, column=0)

	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
	file_path = ""
	file_browse_btn = Button(root, text="open a file", command=partial(fileClick, clicked, dataset, segmentor)).grid(row=0, column=0, padx=3, pady=1)
	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button
	drop_box_btn = OptionMenu(root, clicked, *options).grid(row=0, column=1, padx=3, pady=1)

	# Declared an exit button
	exit_btn = Button(root, text="exit", command=root.quit).grid(row=1, column=1, padx=3, pady=1)
	####### CODE REQUIRED (END) #######

	# This is a `Process` button, check out the sample video to know about its functionality
	myButton = Button(root, text="Process", command=partial(process, clicked))
	myButton.grid(row=1, column=0)

	
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
	root.mainloop()
	####### CODE REQUIRED (END) #######