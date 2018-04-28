from PIL import Image, ImageMath, ImageOps
from PIL.ImageMorph import *
import numpy


def image_colorify(inImg):
	# im = Image.fromarray(np.uint8(cm.gist_earth(inImg)*255))
	im = Image.fromarray(inImg[0], mode="L")
	A = inImg
	B = inImg
	# im1 = Image.open("../../imgShaker/PutinHotdog.jpg").convert('L')
	# im2 = Image.open("../../imgShaker/TerminatroMosquito.jpg").convert('RGBA')
	# background = Image.new('RGBA', im1.size, (255,255,255))
	# lb = LutBuilder(patterns = ["4:(... .1. 111)->1"])
	# out = MorphOp(lut=lb).apply(im1)
	out = A.dot(B)

	# out = Image.alpha_composite(background, im1)
	# out = ImageOps.colorize(im, "red", "black")
	# out = numpy.fromstring(out.tobytes(), dtype=numpy.uint8)
	# out = 10 * numpy.sin(out)
	# out = Image.alpha_composite(out, im2)
	return out



# image_colorify().show()