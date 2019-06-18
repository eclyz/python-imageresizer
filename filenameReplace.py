from PIL import Image

from resizeimage import resizeimage


with open('a.jpeg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [216, 297])
        cover.save('test-image-cover.jpeg', image.format)

