import os
import glob
fs = glob.glob("*.jpg")

for i in fs:
    o = i.replace(".jpg", '-cropped.jpg')
    s = 'magick input.jpg -gravity center -extent $(identify -format "%[fx:w/h > 16/9 ? h*16/9 : w]x%[fx:w/h > 16/9 ? h : w*9/16]" input.jpg) output.jpg'
    s = s.replace('input.jpg', i)
    s = s.replace('output.jpg', o)
    s = s.replace('16/9', '1024/576')
    s = s.replace('9/16', '576/1024')
    os.system(s)
    
