# DESCRIPTION: This program takes a folder of images and resizes all the images to the size 400x350
# INPUT : User enters the Path file to the directory containing the images.
# OUTPUT : Images will be resized and replace the original images.
# PYTHON 2.7.16
from PIL import Image  # Import Image function from PIL module
import os,os.path	



def createFile():
	folder_name = raw_input("Enter the name of the image folder that you want to generate html file for :  ")	
	file="/Users/phuntsho/Desktop/Watson/website/Watson-web/gallery_templates/"+folder_name+".html"
	print ("file name is :  %s" % file)  

	# Start writing a new html file for the specific image folder.
	f =open(file, "w+")
	f.write('<!DOCTYPE html>\n\
		<html lang="en">\n\
  		<head>\n\
    	<title>Photon &mdash; Colorlib Website Template</title>\n\
    	<meta charset="utf-8">\n\
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n\
	    <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300i,400,700" rel="stylesheet">\n\
	    <link rel="stylesheet" href="fonts/icomoon/style.css">\n\
	    <link rel="stylesheet" href="css/bootstrap.min.css">\n\
	    <link rel="stylesheet" href="css/magnific-popup.css">\n\
	    <link rel="stylesheet" href="css/jquery-ui.css">\n\
	    <link rel="stylesheet" href="css/owl.carousel.min.css">\n\
	    <link rel="stylesheet" href="css/owl.theme.default.min.css">\n\
	    <link rel="stylesheet" href="css/lightgallery.min.css">    \n\
	    <link rel="stylesheet" href="css/bootstrap-datepicker.css">\n\
	    <link rel="stylesheet" href="fonts/flaticon/font/flaticon.css">\n\
	    <link rel="stylesheet" href="css/swiper.css">\n\
	    <link rel="stylesheet" href="css/aos.css">\n\
	    <link rel="stylesheet" href="css/style.css">\n\
		</head>\n\
		<body>\n\
 		<div class="site-wrap">\n\
    	<div class="site-mobile-menu">\n\
      	<div class="site-mobile-menu-header">\n\
        <div class="site-mobile-menu-close mt-3">\n\
        <span class="icon-close2 js-menu-toggle"></span>\n\
        </div>\n\
      	</div>\n\
      	<div class="site-mobile-menu-body"></div>\n\
    	</div>\n\
    	<header class="site-navbar py-3 border-bottom" role="banner">\n\
		\n\
      	<div class="container-fluid">\n\
        <div class="row align-items-center">\n\
        \n\
        <div class="col-6 col-xl-2" data-aos="fade-down">\n\
        <h1 class="mb-0"><a href="https://phuens.github.io/Watson/" class="text-black h2 mb-0">Phuntsho</a></h1>\n\
        </div>\n\
        <div class="col-10 col-md-8 d-none d-xl-block" data-aos="fade-down">\n\
        <nav class="site-navigation position-relative text-right text-lg-center" role="navigation">\n\
		\n\
        <ul class="site-menu js-clone-nav mx-auto d-none d-lg-block">\n\
        <li><a href="gallery.html">Home</a></li>\n\
        <li class="has-children active">\n\
        <a href="Gallery.html">Gallery</a>\n\
        <ul class="dropdown">\n\
        <li><a href="Tanzania.html">Tanzania</a></li>\n\
        <li><a href="Zanzibar.html">Zanzibar</a></li>\n\
        <li><a href="Rwanda.html">Rwanda</a></li>\n\
        <li><a href="Kenya.html">Kenya</a></li>\n\
        <li><a href="Mauritius.html">Mauritius</a></li>\n\
        <li><a href="Wheaton.html">Wheaton</a></li>\n\
        <li><a href="Portraits.html">Portraits</a></li>\n\
        <li><a href="Misc.html">Misc</a></li>\n\
        </ul>\n\
        </li>\n\
        </ul>\n\
        </nav>\n\
        </div>\n\
		<!-----------------------------------------------------------------------------------------------\n\
		                                 S O C I A L     M E D I A \n\
		------------------------------------------------------------------------------------------------>\n\
        <div class="col-6 col-xl-2 text-right" data-aos="fade-down">\n\
        <div class="d-none d-xl-inline-block">\n\
        <ul class="site-menu js-clone-nav ml-auto list-unstyled d-flex text-right mb-0" data-class="social">\n\
        <li>\n\
        <a href="#" class="pl-0 pr-3"><span class="icon-facebook"></span></a>\n\
        </li>\n\
        <li>\n\
        <a href="#" class="pl-3 pr-3"><span class="icon-twitter"></span></a>\n\
        </li>\n\
        <li>\n\
        <a href="#" class="pl-3 pr-3"><span class="icon-instagram"></span></a>\n\
        </li>\n\
        <li>\n\
        <a href="#" class="pl-3 pr-3"><span class="icon-youtube-play"></span></a>\n\
        </li>\n\
        </ul>\n\
        </div>\n\
        <div class="d-inline-block d-xl-none ml-md-0 mr-auto py-3" style="position: relative; top: 3px;"><a href="#" class="site-menu-toggle js-menu-toggle text-black"><span class="icon-menu h3"></span></a></div>\n\
        </div>\n\
        </div>\n\
      	</div>\n\
  		\n\
   		</header>\n\
   		\n\
		<!-----------------------------------------------------------------------------------------------\n\
		                                 P I C T U R E S \n\
		------------------------------------------------------------------------------------------------>\n\
		<div class="site-section"  data-aos="fade">\n\
		<div class="container-fluid">\n\
		<div class="row justify-content-center">\n\
		<div class="col-md-7">\n\
		<div class="row mb-5">\n\
		<div class="col-12 ">\n\
		</div>\n\
		</div>\n\
		</div>\n\
		</div>\n\
		<div class="row" id="lightgallery">')

#========================================================================================================================
#||||||||||||||||||||||||| G E N E R A T I N G    P I C T U R E S |||||||||||||||||||||||||||||||||||||||||||||||||||||||
#========================================================================================================================



	
	local_path = "../images/gallery/" + folder_name+"/"	
	path = "/Users/phuntsho/Desktop/Watson/website/Watson-web/images/gallery/"+folder_name+"/"
	if not os.path.exists(path):
		print("Path of the file not found! ")
		restart = raw_input("Would you like to restart? Y or N:  ")
		
		if (restart == 'N'):
			print("Thank You")
			exit()	
		createFile()	


	for item in os.listdir(path):					# Loops through all the items in the directoy. 
   		if (item == ".DS_Store"):					# Need this since there is always .DS_Store file. 
   			continue
   		else:
   			im = Image.open(path+item)				# Opens each individual image in the folder.
   			print('working on : ', item)
   			im.save(path+item,"jpeg", optimize=True,quality=50) # image compression
   			#im = Image.open(path+item)				# Opens each individual image in the folder.
   			print(local_path+item)
   			source = '<div class="col-sm-6 col-md-4 col-lg-3 col-xl-2 item" data-aos="fade" data-src="'+local_path + item+'" data-sub-html="\n\
          			<a href="#"><img src="'+local_path + item+'" alt="'+item+'" class="img-fluid"></a>\n\
        			</div>'
   			f.write(source)


#========================================================================================================================
#||||||||||||||||||||||||| G E N E R A T I N G    P I C T U R E S |||||||||||||||||||||||||||||||||||||||||||||||||||||||
#========================================================================================================================
   	f.write('</div>\n\
    	</div>\n\
  		</div>\n\
		<!-----------------------------------------------------------------------------------------------\n\
		                                 F O O T E R \n\
		------------------------------------------------------------------------------------------------>\n\
		\n\
		<script src="js/jquery-3.3.1.min.js"></script>\n\
		<script src="js/jquery-migrate-3.0.1.min.js"></script>\n\
	    <script src="js/jquery-ui.js"></script>\n\
		<script src="js/popper.min.js"></script>\n\
		<script src="js/bootstrap.min.js"></script>\n\
		<script src="js/owl.carousel.min.js"></script>\n\
		<script src="js/jquery.stellar.min.js"></script>\n\
		<script src="js/jquery.countdown.min.js"></script>\n\
		<script src="js/jquery.magnific-popup.min.js"></script>\n\
		<script src="js/bootstrap-datepicker.min.js"></script>\n\
		<script src="js/swiper.min.js"></script>\n\
		<script src="js/aos.js"></script>\n\
		<script src="js/picturefill.min.js"></script>\n\
		<script src="js/lightgallery-all.min.js"></script>\n\
		<script src="js/jquery.mousewheel.min.js"></script>\n\
		<script src="js/main.js"></script>\n\
		\n\
		<script>\n\
    	$(document).ready(function(){$("#lightgallery").lightGallery();});\n\
		</script>\n\
		</body>\n\
		</html>')
	f.close()



def main(): 
	createFile()																	 	 
	

if __name__== "__main__":
  main()
