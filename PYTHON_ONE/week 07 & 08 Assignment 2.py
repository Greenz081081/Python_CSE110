#week 08 prove Assignment
from PIL import Image

image_beach = Image.open("beach.jpg")
image_boat = Image.open("boat.jpg")
combined_image = Image.new('RGB', image_beach.size)
pixels_beach = image_beach.load()
pixels_boat = image_boat.load()
pixels_combined = combined_image.load()
width, hieght = image_beach.size
color = pixels_boat[1,1]




for x in range(0, width):
     for y in range(0, hieght):
         (r,g,b) = pixels_boat[x,y]
         if r <= 150 and g >= 215 and b <= 60:
               pixels_boat [x,y] = pixels_beach[x,y]
         elif r <= 120 and g >= 200 and b<= 145:
               pixels_boat [x,y] = pixels_beach[x,y]
         elif r <= 155 and g >= 210 and b <= 155:
               pixels_boat [x,y] = pixels_beach[x,y]
         elif r <= 230 and g >= 254 and b <= 230: 
               pixels_boat [x,y] = pixels_beach[x,y]
         elif r <= 164 and g >= 164 and b <= 84:
               pixels_boat [x,y] = pixels_beach[x,y]
         elif r <= 66 and g >= 120 and b <= 45:
               pixels_boat [x,y] = pixels_beach[x,y]
         elif r <= 130 and g >= 200 and b <= 130:
               pixels_boat [x,y] = pixels_beach[x,y]
         pixels_combined[x, y] = pixels_boat[x,y]
# image_beach.show()
# image_cactus.show()
combined_image.show()
combined_image.save("week_eight_assignment.jpg")