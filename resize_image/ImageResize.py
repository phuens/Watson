# DESCRIPTION: 
# INPUT : 
# OUTPUT :

from PIL import Image 
  
def main(): 
    img  = Image.open("lion.jpeg")  
    width, height = img.size 
    print("width:", width, " height:" ,height);
    img = img.resize((400, 300)) 
    img.save("lion.jpeg")

if __name__== "__main__":
  main()
