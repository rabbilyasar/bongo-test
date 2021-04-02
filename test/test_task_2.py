from _pytest import python
import pytest
from source.task_2 import print_depth, Person

class TestTask2:

    @pytest.fixture
    def person_a(self):
        return Person('David', 'Attenborough', None)

    @pytest.fixture
    def person_b(self, person_a):
        return Person('Jessie', 'Pinkman', person_a)

    def test_with_empty_dict(self, capsys):
        data = {}
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == ''
        assert err == ''

    def test_with_single_dict(self, capsys):
        data = {
            "name": 1
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == 'name 1\n'
        assert err == ''

    def test_nested_dict(self, capsys):
        data = {
            "rolling": {
                "thunder": "chaw"
            }
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == 'rolling 1\nthunder 2\n'
        assert err == ''

    def test_with_multiple_nested_dict(self, capsys):
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

    def test_with_one_person(self, capsys, person_a):
        print_depth(person_a)
        out, err = capsys.readouterr()
        assert out == 'David 1\nAttenborough 1\nNone 1\n'
        assert err == ''

    def test_with_mixed_data(self, capsys, person_b):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                }
            },
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            'key1 1\n'
            'key2 1\n'
            'key3 2\n'
            'key4 2\n'
            'key5 3\n'
            'user 3\n'
            'Jessie 4\n'
            'Pinkman 4\n'
            'David Attenborough None 4\n'
            'David 1\n'
            'Attenborough 1\n'
            'None 1\n'
        )
        assert err == ''