[![Build Status](https://travis-ci.org/rob-earwaker/jschema.svg?branch=master)]
(https://travis-ci.org/rob-earwaker/jschema)
[![Coverage Status]
(https://coveralls.io/repos/github/rob-earwaker/jschema/badge.svg?branch=master)]
(https://coveralls.io/github/rob-earwaker/jschema?branch=master)

# jschema
Define classes that conform to a [JSON schema](http://json-schema.org/), with
built-in validation and schema generation.

## The JSchema Class
A `jschema.JSchema` object represents an validated JSON schema. Any recognised
JSON schema field can be passed as a keyword argument when initialising a
`jschema.JSchema` object:

```python
>>> import jschema
>>>
>>> jschema.JSchema()
<jschema.JSchema object at 0x...>
>>>
>>> jschema.JSchema(
...     title='First name',
...     type='string',
...     max_length=32
... )
<jschema.JSchema object at 0x...>
>>>
```

Keywords are provided in the underscored format rather than the camel case
format used by the JSON schema definition, i.e. `max_length` rather than
`maxLength`. This is done to conform to the [PEP8 Style Guide]
(https://www.python.org/dev/peps/pep-0008/).

The JSON schema can be accessed as either a `dict` or a JSON string:

```python
>>> import jschema
>>>
>>> schema = jschema.JSchema(
...     title='Age',
...     type='integer',
...     minimum=0
... )
>>>
>>> import pprint
>>> pprint.pprint(schema.asdict())
{'minimum': 0, 'title': 'Age', 'type': 'integer'}
>>>
>>> print(schema.asjson())
{"minimum":0,"title":"Age","type":"integer"}
>>>
>>> print(schema.asjson(pretty=True))
{
    "minimum": 0,
    "title": "Age",
    "type": "integer"
}
>>>
```

A `jschema.SchemaValidationError` will be raised on initialisation if any
[JSON schema validation]
(http://json-schema.org/latest/json-schema-validation.html) rules are breached:

```python
>>> import jschema
>>>
>>> jschema.JSchema(
...     title='Luggage',
...     type='array',
...     max_items=0.5
... )
Traceback (most recent call last):
  ...
jschema.SchemaValidationError: 'max_items' must be an int
>>>
>>> jschema.JSchema(
...     title='Height',
...     type='object',
...     required=[]
... )
Traceback (most recent call last):
  ...
jschema.SchemaValidationError: 'required' list must not be empty
>>>
```