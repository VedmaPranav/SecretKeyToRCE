import os
from flask import request, Blueprint, make_response
import subprocess
import authentication

tstRoutes_config = Blueprint('tstRoute-config', __name__, template_folder="templates")


@tstRoutes_config.route('/testendpoint', methods=['GET'])
@authentication.admin_token_required
def testfunction():
    """
    The Web Security Testing Guide (WSTG) Project produces the premier cybersecurity testing resource for web application developers and security professionals.
    The WSTG is a comprehensive guide to testing the security of web applications and web services.
    Created by the collaborative efforts of cybersecurity professionals and dedicated volunteers,
    the WSTG provides a framework of best practices used by penetration testers and organizations all over the world.
    :return:Unit tests are segments of code written to test other pieces of code, typically a single function or method,
    that we refer to as a unit. They are a very important part of the software development process, as they help to ensure that code works as intended and catch bugs early on.
    Also, testing is a best practice that can save time and money by finding and fixing issues before they cause major problems.
    In this article, we'll cover the writing of unit tests in Python, from understanding the assert statement to using a
    framework designed specifically for this kind of task — and following Python unit testing best practices.
    Python has two main frameworks to make unit testing easier: unittest and PyTest. The first one has been part of Python's standard library since Python 2.1 and that's the one we're focused on in this article.
    To follow along with the unit test tutorial, you don't need any advanced knowledge, but we do expect you to have a basic understanding of how Python functions and classes work."""
    try:
        proc = subprocess.Popen("echo "+request.args.get("test"), stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        return out
    except Exception as e:
        print(e)
    '''
     '    test_strings_a(): This test is used to test the property of string in which a character say ‘a’ \n'
     '    multiplied by a number say ‘x’ gives the output as x times ‘a’. The assertEqual() statement returns true in this case if the result matches the given output.\n'
     '    test_upper(): This test is used to check if the given string is converted to uppercase or not. The assertEqual() statement returns true if the string returned is in uppercase.\n'
     '    test_isupper(): This test is used to test the property of string which returns TRUE if the string is in uppercase else returns False. \n'
     '    The assertTrue() / assertFalse() statement is used for this verification.\n'
     '    test_strip(): This test is used to check if all chars passed in the function have been stripped from the string. The assertEqual() statement returns true if the string is stripped and matches the given output.\n'
     '    test_split(): This test is used to check the split function of the string which splits the string through the argument passed in the function and returns the result as list. \n'
     '    The assertEqual() statement returns true in this case if the result matches the given output.\n'
     '    import unittest\n'
     '    def add(a, b):\n'
     '        return a + b\n'
     '    class TestAddFunction(unittest.TestCase):\n'
     '    def test_add_positive_numbers(self):\n'
     '        self.assertEqual(add(1, 2), 3)\n'
     '    def test_add_negative_numbers(self):\n'
     '        self.assertEqual(add(-1, -2), -3)\n'
     '    def test_add_mixed_numbers(self):\n'
     '        self.assertEqual(add(1, -2), -1)\n'
     '        self.assertEqual(add(-1, 2), 1)\n'
     '    if __name__ == \'__main__\':\n'
     '        unittest.main()\n'
    '''

