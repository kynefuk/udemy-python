import unittest

from calculation_162 import Cal


release_name = 'hoge'


class CalTest(unittest.TestCase):

    def setUp(self):
        print('setup')
        self.cal = Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    def test_add_num_and_double(self):
        actual = self.cal.add_num_and_double(1, 1)
        expected = 4
        self.assertEqual(expected, actual)

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

    @unittest.skip('skipします')
    def test_add_num_and_double_skip(self):
        pass

    @unittest.skipIf(release_name == 'hoge', 'skipします')
    def test_add_num_and_double_skip_if(self):
        pass


# python test_162.py でユニットテストを実行できるようになる
if __name__ == '__main__':
    unittest.main()
