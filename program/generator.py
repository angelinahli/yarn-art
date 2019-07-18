# name: generator.py
# desc: Programs to generate a yarn pattern given an image and calibration details
# date: 07/18/2019
# auth: Angelina Li

import cv2
from typing import List, TypeVar

class StitchSize:
    # stores the size of a stitch in cm
    def __init__(self, height: float, width: float):
        self.height = height # in cm
        self.width = width

    def __str__(self):
        return "<StitchSize: height={}cm; width={}cm>".format(
            self.height, self.width)

    @staticmethod
    def get_size_from_swatch(
            swatch_height: float, swatch_width: float, 
            num_rows: int, stitches_per_row: int):
        # assumes height and width are in CM; row_size: stitches per row
        height = swatch_height / num_rows
        width = swatch_width / stitches_per_row 
        return StitchSize(height, width)

class Pattern:
    """
    Represents a pattern with a pixel height of `pixel_height` and pixel
    """
    SIZE_TYPE = TypeVar("StitchSize", bound=StitchSize)

    def __init__(
            self, image_url: str, stitch_size: SIZE_TYPE, 
            width: int, height: int=None):
        self.image_url = image_url
        self.stitch_size = stitch_size
        self.width = width # in stitches

        init_image = cv2.imread(image_url, cv2.IMREAD_COLOR)

        self.height = height
        if(self.height == None):
            init_height, init_width, d = init_image.shape
            scale = self.width / init_width
            self.height = int(scale * init_height)
        self.image = cv2.resize(init_image, (self.height, self.width))

    def __str__(self):
        return "<Pattern: image_url={}; height={}sts; width={}sts>".format(
            self.image_url, self.height, self.width)

    @staticmethod
    def get_pattern_from_cm(
            image_url: str, stitch_size: SIZE_TYPE, 
            width_in_cm: float, height_in_cm: float=None):
        width = int(width_in_cm / stitch_size.width)
        height = None if height_in_cm == None else \
                 int(height_in_cm / stitch_size.height)
        return Pattern(image_url, stitch_size, width=width, height=height)

if __name__ == "__main__":
    stitch_size = StitchSize.get_size_from_swatch(
        swatch_width=14, swatch_height=7.6, 
        num_rows=12, stitches_per_row=19)
    image_url = "test/images/sunflower.png"
    image_width = 100. # cm
    print(stitch_size)
    pattern = Pattern.get_pattern_from_cm(image_url, stitch_size, image_width, image_width)
    print(pattern)
    # cv2.imshow("image", pattern.image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
