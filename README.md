# Remove-image-background
Python program to remove image background

Approach:
My approach here is quite simple
1. Convert the given image into its HSV form, so that it will be easy to extract the colors of the object
2.According to the color of the object that we want to extract, we can set the range of the hsv values from low to high,
  depending upon the lighting conditions and object's color.
3.To extract the foreground of the image i have applied the mask to the given image to eliminate the background.The mask
  is nothing but the range of values that i have set for the foreground detection.
4. For segmenting the image i have used 'Bitwise AND' operation and applied the mask over the image.So that the background
   will be removed.

References: https://docs.opencv.org/3.2.0/d0/d86/tutorial_py_image_arithmetics.html
            https://realpython.com/python-opencv-color-spaces

I have tested each test image by changing the hsv values given below, It worked good for 7 images and remaining image's
output has less accuracy.

The range of hsv values for images according the given test images:

Image 1(IMG_20190106_170921.jpg)
Image 2(IMG_20190106_170946.jpg)
Image 4(IMG_20190106_171122.jpg)

lower_green = np.array([10, 0, 60])
upper_green = np.array([92, 255, 255])

----------------------------------------
Image 3(IMG_20190106_171011.jpg)
lower_green = np.array([8, 0, 5])        
upper_green = np.array([120, 150, 150])
----------------------------------------
Image 5 (IMG_20190106_172021.jpg)
lower_green = np.array([30, 0, 30])     
upper_green = np.array([130, 255, 255])
----------------------------------------
Image 6(IMG_20190106_172053.jpg)
Image 7(IMG_20190106_172105.jpg)
lower_green = np.array([6, 0, 60])
upper_green = np.array([150, 255, 255])
----------------------------------------
IMG_20190106_172320.jpg 9
IMG_20190106_172248.jpg 8
lower_green = np.array([5, 100, 50])
upper_green = np.array([120, 255, 250])
----------------------------------------
IMG_20190106_172329.jpg 10
lower_green = np.array([2, 70, 50])  
upper_green = np.array([130, 255, 255])
----------------------------------------
IMG_20190106_172525.jpg 11
lower_green = np.array([50, 0, 50])       
upper_green = np.array([255, 255, 255])
----------------------------------------

IMG_20190106_172607.jpg 12
lower_green = np.array([20, 0, 20])   
upper_green = np.array([100, 255, 255])
