import unittest2 as unittest


# ----------------------------------------------------------------------------
# TDD: 1. Step (Make Test pass as quickly as possible)
# ----------------------------------------------------------------------------
def is_palindrome(input_string):
    return True


class UnitTestIsPalindrome(unittest.TestCase):

    def test_function_should_accept_palindromic_words(self):
        self.assertTrue(is_palindrome("noon"))


# ----------------------------------------------------------------------------
# TDD: 2. Step
# ----------------------------------------------------------------------------
def is_palindrome(input_str):
    return input_str == input_str[::-1]

class UnitTestIsPalindrome(unittest.TestCase):

    def test_function_should_accept_palindromic_words(self):
        self.assertTrue(is_palindrome("noon"))

    def test_function_should_not_accept_non_palindromic_words(self):
        self.assertFalse(is_palindrome("foo"))


# ----------------------------------------------------------------------------
# TDD: 3. Step
# ----------------------------------------------------------------------------
def is_palindrome(input_str):
    return input_str.lower() == input_str[::-1].lower()

class UnitTestIsPalindrome(unittest.TestCase):

    def test_function_should_accept_palindromic_words(self):
        self.assertTrue(is_palindrome("noon"))

    def test_function_should_not_accept_non_palindromic_words(self):
        self.assertFalse(is_palindrome("foo"))

    def test_function_should_ignore_case(self):
        self.assertTrue(is_palindrome("Noon"))
