class Cal:
    def add_num_and_double(self, x, y):
        result = x + y
        return result * 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
