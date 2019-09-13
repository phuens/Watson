# DESCRIPTION: This program takes a folder of images and resizes all the images to the size 400x350
# INPUT : User enters the Path file to the directory containing the images.
# OUTPUT : Images will be resized and replace the original images.
# PYTHON 2.7.16
from PIL import Image  # Import Image function from PIL module
import os,os.path	


def start():
	path = "/Users/phuntsho/Desktop/Watson/website/Watson-web/images/gallery/"  # Defualt the path for the directory.  
	if not os.path.exists(path):
		print("Path of the file is Invalid")	
	return (path)


def createFile(path):
	file="/Users/phuntsho/Desktop/Watson/website/Watson-web/gallery.html"
	f =open(file, "w+")
	f.write('\
		<!DOCTYPE html>\n\
			<html lang="en">\n\
			<head>\n\
			    <meta charset="UTF-8">\n\
			    <title>Gallery</title>\n\
			    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n\
			    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>\n\
			    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>\n\
			    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\n\
			    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">\n\
			    <link href="https://fonts.googleapis.com/css?family=Bungee+Outline|Raleway|Hanalei|Darker+Grotesque|Monoton|ZCOOL+KuaiLe|Major+Mono+Display|Slabo+27px|Staatliches|Patrick+Hand" rel="stylesheet">\n\
			    <script src="js/gallery.js"></script>\n\
			    <link rel="stylesheet" href="css/gallery.css">\n\
			</head>\n\
			<body>\n\
			    <div class="container">\n\
			        <div  class="row justify-content-center">\n\
			            <div class="col-lg-12 col-md-12 col-sm-12">\n\
			                <h1 class="header"> Gallery </h1>\n\
			            </div>\n')


	local_path = "images/gallery/"										
	for item in os.listdir(path):					# Loops through all the items in the directoy. 
   		if (item == ".DS_Store"):					# Need this since there is always .DS_Store file. 
   			continue
   		else:
   			#im = Image.open(path+item)				# Opens each individual image in the folder.
   			source = "<div class='col-lg-6 col-md-6 col-sm-12'><img alt=" + item + " src=" + local_path + item + "></div>\n"
   			f.write(source)

   	f.write('	</div>\n\
    		</div>\n\
		</body>\n\
	</html>\n')
	f.close()



def main(): 
	path = start()
	file = createFile(path)																	 	 
	

if __name__== "__main__":
  main()