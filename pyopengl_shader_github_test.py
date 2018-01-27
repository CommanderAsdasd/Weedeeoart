import sys
import glfw
from PyQt4 import QtGui
from OpenGL.GL import *
from OpenGL.GL.shaders import *
import numpy


def main():
    # take monitor wight and height
    app = QtGui.QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width = screen_rect.width() - 300
    height = screen_rect.height() - 300

    # initilize glfw
    if not glfw.init():
        return

    window = glfw.create_window(width, height, "My openGL window", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    triangle = [-0.8, -0.8, 0.0,
               0.0, 0.8, 0.0,
               0.8, -0.8, 0.0]

    triangle = numpy.array(triangle, dtype=numpy.float32)

    vertex_shader = """
    #version 330
    in vec4 position;
    void main(){
        gl_Position = position;
    }
    """

    fragment_shader = """
    #version 330
    void main(){
        gl_FragColor = vec4(1.0f, 1.0f, 1.0f, 1.0f);
    }
    """
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 36, triangle, GL_STREAM_DRAW)  # GL_STREAM_DRAW GL_STATIC_DRAW

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)  # !!!!!!
    glEnableVertexAttribArray(position)

    glUseProgram(shader)

    glClearColor(0.32, 0.83, 1.0, 0.5)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glDrawArrays(GL_TRIANGLES, 0, 3)  # !!!!!!

        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == '__main__':
    main()