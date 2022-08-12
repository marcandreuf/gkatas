def stringify_numbers(obj):
	for key in obj:
		if type(obj[key]) == int:
			obj[key] = f'{obj[key]}'
		elif isinstance(obj[key], dict):
			obj[key] = stringify_numbers(obj[key])
	return obj

obj1 = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

expected = {
 'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}

def test_stringify_numbers():
	assert stringify_numbers({}) == {}
	assert stringify_numbers({'num':1}) == {'num':'1'}
	assert stringify_numbers(obj1) == expected
	print('test_stringify_numbers Pass')

test_stringify_numbers()
