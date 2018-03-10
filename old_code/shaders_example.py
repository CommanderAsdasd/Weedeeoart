from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import *
import numpy, math
from PIL import Image


class StereoDepth:

    # constants
    BACKGROUND_IMAGE = 'image_left.png'

    # vertex shader program
    vertexShader = """
        #version 330 core
    
        attribute vec3 vert;
        attribute vec2 uV;
        uniform mat4 mvMatrix;
        uniform mat4 pMatrix;
        out vec2 UV;
    
        void main() {
          gl_Position = pMatrix * mvMatrix * vec4(vert, 1.0);
          UV = uV;
        }
    """

    # fragment shader program
    fragmentShader = """
        #version 330 core
    
        in vec2 UV;
        uniform sampler2D backgroundTexture;
        out vec3 colour;
    
        void main() {
          colour = texture(backgroundTexture, UV).rgb;
        }
    """

    # initialise opengl
    def _init_opengl(self):

        # create shader program
        vs = compileShader(self.vertexShader, GL_VERTEX_SHADER)
        fs = compileShader(self.fragmentShader, GL_FRAGMENT_SHADER)
        self.program = compileProgram(vs, fs)
        glUseProgram(self.program)

        # obtain uniforms and attributes
        self.aVert = glGetAttribLocation(self.program, "vert")
        self.aUV = glGetAttribLocation(self.program, "uV")
        self.uPMatrix = glGetUniformLocation(self.program, 'pMatrix')
        self.uMVMatrix = glGetUniformLocation(self.program, "mvMatrix")
        self.uBackgroundTexture = glGetUniformLocation(self.program, "backgroundTexture")

        # set background vertices
        backgroundVertices = [
            -2.0,  1.5, 0.0, 
            -2.0, -1.5, 0.0,
             2.0,  1.5, 0.0, 
             2.0,  1.5, 0.0, 
            -2.0, -1.5, 0.0, 
             2.0, -1.5, 0.0]

        self.vertexBuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertexBuffer)
        vertexData = numpy.array(backgroundVertices, numpy.float32)
        glBufferData(GL_ARRAY_BUFFER, 4 * len(vertexData), vertexData, GL_STATIC_DRAW)

        # set background UV
        backgroundUV = [
            0.0, 0.0,
            0.0, 1.0,
            1.0, 0.0,
            1.0, 0.0,
            0.0, 1.0,
            1.0, 1.0]

        self.uvBuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.uvBuffer)
        uvData = numpy.array(backgroundUV, numpy.float32)
        glBufferData(GL_ARRAY_BUFFER, 4 * len(uvData), uvData, GL_STATIC_DRAW)

        # set background texture
        backgroundImage = Image.open(self.BACKGROUND_IMAGE)
        backgroundImageData = numpy.array(list(backgroundImage.getdata()), numpy.uint8)
            
        self.backgroundTexture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.backgroundTexture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, backgroundImage.size[0], backgroundImage.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, backgroundImageData)

# setup and run OpenGL
    def main(self):
        glutInit()
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(100, 100)
        glutCreateWindow('Stereo Depth')
        glutDisplayFunc(self._draw_frame)
        self._init_opengl()
        glutMainLoop()

# run an instance of StereoDepth
StereoDepth().main()