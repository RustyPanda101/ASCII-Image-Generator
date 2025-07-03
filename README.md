# ASCII Image Generator

This project converts any image into ASCII art and displays it visually using OpenCV.

Example 1:
| orignal | Coloured ASCII | Binary ASCII |
|---------|----------------|--------------|
![dog](https://github.com/user-attachments/assets/10e5aa90-39fd-48d9-8c93-7bef1ab630a3) | ![asciiArt_colour](https://github.com/user-attachments/assets/1ef40567-a7e5-427c-ab50-693358ca01ef) | ![asciiArt_binary](https://github.com/user-attachments/assets/516a1f82-670d-4081-ba95-55622cfc89aa) |
Image from [Brooke Balentine](https://unsplash.com/@brookebalentine)



## Features
- for colour ascii art : use colourImage(<image_array>, <quality_factor>)
- for binary ascii art : use monoChrome(<image_array>, <quality_factor>)
- Converts images to grayscale
- Resizes image to fit ASCII proportions
- Maps brightness to ASCII characters
- Renders ASCII art on a graphical window using OpenCV


## Recommendation
- Adjust the fac value till you find a good value
  
## Requirements
- Python 3.x  
- NumPy  
- OpenCV (`cv2`)

## Installation
```bash
pip install numpy opencv-python
