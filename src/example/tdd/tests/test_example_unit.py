import unittest2 as unittest


# ----------------------------------------------------------------------------
# Step 1: Write a test (test_is_palindrome_accepts_palindromic_words)
# Step 2: Make test pass as quickly as possible by just returning True
# (is_palindrome)
# ----------------------------------------------------------------------------

def is_palindrome(input_string):
    return True


class UnitTestIsPalindrome(unittest.TestCase):

    def test_function_should_accept_palindromic_words(self):
        self.assertTrue(is_palindrome("noon"))


# ----------------------------------------------------------------------------
# Step 3: Write a second test
# (test_is_palindrome_does_not_accept_non_palindromic_words)
# Step 4: Make test pass as quickly as possible by adding a real implementation
# ----------------------------------------------------------------------------

def is_palindrome(input_str):

    if input_str == input_str[::-1]:
        return True
    else:
        return False


class UnitTestIsPalindrome(unittest.TestCase):

    def test_function_should_accept_palindromic_words(self):
        self.assertTrue(is_palindrome("noon"))

    def test_function_should_not_accept_non_palindromic_words(self):
        self.assertFalse(is_palindrome("foo"))


# ----------------------------------------------------------------------------
# Step 5: Refactor is_palindrome to eliminate duplication
# ----------------------------------------------------------------------------

def is_palindrome(input_str):
    return input_str == input_str[::-1]


class UnitTestIsPalindrome(unittest.TestCase):

    def test_function_should_accept_palindromic_words(self):
        self.assertTrue(is_palindrome("noon"))

    def test_function_should_not_accept_non_palindromic_words(self):
        self.assertFalse(is_palindrome("foo"))

# ----------------------------------------------------------------------------
# Step 6: Write a third test (test_function_should_ignore_case)
# Step 7: Make sure the test passes by adapting the comparison (is_palindrome)
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


# ----------------------------------------------------------------------------
# TDD: 8. Step
# ----------------------------------------------------------------------------

# ...
