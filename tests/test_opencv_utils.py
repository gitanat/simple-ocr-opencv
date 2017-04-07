import unittest
import opencv_utils
from files import ImageFile


class TestOpenCVUtils(unittest.TestCase):
    def test_opencv_brightness_raise(self):
        image = ImageFile('digits1')
        processor = opencv_utils.BrightnessProcessor(brightness=2.0)
        self.assertRaises(AssertionError, lambda: processor._process(image.image))

    def test_opencv_brightness(self):
        image = ImageFile('digits1')
        processor = opencv_utils.BrightnessProcessor(brightness=0.5)
        processor._process(image.image)
        # TODO: Add checking and try display() function
        # TODO: Verify the result

    # TODO: Check other ImageProcessors

    def test_opencv_imageprocesser(self):
        processor = opencv_utils.ImageProcessor()
        self.assertRaises(NotImplementedError, lambda: processor._image_processing(object))