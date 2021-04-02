import unittest

from source.task_1 import print_depth


class TestTask1:

    def test_with_empty_data(self, capsys):
        data = {}
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == ''
        assert err == ''

    def test_with_single_entry(self, capsys):
        data = {"key": 1}
        print_depth(data)
        out, err = capsys.readouterr()

        assert out == 'key 1\n'
        assert err == ''

    def test_with_mltiple_entries(self, capsys):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }

        print_depth(data)
        out, err = capsys.readouterr()
        assert out == 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n'
        assert err == ''

if __name__ == '__main__':
    unittest.main()
