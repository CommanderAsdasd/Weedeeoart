#coding:utf-8
#gvec4 imageLoad(gimage image​, IMAGE_COORD);
# import 
from OpenGL.GL import *
from PIL import Image

imagefilegl1 = Image.open("../imgShaker/kBln55mIDH8.jpg")
xsize, ysize, image = imagefilegl1.size[0], imagefilegl1.size[1], imagefilegl1.tobytes("raw", "RGBX", 0, -1)
textureone = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, textureone)
glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
glTexImage2D(
	GL_TEXTURE_2D, 0, 3, xsize, ysize, 0,
	GL_RGBA, GL_UNSIGNED_BYTE, image
)

glClear(GL_COLOR_BUFFER_BIT)
if textureflag == 1:
	count = 0
	while count < quadnum:
		if pz[texture[count][0]] < look and pz[texture[count][1]] < look and pz[texture[count][2]] < look and pz[texture[count][3]] < look:
			coltemp = colour[count]
			textemp = texture[count]
			a = textemp[0]
			b = textemp[1]
			c = textemp[2]
			d = textemp[3]
			glEnable(GL_TEXTURE_2D)
			glBindTexture(GL_TEXTURE_2D, colour[count])
			glBegin(GL_QUADS)
			glTexCoord2f(0.0, 0.0); glVertex2f(px[a], py[a]);
			glTexCoord2f(0.0, 1.0); glVertex2f(px[b], py[b]);
			glTexCoord2f(1.0, 1.0); glVertex2f(px[c], py[c]);
			glTexCoord2f(1.0, 0.0); glVertex2f(px[d], py[d]);
			glEnd()
			glDisable(GL_TEXTURE_2D)
			count += 1
			glFlush()