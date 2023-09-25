from custom_pycairo.vector import Vector


class Line:
    def __init__(self, context, x1, y1, x2, y2, draw=False, id=None):
        self.context = context
        self.v1 = Vector([x1, y1])
        self.v2 = Vector([x2, y2])
        self.id = id

    def draw(self):

        self.context.line_to(self.v1.x, self.v1.y)
        self.context.line_to(self.v2.x, self.v2.y)
        return self.context

    def set_id(self, id):
        self.id = id

    def get_linear_interpolation(self, t):
        # y = mx + c
        # dest = (v2-v1)*t + v1
        x = (self.v2.x - self.v1.x) * t + self.v1.x
        y = (self.v2.y - self.v1.y) * t + self.v1.y
        new_vec_point = Vector([x, y])
        print(new_vec_point)
        return new_vec_point


class Polygon:
    def __init__(self, context, coords):  # coords: [ [x,y], [x1,y1],....]
        self.context = context
        self.coords = coords
        self.lines = []

    def draw(self):
        self.context.move_to(self.coords[0][0], self.coords[0][1])

        for i in range(len(self.lines)):
            self.lines[i].draw()
        self.context.close_path()


class Triangle(Polygon):
    def __init__(self, **kwargs):
        Polygon.__init__(self, kwargs['context'], kwargs['coords'])
        self.initialize_lines()

    def initialize_lines(self):
        self.lines.append(
            Line(self.context, self.coords[0][0], self.coords[0][1], self.coords[1][0], self.coords[1][1]))
        self.lines.append(
            Line(self.context, self.coords[1][0], self.coords[1][1], self.coords[2][0], self.coords[2][1]))
        self.lines.append(
            Line(self.context, self.coords[2][0], self.coords[2][1], self.coords[0][0], self.coords[0][1]))

class Rectangle(Polygon):
    def __init__(self, **kwargs):
        Polygon.__init__(self, kwargs['context'], kwargs['coords'])
        self.initialize_lines()

    def initialize_lines(self):
        self.lines.append(
            Line(self.context, self.coords[0][0], self.coords[0][1], self.coords[1][0], self.coords[1][1]))
        self.lines.append(
            Line(self.context, self.coords[1][0], self.coords[1][1], self.coords[2][0], self.coords[2][1]))
        self.lines.append(
            Line(self.context, self.coords[2][0], self.coords[2][1], self.coords[3][0], self.coords[3][1]))
        self.lines.append(
            Line(self.context, self.coords[3][0], self.coords[3][1], self.coords[0][0], self.coords[0][1]))

