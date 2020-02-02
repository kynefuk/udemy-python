import contextlib


class tag(contextlib.ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_tag = '<{}>'.format(self.name)
        self.end_tag = '</{}>'.format((self.name))

    def __enter__(self):
        print(self.start_tag)

    def __exit__(self, *exc_info):
        print(self.end_tag)


with tag('h1'):
    print('content')
