# Training Data Preparation
This tools designed to create a set of images cropped from the original images for making an appropriate database of classified images. The graphical interface provided by 'imglab' makes it very easy to use. 

You can use the up and down arrow keys to cycle though the images and the mouse to label objects.  In particular, holding the shift key, left clicking, and dragging the mouse will allow you to draw boxes around the objects you wish to detect.  

Once you finish labeling objects go to the file menu, click save, and then close the program. This will save the object boxes back to the xml file.

Possible usages is to create train/test database for a Neural Network.

## Pre-requisites
    OpenCV (2.4.11 or later)
    imglab tool (see https://github.com/SaswatPadhi/dlib/tree/master/tools/imglab)

## Running
    ./create_training_data.py <dir_for_cropped_images> <file.xml> <path_to_original_images>
    where:
    <dir_for_cropped_images>  - is directory where cropped images will be saved
    <file.xml>                - is an xml file name where the intermediate
                                information will be kept before cropping
    <path_to_original_images> - path to the directory where the original images
                                are located.
