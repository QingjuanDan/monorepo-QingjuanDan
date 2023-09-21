# README.md for CustomJSON Package

## Description

The CustomJSON package provides enhanced JSON encoding and decoding features, allowing the serialization and deserialization of Python's `datetime.datetime` and `range` objects, which are not supported by the default JSON package. It achieves this through custom JSON encoder and decoder classes, `CustomJSONEncoder` and `CustomJSONDecoder`.

## Installation

To use the CustomJSON package, you can copy the CustomJSONEncoder and CustomJSONDecoder classes along with the dumps and loads functions into your project. 

If a formal package is created, the installation would usually be done using pip:

pip install customjson

## Usage

### Encoding

```python
import json
import datetime
from customjson import dumps

data = {
    "datetime": datetime.datetime(2023, 9, 21, 12, 34, 56),
    "range": range(1, 5)
}

json_str = dumps(data)
print(json_str)
```

### Decoding

```python
from customjson import loads

decoded_data = loads(json_str)
print(decoded_data)
```

## Examples

### CustomJSONEncoder

The `CustomJSONEncoder` class can encode `datetime.datetime` objects to ISO format strings and `range` objects to lists.

```python
import datetime
from customjson import CustomJSONEncoder

encoder = CustomJSONEncoder()

datetime_obj = datetime.datetime(2023, 9, 21, 12, 34, 56)
range_obj = range(1, 5)

print(encoder.default(datetime_obj))  # Outputs: '2023-09-21T12:34:56'
print(encoder.default(range_obj))  # Outputs: [1, 2, 3, 4]
```

### CustomJSONDecoder

The `CustomJSONDecoder` class can decode ISO format strings to `datetime.datetime` objects and lists to `range` objects.

```python
from dateutil import parser
from customjson import CustomJSONDecoder, loads

decoder = CustomJSONDecoder()

datetime_str = '2023-09-21T12:34:56'
range_list = [1, 2, 3, 4]

json_str = '{"datetime": "2023-09-21T12:34:56", "range": [1, 2, 3, 4]}'

decoded_obj = loads(json_str, cls=CustomJSONDecoder)

print(decoded_obj)  # Outputs: {'datetime': datetime.datetime(2023, 9, 21, 12, 34, 56), 'range': range(1, 5)}
```

## Note

Ensure you have the `dateutil` package installed in your environment as it is required for decoding datetime strings back to datetime objects. You can install it using pip:

```sh
pip install python-dateutil
```

## Disclaimer

This README is for illustrative purposes, and the package/installation instructions are hypothetical unless a real package has been created and hosted on a package index such as PyPI.
# TODO Please edit the following information in your assignment

- Name:
- How many hours did it take you to complete this assignment?
- Did you collaborate with any other students/TAs/Professors?
- Did you use any external resources? (Cite them below)
  - tbd
  - tbd
- (Optional) What was your favorite part of the assignment?
- (Optional) How would you improve the assignment?

# Implementation Logistics

- You may use whatever operating system, IDE, or tools for completing this assignment.
- In the future there may be restrictions, so please review here.

# Part(s) to this assignment!

See the folders [part1](./part1) and [part2](./part2) for this assignment. **You should complete the assignment in order**

# Rubric

  <table>
  <tbody>
    <tr>
      <th>Points</th>
      <th align="center">Description</th>
    </tr>
      <td>50% (Part 1 - extend the json library to support complex and range objects)</td>
	        <td ><ul>
              <li>You must import the json standard library so that you can extend the json.JSONEncoder and json.JSONDecoder classes</li>
              <li>Read the Python [documentation](https://docs.python.org/3/library/json.html) for examples on how to serialize unsupported objects</li>
              <li>You must have tests that check if complex and range objects can be both serialized and deserialized</li>
            </ul></td>
    </tr>
  </tbody>
</table>

  <table>
  <tbody>
    <tr>
      <th>Points</th>
      <th align="center">Description</th>
    </tr>
	 <tr>
		<td>10% (Part 2) Publishing to Github</td>
		<td align="left"><ul>
            <li>Using your Github personal account, create a new, empty public repo named `jsonapi`</li>
              <li>When your work is finished, push your 'main' branch to that repo on Github</li>
              <li>Create a tag called 'v0.0.1' from the main branch on Github</li>
              <li>Create your first release notes using the tag; publish the release notes on Github</li>
        </ul></td>
	  </tr>
	<tr>
    	<td>40% (Part 2) Packaging and Distribution</td>
		<td align="left"><ul>
          <li>Create a setup.py</li>
          <li>Create a README.md that describes your repo, gives instructions on how to install it locally, and some code examples on how to use it</li>
          <li>Create a CHANGELOG.md</li>
          <li>Create a .gitignore</li>
          <li>Test your setup.py by building a source and wheel distribution locally. I.e. use python -m build, which should create a new dist/ folder containing the distribution files</li>
        </ul></td>
    </tr>
  </tbody>
</table>


* Note: You must also commit any additional files into your repository so we can test your code.
  * Points will be lost if you forget!
