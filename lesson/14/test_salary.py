import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        # apiをモック化する
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)

    # @mock.patch('salary.ThirdPartyBonusAPI.bonus_price', return_value=1)
    @mock.patch('salary.ThirdPartyBonusAPI.bonus_price')
    def test_calculation_salary_mock(self, mock_bonus):
        # 第二引数に指定した任意の変数名がモックオブジェクトとなる
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    def test_calculation_salary_mock_with(self):
        # withブロック内だけmock化する
        with mock.patch(
            'salary.ThirdPartyBonusAPI.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    def test_calculation_salary_mock_patcher(self):
        patcher = mock.patch('salary.ThirdPartyBonusAPI.bonus_price')
        # start()からstop()の間だけmock化する
        mock_bonus = patcher.start()
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()
        patcher.stop()

    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBonusAPI.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary_mock_side_effect(self):

        def mock_return_value(self):
            return 1

        # モックオブジェクトの戻り値が複雑な場合は
        # side_effectで戻り値を定義した関数を指定する
        self.mock_bonus.side_effect = mock_return_value

    # クラスごとモック化する spec=Trueでクラス内の全てのプロパティをモック化
    @mock.patch('salary.ThirdPartyBonusAPI', spec=True)
    def test_calculation_salary_mock_class(self, mock_rest):
        # return_valueでモック対象のクラスのインスタンスが返る
        mock_rest = mock_rest.return_value
        mock_rest.bonus_price.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)