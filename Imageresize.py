# DESCRIPTION: This program takes a folder of images and resizes all the images to the size 400x350
# INPUT : User enters the Path file to the directory containing the images.
# OUTPUT : Images will be resized and replace the original images.
# PYTHON 2.7.16
from PIL import Image  # Import Image function from PIL module
import os,os.path	


def start():
	user_input = raw_input("Do you want to change the directory? \n Y or N:  ")		 # User Input 
	if (user_input == 'Y' ): 														 # Change default directory
		path = raw_input("Enter the full file path (starting with /Users/):  ")		
		print("PATH:  %s" % path)
	else:
		path = "/Users/phuntsho/Desktop/Watson/website/Watson-web/images/projects/"  # Defualt the path for the directory.  

	if not os.path.exists(path):
		print("Path of the file is Invalid")
		restart = raw_input("Would you like to restart? Y or N:  ")
		
		if (restart == 'N'):
			print("Thank You")
			exit()	
		start()

	return (path)


def main(): 
	path = start()																	 	 
	dirs = os.listdir( path ) 						# dirs stores all the file names in the 
													#directory of the path variable.
	#print(dirs)							
	image_count = 0									# Keep track of amount of images formatted.

	#*********************************************
	#size = 400, 350 # FOR HOMEPAGE COVER		 *
	size = 265,400	 # FOR BOOKS IN BOOK REVIEW  *
	#*********************************************

	for item in os.listdir(path):					# Loops through all the items in the directoy. 
   		if (item == ".DS_Store"):					# Need this since there is always .DS_Store file. 
   			continue
   		else:
   			im = Image.open(path+item)				# Opens each individual image in the folder.
   			width, height = im.size					# Stores the original width and height of the image.				
   			print("Image name: %s...  width:  %d. height:  %d" % (item[0:10],width,height))	# Print original width and height of the image with the name.
   			img = im.resize(size,Image.ANTIALIAS)	# Resizes each image into the set given size(400x350)
   			img.save(path+item,"png",optimize=True,quality=50) 			# Saves the image as its orginial filename in its original folder. 
   			image_count = image_count +1			# Counter.
	
	print("------------------")						# Just a Done message.
	print("Formated %d images" % image_count)
	print("------------------")


if __name__== "__main__":
  main()