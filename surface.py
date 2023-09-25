import cairo
import os

class PySurface:
    def __init__(self, width, height, img_type, file_name):
        self.width = width
        self.height = height
        self.img_type = img_type
        self.fullpath = os.getcwd() + '/' + file_name + '.' + self.img_type.lower()
        self.surface = None

        self.init()

    def init(self):
        if self.img_type == 'svg':
            self.create_svg_surface()

    def create_svg_surface(self):
        self.surface = cairo.SVGSurface(self.fullpath, self.width, self.height)
        return self.surface

    @property
    def surface_ctx(self):
        return self.surface
