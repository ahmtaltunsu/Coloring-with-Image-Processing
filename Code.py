import cv2
import time

image_paths = [
    'images/00125v.jpg',
    'images/00149v.jpg',
    'images/00153v.jpg',
    'images/00351v.jpg',
    'images/00398v.jpg',
    'images/01112v.jpg'
]
color_image_paths = []

start_time = time.time()

for i, path in enumerate(image_paths):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    height = image.shape[0] // 3

    blue_channel = image[0:height]
    green_channel = image[height:2*height]
    red_channel = image[2*height:3*height]

    color_image = cv2.merge((blue_channel, green_channel, red_channel))

    color_image_path = f'images/coloredimage{i+1}.jpg'
    color_image_paths.append(color_image_path)

    cv2.imwrite(color_image_path, color_image)

end_time = time.time()

total_time = end_time - start_time
print(total_time)

