jsonk
=====

JSONK (short for JSON with linKs) is a way of defining links between JSON
data files for efficient reuse. For example, suppose we have two files,
`location.json` and `coordinates.json`:

location.json:
```
{
	"name": "White House"
}
```

coordinates.json:
```
{
	"longitude": "38.8977° N", 
  "latitude": "77.0366° W"
}
```

We can define a `.jsonk` file, `location.jsonk`, which imports the coordinates
from `coordinates.json`, like so:

location.jsonk:
```
{
	"name": "White House",
  "coordinates": "@coordinates.json"
}
```

If opened with the `jsonk` library, this file is parsed into:
```python
>>> import jsonk
>>> jsonk.load(open('./location.jsonk'))
{'coordinates': {'latitude': '77.0366° W', 'longitude': '38.8977° N'}, 'name': 'White House'}
```

.jsonk files may also reference other .jsonk files.  Importantly, filepaths are
evaluated relative to the file being parsed. This means that if one .jsonk file
references a .jsonk file in another directory, the links in the second file are
relative to the location of the second file, not the first.

In the case of jsonk.loads, paths are evaluated as relative to the current
directory (alternately, you can pass cwd='blah' to specify a different current
directory).
