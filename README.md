# Convert Resize Image To Base64

Feel free to use. This script will expect an image path, and then where you want to export the base64 text file to. Currently this supports png images, but converting over to JPEG/other formats should be trivial.

Also feel free to change the resize of the image under `resize_image()`

### Dependencies

- PIL: [pip install Pillow](https://pypi.org/project/Pillow/)



### Run

```
python resize_convert_to_base64.py
```

### Example Output

Example Input image of 1920 by 1080 resolution
![example_image](/images/example.png)

Output of image with 480 by 270 resolution as a decoded base64 text file
![output](/images/output.png)

### Test your base64 string

Many websites online to check your base64 string. [Here is one for example](https://codebeautify.org/base64-to-image-converter)

![test](/images/test.png)