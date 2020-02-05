import pytest
import calculation_162


is_release = True


# pytestでtest_*.pyを全て実行してくれる
# テストコード内のprint文を出力するには-s を付けて実行する
class TestCal:
    # テストクラス作成時の前処理
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation_162.Cal()
        cls.test_filename = 'test.txt'

    # テストクラス破棄時の後処理
    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    # 各テストメソッドが実行前の前処理
    def setup_method(self, method):
        print('hoge')
        print(f'{method.__name__=}')
        print('method={}'.format(method.__name__))

    # 各テストメソッドの実行後の後処理
    def teardown_method(self, method):
        print(f'{method.__name__=}')
        print('method={}'.format(method.__name__))

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

    # fixtureのrequestを使う
    def test_add_num_and_double_os_name(self, request):
        os_name = request.config.getoption('--os-name')
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')

    # fixtureのtmpdirを使う
    # pytestがtmpディレクトリを生成してくれる
    def test_save(self, tmpdir):
        print(tmpdir)
        self.cal.save(tmpdir, self.test_filename)
        test_filepath = os.path.join(tmpdir, self.test_filename)
        assert os.path.exists(test_filepath) is True

    # テストをスキップ
    @pytest.mark.skip(reason='とりあえずskip')
    def test_add_num_and_double_skip(self):
        pass

    # 条件に応じてテストをスキップ
    @pytest.mark.skipif(is_release is True, reason='とりあえずskip')
    def test_add_num_and_double_skip_if(self):
        pass
