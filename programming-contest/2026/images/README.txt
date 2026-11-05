aspect ratio:
       identify -format "%[fx:w/h]\n" pics-2025-cropped.jpg

1.77778

crop image to aspect ratio

1024x??? aspect ratio 1.77778 => 1024/??? = 1.77778
                              => ??? = 1024/1.7778 = 576
                              

magick 2026-lunch.jpg -gravity Center -crop 1024x576+0+0 2026-lunch-cropped.jpg


convert input.jpg -gravity center -extent $(identify -format "%[fx:w/h > 1024/576 ? h*1024/576 : w]x%[fx:w/h > 1024/576 ? h : w*576/1024]" input.jpg) output.jpg

2026-lunch.jpg

main.py
import os
i = '2026-awards.jpg'
o = i.replace(".jpg", '-cropped.jpg')
s = 'convert input.jpg -gravity center -extent $(identify -format "%[fx:w/h > 16/9 ? h*16/9 : w]x%[fx:w/h > 16/9 ? h : w*9/16]" input.jpg) output.jpg'
s = s.replace('input.jpg', i)
s = s.replace('output.jpg', o)
s = s.replace('16/9', '1024/576')
s = s.replace('9/16', '576/1024')
os.system(s)
