'''Tk_Canvas_Image_url.py
display an image obtained from an internet web page in Tkinter
tested with Python27 and Python33  by  vagaseat   21nov2012
'''
#Important requires Pillow module install as : "pip install pillow"
#warning " Stackoverflow code i didn't wrote this "

from io import BytesIO
import base64
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
    from PIL import Image,ImageTk
root = tk.Tk()
root.title("Image on ID card!")
# a little more than width and height of image
w = 520
h = 320
x = 80
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# this GIF picture previously downloaded to tinypic.com
idno = input("Enter id number:")
extensionlol = ".jpg"
imageurl = "http://exams.kluniversity.in/photos/"               
image_url = imageurl+idno+extensionlol
print(image_url)
#commented lines i dont know i didnt wrote this don't ask
#image_url = "http://i46.tinypic.com/r9oh0j.gif"
#image_byt = urlopen(image_url).read()
#image_b64 = base64.encodestring(image_byt)
#photo = tk.PhotoImage(data=image_b64)
#-----added mitai
with urlopen(image_url) as u:
    raw_data = u.read()
im = Image.open(BytesIO(raw_data))
image = ImageTk.PhotoImage(im)
label = tk.Label(image=image)
label.pack()

# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')
# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
#can cange image size here if needed max size 200x250 exam site lol 
cv.create_image(200, 250, image=image, anchor='nw')
root.mainloop()
