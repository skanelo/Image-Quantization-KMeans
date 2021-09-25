# Colour Image Quantization using K-means

## About the project
A simple tutorial on how to reduce the number of distinct colours in an image using Python and OpenCV. <br>
>Medium Post: [url-pending].

## Built with
- [OpenCV](https://opencv.org/) (4.5.3)
- [scikit-learn](https://scikit-learn.org/stable/) (1.0)

## Getting Started
### Installation
```git clone https://github.com/skanelo/Image-Quantization-KMeans.git```
### Usage
Open the terminal in the directory where the files are located to <br>
Run: ```python quant.py --image <path_to_your_image.png> --clusters <#_clusters>``` <br>
The quantized image is stored in the current directory as **color_quantization_{#_clusters}.jpg**

## Results
### K = 2
![](https://github.com/skanelo/Image-Quantization-KMeans/blob/main/Results/color_quantization_k_2.jpg)
### K = 4
![](https://github.com/skanelo/Image-Quantization-KMeans/blob/main/Results/color_quantization_k_4.jpg)
### K = 8
![](https://github.com/skanelo/Image-Quantization-KMeans/blob/main/Results/color_quantization_k_8.jpg)
### K = 16
![](https://github.com/skanelo/Image-Quantization-KMeans/blob/main/Results/color_quantization_k_16.jpg)
### K = 32
![](https://github.com/skanelo/Image-Quantization-KMeans/blob/main/Results/color_quantization_k_32.jpg)
### K = 40
![](https://github.com/skanelo/Image-Quantization-KMeans/blob/main/Results/color_quantization_k_40.jpg)
The original image has been taken from the official [My Hero Academia Wiki](https://myheroacademia.fandom.com/wiki/My_Hero_Academia_Wiki).

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Stefanos Kanellopoulos - skanelo.ai@gmail.com
Project Link: [https://github.com/skanelo/Image-Quantization-KMeans](https://github.com/skanelo/Image-Quantization-KMeans)
