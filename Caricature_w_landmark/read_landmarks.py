import argparse
from PIL import Image, ImageDraw 

## args
parser = argparse.ArgumentParser()
parser.add_argument('Number', type=int, help = "Please input the index of image-landmark pair, from 1-50.", choices = "range: 1-50", default = 10)
args = parser.parse_args()
index = args.Number
img_name = str(index)+ '.jpg'
lan_name = str(index) + '.txt'

## Read landmark and store in land_list
land_list = []
lan_f = open(lan_name, 'r')
for i in range(1,69):
    line = lan_f.readline()
    line = line.strip('\n')
    land_list.append( float(line.split(' ')[0]) )
    land_list.append( float(line.split(' ')[1]) )
    if not line:
        break

## Read Image and draw facial landmarks
Img = Image.open(img_name)
Draw = ImageDraw.Draw(Img)
x_size, y_size = Img.size

  # resize Image
scale = 600.0/x_size
new_x = int(scale*x_size)
new_y = int(scale*y_size)


for i in range(1,68):
    point_x = land_list[2*(i-1)]
    point_y = land_list[2*i-1]
    Draw.rectangle([point_x-1,point_y-1,point_x+1,point_y+1], outline = "red", fill = (255,100,0))

Img = Img.resize((new_x, new_y), Image.ANTIALIAS)
Img.show()
