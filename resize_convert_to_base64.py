#! python

import os
import base64
from PIL import Image
from io import BytesIO

'''

 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
June 2022

This script is designed to do the following:

1. Take the image path as input from the user
2. Convert the image down to a smaller size
3. Output a text file of a decoded base64 value of the image

'''

def get_image_path():

    '''Return the image path from the user'''

    image_path = input("Enter the path of the image that needs to be converted: ").replace('"', "")
    image_location = os.path.normpath(image_path)

    return image_location


def resize_image(image_path):

    '''This function will resize the inputted image and outputted to a different size'''

    resize_x = int(1920 / 4)
    resize_y = int(1080 / 4)

    original_image = Image.open(image_path)

    new_image = original_image.resize((resize_x, resize_y))

    return new_image


def convert_to_base_64(image_object):

    '''This function will expect a PIL image object and then return the decoded base64 vers of image'''
    buffered = BytesIO()

    image_object.save(buffered, format='PNG')
    image_base64_str = base64.b64encode(buffered.getvalue()).decode()
    
    data_image_str = "data:image/png;base64,"

    return data_image_str + image_base64_str


def get_stream_package_location():

    '''This function will simply grab the stream package location and set that as an available path.'''
    get_input_package = input("Enter the folder location of the rendered Stream Package: ").replace('"', "")
    stream_package_location = os.path.normpath(get_input_package)
     
    return stream_package_location


def output_to_text_file(project_path, base64_string):

    '''This will output the base64 string into a text file inside the project folder'''

    base_64_text_file = "image_base64_value.txt"

    if (project_path):

        text_file_path = os.path.join(project_path, base_64_text_file)

        with open(text_file_path, 'w') as file:
            file.write(base64_string)
        
        return True


def main():

    # First get the image path from the user
    image = get_image_path()
    # Resize the Image
    resized_image = resize_image(image)
    # Get the base64 string of the image
    base64_string = convert_to_base_64(resized_image)
    # Get the project path for the project
    project_path = get_stream_package_location()
    # Output the base64 string into a text file inside the project folder
    output_to_text_file(project_path, base64_string)


if __name__ == "__main__":
    main()