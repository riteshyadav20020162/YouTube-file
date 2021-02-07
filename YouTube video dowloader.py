#importing tkinter
from tkinter import *
#importing YouTube module
from pytube import YouTube
#initializing tkinter
root=Tk()
#setting the geometry of the GUI
root.geometry("400×350")
#setting the title of the GUI
root.title("YouTube video downloader application")
#defining download function
def download():
	           #using try and except to execute program without errors
	           try:
	           	myVar.set("Downloading...")
	           	root.update()
	           	YouTube(link.get()).streams.first().download()
	           	link.set("Video download successfully")
	           except Exception as e:
	        	   MyVar.set("Mistake")   	
	        	   root.update()
	        	   limk.set("Enter correct link")
#Created the Label widget to welcom user
Label(root,text="Welcome to youtube\nDownloader Application",font="Consolas 15 bold").pack()
#declaring StringVar type variable
myVar= StringVar()
#setting the default text to myVar
myVar.set("Enter the link below")
#created the Entry widget to ask user to enter the url
Entry(root,textvariable=myVar,width=40).pack(pady=10)
#declaring StringVar type variable
link=StringVar()
#created and called the download  function to download video
Button(root,text="Download video", command=download).pack()
#running the mainloop
root.mainloop()
