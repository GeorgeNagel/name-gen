from unittest import TestCase

from name_gen.new_names import generate_name

class TestGenerateName(TestCase):
    def test_anglo_saxon(self):
        name = generate_name('male', 'anglo-saxon')
        self.assertNotEqual(name, '')
