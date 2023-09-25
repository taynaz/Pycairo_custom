import cairo


class PyContext():
    def __init__(self, surface):
        self.cairo_context = cairo.Context(surface.surface_ctx)

    @property
    def context(self):
        return self.cairo_context
