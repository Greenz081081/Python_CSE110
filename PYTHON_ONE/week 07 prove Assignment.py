#week 07 prove Assignment
from PIL import Image

# image_beach = Image.open ("beach.jpg")
 

# (width, hieght) = image_beach.size
# print(f"Width: {width}")
# print(f"Hieght: {hieght}")


# pixels_beach = image_beach.load()

# print(image_beach.size)
# print(image_beach.format)


# print(pixels_beach[200, 100])


# for y in range(100, 500):
#     for x in range(0, 300):

#        (r, g, b) = pixels_beach[x, y]

      

#        new_blue = b + 800
#        pixels_beach [x, y] = (r, g, new_blue) 
       
       
       

# image_beach.show()


# image_beach.save("the_new_image.jpg")






image_snow =Image.open("snowscape.jpg")

(width, hieght) = image_snow.size
print(f"Width: {width}")
print(f"Hieght: {hieght}")

pixels_snow = image_snow.load()


print(image_snow.size)
print(image_snow.format)

print(pixels_snow[200, 100])

for x in range(0, width):
     for y in range(0, hieght):



      (r,g,b) = pixels_snow[x, y]

      new_red = r + 100
      new_blue = b + 50

      pixels_snow[x, y] = (new_red, g, new_blue )

image_snow.show()
image_snow.save("The_new_snowscape_image.jpg")