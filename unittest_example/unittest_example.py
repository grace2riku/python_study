# pythonでユニットテストを書くにはunittestモジュールを使用する
import unittest

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count
    
# テストケースを作成するにはunit.TestCaseを継承したクラスを作成し、
# testで始まる名前のテストメソッドを記述する
class CounterTest(unittest.TestCase):
    # 各テストの実行前
    # 各テストの共通コードを記述することができる。
    # 今回は共通コード特になしのためpassと記述している
    def setUp(self):
        pass

    # 各テストの実行後
    def tearDown(self):
        pass

    def test_increment(self):
        c = Counter()
        c.increment()
        self.assertTrue(c.get_count() == 1)
        c.increment()
        self.assertTrue(c.get_count() == 2)

    def test_decrement(self):
        c = Counter()
        c.decrement()
        self.assertTrue(c.get_count() == -1)
        c.decrement()
        self.assertTrue(c.get_count() == -2)

if __name__ == '__main__':
    unittest.main() # unittest.main関数を呼び出すことでテストメソッドを自動実行する 
