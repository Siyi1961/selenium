import unittest
from calculator import Calculator

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j=Calculator(5,10)
        self.assertEqual(j.add(),15)

    def test_add_err(self):
        j=Calculator(5,10)
        self.assertNotEqual(j.add(), 12)

    def test_assertTrue(self):
        j=Calculator(5,10)
        self.assertTrue(j.add()>10)

    def test_assertIn(self):
        self.assertIn("d","hello world")

    def test_assertIs(self):
        self.assertIs("world","hello world")



    def tearDown(self):
        print("test end")

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestMath("test_add"))
    suite.addTest(TestMath("test_add_err"))
    suite.addTest(TestMath("test_assertTrue"))
    suite.addTest(TestMath("test_assertIn"))
    suite.addTest(TestMath("test_assertIs"))

    runner=unittest.TextTestRunner()
    runner.run(suite)

