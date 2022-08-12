def nestedEvenSum(obj, sum=0):
	for key in obj:
		if type(obj[key]) == int:
			num = obj[key]
			if num%2 == 0:
				sum += num
		elif isinstance(obj[key], dict):
			sum = nestedEvenSum(obj[key], sum)
	return sum

obj0 = {"outer": 2, "obj": {"inner": 2}}
obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def test_nested_even_sum():
	assert nestedEvenSum({}) == 0	
	assert nestedEvenSum({"outer": 2}) == 2
	assert nestedEvenSum({"outer": 2, "a": 3}) == 2	
	assert nestedEvenSum(obj0) == 4	
	assert nestedEvenSum(obj1) == 6	
	assert nestedEvenSum(obj2) == 10
	print('test_nested_even_sum Pass')

test_nested_even_sum()
