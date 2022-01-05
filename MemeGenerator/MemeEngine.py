"""Class MemeEngine."""
from PIL import Image, ImageDraw, ImageFont
import random
import time


class MemeEngine:
    """Load image from path and draw a quote on top."""

    def __init__(self, out_path):
        """Init of MemeEngine. OutputPath as argument."""
        self.out_path = out_path

    def make_meme(self, img_path, text=None, author=None, width=500):
        """Create a Postcard With a Text Greeting.

        Arguments:
            in_path {str} -- the file location for the input image.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            x_pos = random.randint(40, width-200)
            y_pos = random.randint(40, height-40)
            draw.text((x_pos, y_pos), f'{text}', font=font, fill='white')
            draw.text((x_pos, y_pos+20), f'-{author}', font=font, fill='white')

        output_path = self.out_path + f'/out{time.time()}.jpg'
        img.save(output_path)
        return output_path
