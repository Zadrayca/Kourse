from unittest import TestCase, main


class SomeTest(TestCase):

    def test_1(self):
        # 'FOO'.lower() # --> foo

        self.assertEqual('fooo', 'FOO'.lower())

    def test_2(self):

        self.assertTrue('fooo' == 'FOO'.lower())


# проверить функункцию дудикт с помощю unittest

if __name__ == '__main__':
    main()