import random
  
# def add_spnoise(img):
  
#     # Getting the dimensions of the image
#     row , col = img.shape
      
#     # Randomly pick some pixels in the
#     # image for coloring them white
#     # Pick a random number between 300 and 10000
#     number_of_pixels = random.randint(300, 10000)
#     for i in range(number_of_pixels):
        
#         # Pick a random y coordinate
#         y_coord=random.randint(0, row - 1)
          
#         # Pick a random x coordinate
#         x_coord=random.randint(0, col - 1)
          
#         # Color that pixel to white
#         img[y_coord][x_coord] = 255
          
#     # Randomly pick some pixels in
#     # the image for coloring them black
#     # Pick a random number between 300 and 10000
#     number_of_pixels = random.randint(300 , 10000)
#     for i in range(number_of_pixels):
        
#         # Pick a random y coordinate
#         y_coord=random.randint(0, row - 1)
          
#         # Pick a random x coordinate
#         x_coord=random.randint(0, col - 1)
          
#         # Color that pixel to black
#         img[y_coord][x_coord] = 0
          
#     return img

# Salt and pepper noise
def add_spnoise(img):
  
    # Getting the dimensions of the image
    row , col = img.shape
    number_of_pixels = (row * col)*5//100 # 5% noisy pixel
    for i in range(number_of_pixels):
        
        # Extreme white
        y_coord_w=random.randint(0, row - 1)
        x_coord_w=random.randint(0, col - 1)
        img[y_coord_w][x_coord_w] = 255

        # Extreme dark
        y_coord_b=random.randint(0, row - 1)
        x_coord_b=random.randint(0, col - 1)
        img[y_coord_b][x_coord_b] = 0
          
    return img