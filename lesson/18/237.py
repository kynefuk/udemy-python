class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point ({x}, {y})'.format(x=self.x, y=self.y)
