def isPalindrome(strng):	
	if len(strng) <= 1:
		return True
	else:			
		return strng[0] == strng[len(strng)-1] and \
			isPalindrome(strng[1:(len(strng)-1)])


def test_isPalindrome():
	assert True == isPalindrome('')
	assert True == isPalindrome('a')
	assert False == isPalindrome('ab')
	assert True == isPalindrome('aba')
	assert True == isPalindrome('abba')
	assert False == isPalindrome('awesome')
	assert False == isPalindrome('foobar')
	assert True == isPalindrome('tacocat')
	assert True == isPalindrome('amanaplanacanalpanama')
	print('test_isPalindrome Pass')


test_isPalindrome()