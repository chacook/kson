# Kson - A simple json printing CLI tool.

## To run:
1. Run `python3 <filename.json> <comma-separated-node-names-or-paths>`

## Examples
Given a JSON file named `input.json`:
```
{
	"boxers": [
		{
			"name": "floyd",
			"age": 26,
			"stats": {
				"reach": 72
			}
		},
		{
			"name": "bernard",
			"age": 41,
			"stats": {
				"reach": 75
			}
		}
	]
}
```
You can use a node name on its own: 

`python3 main.py input.json reach`

Or a disambiguated node path: 

`python3 main.py input.json stats.reach`

Or a full node path: 

`python3 main.py input.json boxers.stats.reach`

All of which return:
```
boxers.stats.reach: 72
boxers.stats.reach: 75
```

You can also print multiple nodes by comma separating the node name/disambiguated path/full path:

`python3 main.py input.json name,reach`

Which returns:
```
boxers.name: "floyd"
boxers.age: 26
boxers.name: "bernard"
boxers.age: 41
```

