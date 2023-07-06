# Object Counting in Image using Python

This project focuses on counting objects in an image using Python and computer vision techniques. The goal is to develop a program that can automatically detect and count objects of interest within an image. This README file provides an overview of the project, its objectives, and instructions for running the code.

## Project Structure

The project is structured as follows:

```
- images/                   # Directory for storing input images
- results/                  # Directory for storing output images with object count
- count.py           # Python script for object counting
- README.md                 # Project overview and instructions
```

## Getting Started

### Prerequisites

To run the code, make sure you have the following dependencies installed:

- Python 3.6 or higher
- OpenCV (cv2) library
- Numpy library

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/sejalmankar1012/object-counting.git
   ```

2. Navigate to the project directory:

   ```
   cd object-counting
   ```

### Usage

1. Place the image you want to analyze in the `images/` directory.

2. Run the `count.py` script:

   ```
   python count.py --image images/Coins.jpg
   ```

   Replace `your_image.jpg` with the actual image filename you want to analyze.

3. The script will process the image, detect objects, and generate an output image with the object count.

4. The resulting image will be saved in the `results/` directory with the filename `Coins.jpg`.

## Example Output

The output image will display the original image with bounding boxes around the detected objects and the count of objects in the image.

![Example Output](results/your_image_count.jpg)

## Customization

You can customize the code to detect specific objects or modify the visual representation of the output. Feel free to explore and adapt the script according to your specific requirements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The code for object counting in the image was inspired by various computer vision resources and tutorials.

Feel free to modify and extend this project according to your needs. Happy object counting!
