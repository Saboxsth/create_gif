import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames= ['first_img.png','second_img.png','third_img.png','fourth_img.png','fifth_img.png']
images = []
common_size = (1920, 1080)

for filename in filenames:
    try:
        img= Image.open(filename)
        img_resized= img.resize(common_size)
        images.append(np.array (img_resized))
    except FileNotFoundError:
        print(f'Error: File {filename} was not found')

    except Exception as e:
        print(f'An erro occured with {filename}; {e}')

if images :
    iio.imwrite('Tattoo2.gif', images, duration = 500, loop =0)
    print('GIF created successfully!')

else:
    print('No images were load.')