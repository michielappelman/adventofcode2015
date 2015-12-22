#!/usr/bin/env python3
import day1_apartment
import unittest

class TestMoveUpDown(unittest.TestCase):
    known_values = ( ('(())', 0),
                    ('()()', 0),
                    ('(((', 3),
                    ('(()(()(', 3),
                    ('))(((((', 3),
                    ('())', -1),
                    ('))(', -1),
                    (')))', -3),
                    (')())())', -3))
    invalid_values = ( '()a' ,
                        'a(',
                        '&()', 
                        '*kc',
                        '89')

    def test_valid_move_up_down(self):
        for instruction, floor in self.known_values:
            result = day1_apartment.move_up_down(instruction)
            self.assertEqual(floor, result)

    def test_invalid(self):
        for instruction in self.invalid_values:
            self.assertRaises(day1_apartment.NonBracket,
                                day1_apartment.move_up_down,
                                instruction)

if __name__ == "__main__":
    unittest.main()
