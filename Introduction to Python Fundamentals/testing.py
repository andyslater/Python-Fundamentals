#
# 
#
import os
import unittest


def analyze_text(filename):
    """calculate number of lines, words, chars in file

    Args:
        filename: name of file to analyze

    Raises: 
        IOError: if filename can not be read
    """
    with open(filename, mode='r') as f:
        lines = 0
        words = 0 
        chars = 0
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
        return (lines, words, chars)
            


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ''analyze_text()'' function""" 

    def setUp(self):
       """fixture that deates a file for the test mothod to use"""
       self.filename = 'text_analysis_test_file.txt'
       
       """write out the test file"""
       with open(self.filename, 'w') as f:
           f.write('now we are \ntesting \nor any \ncan lon')

    def tearDown(self):
        """deletes files used by the rest methods"""
        try:
            os.remove(self.filename)
        except:
            pass
    
    def test_function_runs(self):
        """Basic test"""
        analyze_text(self.filename)

    def test_counts(self):
        """check line count correct"""
        lines, words, chars = analyze_text(self.filename)
        self.assertEqual(lines, 4)
        self.assertEqual(words, 8)
        self.assertEqual(chars, 36)

    def test_line_count(self):
        """check line count correct"""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_word_count(self):
        """check word count"""
        self.assertEqual(analyze_text(self.filename)[1], 8)

    def test_char_count(self):
        """check word count"""
        self.assertEqual(analyze_text(self.filename)[2], 36)

    def test_no_such_file(self):
        """check no file error"""
        with self.assertRaises(IOError):
            analyze_text('foobar')
        
    def test_no_delete(self):
        """check no file error"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))



if __name__ == '__main__':
    # will search for all test_* functions and run them
    unittest.main()
