import numpy as np 
import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def test_name(name):
	return bool(name.isalnum())

def save_pct():
	if (not test_name(entr.get())):
		messagebox.showerror('Error!', 'Filename is wrong! Must be a-zA-Z1-9')
	else:
		cv2.imwrite(entr.get()+'.jpg',frame_to_save)
cam = cv2.VideoCapture(0)
root = tk.Tk()
root.title("DZ3")
lsave = tk.Label(root,text="Enter filename:")
s = tk.Scale(root, label='Brightness', from_=0, to=255, orient=tk.HORIZONTAL, length=500,  resolution=1)
btm=tk.Button(text="Save frame",command=save_pct)
entr = tk.Entry(width=50)
s.set(128)
lmain = tk.Label(root)
s.grid(row=2,column=0,columnspan=2,sticky='wnse')
lmain.grid(row=3,column=0,columnspan=2,sticky='wnse')
lsave.grid(row=0,column=0,sticky='wnse')
entr.grid(row=0,column=1,sticky='wnse')
btm.grid(row=1,column=0,columnspan=2,sticky='wnse')
while(True):
	cam_sc, frame = cam.read()
	if(cam_sc):
		brt=s.get()
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		if (brt<128):
			hsv[:,:,2] = np.where((hsv[:,:,2]) > (128-brt),hsv[:,:,2]-(128-brt),0)
		elif (brt>128):
			hsv[:,:,2] = np.where((255 - hsv[:,:,2]) < (brt-128),255,hsv[:,:,2]+(brt-128))
		else:
			pass
		frame_to_save  = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
		frame  = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
		img = Image.fromarray(frame)
		imgtk = ImageTk.PhotoImage(image=img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		root.update()
		root.bind("<q>", lambda event: root.destroy())
	else:
		messagebox.showerror('Error!', 'Cam is not available!')
		break   
cam.release()