def collect_strings(obj):
	acc = []
	for key in obj:
		if isinstance(obj[key], str):
			acc.append(obj[key])
		elif isinstance(obj[key], dict):
			acc.extend(collect_strings(obj[key]))
	return acc


obj0 = {"stuff": 'foo'}

obj1 = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}


def test_collect_strings():
	assert collect_strings({}) == []
	assert collect_strings(obj0) == ['foo']
	assert collect_strings(obj1) == \
		['foo', 'bar', 'baz']
	print('test_collect_strings Pass')

test_collect_strings()

