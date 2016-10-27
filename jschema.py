import json
import uuid


ADDITIONAL_ITEMS_KEY = 'additional_items'
ADDITIONAL_PROPERTIES_KEY = 'additional_properties'
ALL_OF_KEY = 'all_of'
ANY_OF_KEY = 'any_of'
EXCLUSIVE_MAXIMUM_KEY = 'exclusive_maximum'
EXCLUSIVE_MINIMUM_KEY = 'exclusive_minimum'
ITEMS_KEY = 'items'
MAX_ITEMS_KEY = 'max_items'
MAX_LENGTH_KEY = 'max_length'
MAX_PROPERTIES_KEY = 'max_properties'
MAXIMUM_KEY = 'maximum'
MIN_ITEMS_KEY = 'min_items'
MIN_LENGTH_KEY = 'min_length'
MIN_PROPERTIES_KEY = 'min_properties'
MINIMUM_KEY = 'minimum'
MULTIPLE_OF_KEY = 'multiple_of'
PATTERN_KEY = 'pattern'
PATTERN_PROPERTIES_KEY = 'pattern_properties'
PROPERTIES_KEY = 'properties'
REQUIRED_KEY = 'required'
TYPE_KEY = 'type'
UNIQUE_ITEMS_KEY = 'unique_items'

PRIMITIVE_TYPES = [
    'array', 'boolean', 'integer', 'null', 'number', 'object', 'string'
]


class DefinitionError(Exception):
    pass


def validate_additional_items(additional_items):
    if additional_items is not None:
        if not isinstance(additional_items, (bool, JSchema)):
            raise DefinitionError(
                "'{0}' must be a bool or a schema".format(
                    ADDITIONAL_ITEMS_KEY
                )
            )


def validate_additional_properties(additional_properties):
    if additional_properties is not None:
        if not isinstance(additional_properties, (bool, JSchema)):
            raise DefinitionError(
                "'{0}' must be a bool or a schema".format(
                    ADDITIONAL_PROPERTIES_KEY
                )
            )


def validate_all_of(all_of):
    if all_of is not None:
        if not isinstance(all_of, list):
            raise DefinitionError("'{0}' must be a list".format(ALL_OF_KEY))
        if not len(all_of) >= 1:
            raise DefinitionError(
                "'{0}' list must contain at least one item".format(ALL_OF_KEY)
            )
        for item in all_of:
            if not isinstance(item, JSchema):
                raise DefinitionError(
                    "'{0}' list item must be a schema".format(ALL_OF_KEY)
                )


def validate_any_of(any_of):
    if any_of is not None:
        if not isinstance(any_of, list):
            raise DefinitionError("'{0}' must be a list".format(ANY_OF_KEY))
        if not len(any_of) >= 1:
            raise DefinitionError(
                "'{0}' list must contain at least one item".format(ANY_OF_KEY)
            )
        for item in any_of:
            if not isinstance(item, JSchema):
                raise DefinitionError(
                    "'{0}' list item must be a schema".format(ANY_OF_KEY)
                )


def validate_items(items):
    if items is not None:
        if not isinstance(items, (JSchema, list)):
            raise DefinitionError(
                "'{0}' must be a schema or a list".format(ITEMS_KEY)
            )
        if isinstance(items, list):
            for item in items:
                if not isinstance(item, JSchema):
                    raise DefinitionError(
                        "'{0}' list must contain only schemas".format(
                            ITEMS_KEY
                        )
                    )


def validate_max_items(max_items):
    if max_items is not None:
        if not isinstance(max_items, int):
            raise DefinitionError(
                "'{0}' must be an int".format(MAX_ITEMS_KEY)
            )
        if not max_items >= 0:
            raise DefinitionError(
                "'{0}' must be greater than or equal to zero".format(
                    MAX_ITEMS_KEY
                )
            )


def validate_max_length(max_length):
    if max_length is not None:
        if not isinstance(max_length, int):
            raise DefinitionError(
                "'{0}' must be an int".format(MAX_LENGTH_KEY)
            )
        if not max_length >= 0:
            raise DefinitionError(
                "'{0}' must be greater than or equal to zero".format(
                    MAX_LENGTH_KEY
                )
            )


def validate_max_properties(max_properties):
    if max_properties is not None:
        if not isinstance(max_properties, int):
            raise DefinitionError(
                "'{0}' must be an int".format(MAX_PROPERTIES_KEY)
            )
        if not max_properties >= 0:
            raise DefinitionError(
                "'{0}' must be greater than or equal to zero".format(
                    MAX_PROPERTIES_KEY
                )
            )


def validate_maximum(maximum, exclusive_maximum):
    if maximum is not None:
        if not isinstance(maximum, (int, float)):
            raise DefinitionError(
                "'{0}' must be an int or float".format(MAXIMUM_KEY)
            )
    if exclusive_maximum is not None:
        if not isinstance(exclusive_maximum, bool):
            raise DefinitionError(
                "'{0}' must be a bool".format(EXCLUSIVE_MAXIMUM_KEY)
            )
        if maximum is None:
            raise DefinitionError(
                "'{0}' must be present if '{1}' is defined".format(
                    MAXIMUM_KEY, EXCLUSIVE_MAXIMUM_KEY
                )
            )


def validate_min_items(min_items):
    if min_items is not None:
        if not isinstance(min_items, int):
            raise DefinitionError(
                "'{0}' must be an int".format(MIN_ITEMS_KEY)
            )
        if not min_items >= 0:
            raise DefinitionError(
                "'{0}' must be greater than or equal to zero".format(
                    MIN_ITEMS_KEY
                )
            )


def validate_min_length(min_length):
    if min_length is not None:
        if not isinstance(min_length, int):
            raise DefinitionError(
                "'{0}' must be an int".format(MIN_LENGTH_KEY)
            )
        if not min_length >= 0:
            raise DefinitionError(
                "'{0}' must be greater than or equal to zero".format(
                    MIN_LENGTH_KEY
                )
            )


def validate_min_properties(min_properties):
    if min_properties is not None:
        if not isinstance(min_properties, int):
            raise DefinitionError(
                "'{0}' must be an int".format(MIN_PROPERTIES_KEY)
            )
        if not min_properties >= 0:
            raise DefinitionError(
                "'{0}' must be greater than or equal to zero".format(
                    MIN_PROPERTIES_KEY
                )
            )


def validate_minimum(minimum, exclusive_minimum):
    if minimum is not None:
        if not isinstance(minimum, (int, float)):
            raise DefinitionError(
                "'{0}' must be an int or float".format(MINIMUM_KEY)
            )
    if exclusive_minimum is not None:
        if not isinstance(exclusive_minimum, bool):
            raise DefinitionError(
                "'{0}' must be a bool".format(EXCLUSIVE_MINIMUM_KEY)
            )
        if minimum is None:
            raise DefinitionError(
                "'{0}' must be present if '{1}' is defined".format(
                    MINIMUM_KEY, EXCLUSIVE_MINIMUM_KEY
                )
            )


def validate_multiple_of(multiple_of):
    if multiple_of is not None:
        if not isinstance(multiple_of, (int, float)):
            raise DefinitionError(
                "'{0}' must be an int or float".format(MULTIPLE_OF_KEY)
            )
        if not multiple_of > 0:
            raise DefinitionError(
                "'{0}' must be greater than zero".format(MULTIPLE_OF_KEY)
            )


def validate_pattern(pattern):
    if pattern is not None:
        if not isinstance(pattern, str):
            raise DefinitionError("'{0}' must be a str".format(PATTERN_KEY))


def validate_pattern_properties(pattern_properties):
    if pattern_properties is not None:
        if not isinstance(pattern_properties, dict):
            raise DefinitionError(
                "'{0}' must be a dict".format(PATTERN_PROPERTIES_KEY)
            )
        for key, value in pattern_properties.items():
            if not isinstance(key, str):
                raise DefinitionError(
                    "'{0}' dict key must be a str".format(
                        PATTERN_PROPERTIES_KEY
                    )
                )
            if not isinstance(value, JSchema):
                raise DefinitionError(
                    "'{0}' dict value must be a schema".format(
                        PATTERN_PROPERTIES_KEY
                    )
                )


def validate_properties(properties):
    if properties is not None:
        if not isinstance(properties, dict):
            raise DefinitionError(
                "'{0}' must be a dict".format(PROPERTIES_KEY)
            )
        for key, value in properties.items():
            if not isinstance(key, str):
                raise DefinitionError(
                    "'{0}' dict key must be a str".format(PROPERTIES_KEY)
                )
            if not isinstance(value, JSchema):
                raise DefinitionError(
                    "'{0}' dict value must be a schema".format(PROPERTIES_KEY)
                )


def validate_required(required):
    if required is not None:
        if not isinstance(required, list):
            raise DefinitionError(
                "'{0}' must be a list".format(REQUIRED_KEY)
            )
        if not len(required) >= 1:
            raise DefinitionError(
                "'{0}' list must have at least one item".format(
                    REQUIRED_KEY
                )
            )
        for item in required:
            if not isinstance(item, str):
                raise DefinitionError(
                    "'{0}' list item must be a str".format(REQUIRED_KEY)
                )
        if not len(set(required)) == len(required):
            raise DefinitionError(
                "'{0}' list items must be unique".format(REQUIRED_KEY)
            )


def validate_type(type):
    if type is not None:
        if not isinstance(type, (str, list)):
            raise DefinitionError(
                "'{0}' must be a str or a list".format(TYPE_KEY)
            )
        if isinstance(type, str):
            if type not in PRIMITIVE_TYPES:
                raise DefinitionError(
                    "'{0}' str must be a primitive type".format(TYPE_KEY)
                )
        if isinstance(type, list):
            for item in type:
                if not isinstance(item, str):
                    raise DefinitionError(
                        "'{0}' list item must be a str".format(TYPE_KEY)
                    )
                if item not in PRIMITIVE_TYPES:
                    raise DefinitionError(
                        "'{0}' list item str must be a primitive type".format(
                            TYPE_KEY
                        )
                    )
            if not len(set(type)) == len(type):
                raise DefinitionError(
                    "'{0}' list item str must be unique".format(TYPE_KEY)
                )


def validate_unique_items(unique_items):
    if unique_items is not None:
        if not isinstance(unique_items, bool):
            raise DefinitionError(
                "'{0}' must be a bool".format(UNIQUE_ITEMS_KEY)
            )


class JSchema(object):
    FIELD_NAMES = {
        # meta
        'schema': '$schema',
        'ref': '$ref',
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'default': 'default',
        # array
        ADDITIONAL_ITEMS_KEY: 'additionalItems',
        ITEMS_KEY: 'items',
        MAX_ITEMS_KEY: 'maxItems',
        MIN_ITEMS_KEY: 'minItems',
        UNIQUE_ITEMS_KEY: 'uniqueItems',
        # integer, number
        MULTIPLE_OF_KEY: 'multipleOf',
        MAXIMUM_KEY: 'maximum',
        EXCLUSIVE_MAXIMUM_KEY: 'exclusiveMaximum',
        MINIMUM_KEY: 'minimum',
        EXCLUSIVE_MINIMUM_KEY: 'exclusiveMinimum',
        # object
        MAX_PROPERTIES_KEY: 'maxProperties',
        MIN_PROPERTIES_KEY: 'minProperties',
        REQUIRED_KEY: 'required',
        ADDITIONAL_PROPERTIES_KEY: 'additionalProperties',
        PROPERTIES_KEY: 'properties',
        PATTERN_PROPERTIES_KEY: 'patternProperties',
        'dependencies': 'dependencies',
        # string
        MAX_LENGTH_KEY: 'maxLength',
        MIN_LENGTH_KEY: 'minLength',
        PATTERN_KEY: 'pattern',
        # all
        'enum': 'enum',
        TYPE_KEY: 'type',
        ALL_OF_KEY: 'allOf',
        ANY_OF_KEY: 'anyOf',
        'one_of': 'oneOf',
        'not_': 'not',
        'definitions': 'definitions'
    }

    def __init__(self, **kwargs):
        additional_items = kwargs.get(ADDITIONAL_ITEMS_KEY, None)
        validate_additional_items(additional_items)

        additional_properties = kwargs.get(ADDITIONAL_PROPERTIES_KEY, None)
        validate_additional_properties(additional_properties)

        all_of = kwargs.get(ALL_OF_KEY, None)
        validate_all_of(all_of)

        any_of = kwargs.get(ANY_OF_KEY, None)
        validate_any_of(any_of)

        items = kwargs.get(ITEMS_KEY, None)
        validate_items(items)

        max_items = kwargs.get(MAX_ITEMS_KEY, None)
        validate_max_items(max_items)

        max_length = kwargs.get(MAX_LENGTH_KEY, None)
        validate_max_length(max_length)

        max_properties = kwargs.get(MAX_PROPERTIES_KEY, None)
        validate_max_properties(max_properties)

        maximum = kwargs.get(MAXIMUM_KEY, None)
        exclusive_maximum = kwargs.get(EXCLUSIVE_MAXIMUM_KEY, None)
        validate_maximum(maximum, exclusive_maximum)

        min_items = kwargs.get(MIN_ITEMS_KEY, None)
        validate_min_items(min_items)

        min_length = kwargs.get(MIN_LENGTH_KEY, None)
        validate_min_length(min_length)

        min_properties = kwargs.get(MIN_PROPERTIES_KEY, None)
        validate_min_properties(min_properties)

        minimum = kwargs.get(MINIMUM_KEY, None)
        exclusive_minimum = kwargs.get(EXCLUSIVE_MINIMUM_KEY, None)
        validate_minimum(minimum, exclusive_minimum)

        multiple_of = kwargs.get(MULTIPLE_OF_KEY, None)
        validate_multiple_of(multiple_of)

        pattern = kwargs.get(PATTERN_KEY, None)
        validate_pattern(pattern)

        pattern_properties = kwargs.get(PATTERN_PROPERTIES_KEY, None)
        validate_pattern_properties(pattern_properties)

        properties = kwargs.get(PROPERTIES_KEY, None)
        validate_properties(properties)

        required = kwargs.get(REQUIRED_KEY, None)
        validate_required(required)

        type = kwargs.get(TYPE_KEY, None)
        validate_type(type)

        unique_items = kwargs.get(UNIQUE_ITEMS_KEY, None)
        validate_unique_items(unique_items)

        self._optional = kwargs.pop('optional', False)
        schema = {}
        for field, field_name in self.FIELD_NAMES.items():
            if field in kwargs:
                schema[field_name] = kwargs[field]
        if 'ref' in kwargs:
            self._dict = {
                'definitions': schema.pop('definitions', {}),
                '$ref': '#/definitions/{0}'.format(kwargs['ref'])
            }
            self._dict['definitions'][kwargs['ref']] = schema
        else:
            self._dict = schema

    @property
    def optional(self):
        return self._optional

    @property
    def definitions(self):
        return self._dict.get('definitions', {})

    def asdict(self, root=True, id=None):
        dict = self._dict.copy()
        if not root:
            dict.pop('definitions', None)
        if id:
            dict['id'] = id
        return dict

    def asjson(self, pretty=False):
        indent = 4 if pretty else None
        separators = (',', ': ') if pretty else (',', ':')
        return json.dumps(
            self.asdict(), sort_keys=True, indent=indent, separators=separators
        )


def uname():
    return uuid.uuid4().hex


def Properties(**kwargs):
    return kwargs


def Dependencies(**kwargs):
    return kwargs


class JSchemaMeta(type):
    def __call__(cls, *args, **kwargs):
        jschema = super(JSchemaMeta, cls).__call__(*args, **kwargs)
        return type(uname(), (object,), {'jschema': jschema})


class Array(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        definitions = {}
        additional_items = kwargs.get('additional_items', None)
        if hasattr(additional_items, 'jschema'):
            schema = additional_items.jschema
            kwargs['additional_items'] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        items = kwargs.get('items', None)
        if isinstance(items, list):
            kwargs['items'] = []
            for item in items:
                schema = item.jschema
                kwargs['items'].append(schema.asdict(root=False))
                for name in schema.definitions:
                    definitions[name] = schema.definitions[name]
        elif hasattr(items, 'jschema'):
            schema = items.jschema
            kwargs['items'] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        kwargs['type'] = 'array'
        super(Array, self).__init__(**kwargs)


class Boolean(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'boolean'
        super(Boolean, self).__init__(**kwargs)


class Integer(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'integer'
        super(Integer, self).__init__(**kwargs)


class Null(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'null'
        super(Null, self).__init__(**kwargs)


class Number(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'number'
        super(Number, self).__init__(**kwargs)


class Object(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        definitions = {}
        additional_properties = kwargs.get('additional_properties', None)
        if hasattr(additional_properties, 'jschema'):
            schema = additional_properties.jschema
            kwargs['additional_properties'] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        properties = kwargs.get('properties', {})
        for name in sorted(properties):
            schema = properties[name].jschema
            kwargs['properties'][name] = schema.asdict(root=False)
            if not schema.optional:
                if 'required' not in kwargs:
                    kwargs['required'] = []
                kwargs['required'].append(name)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        pattern_properties = kwargs.get('pattern_properties', {})
        for name in pattern_properties:
            schema = pattern_properties[name].jschema
            kwargs['pattern_properties'][name] = schema.asdict(root=False)
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        dependencies = kwargs.get('dependencies', {})
        for name, dependency in dependencies.items():
            if hasattr(dependency, 'jschema'):
                schema = dependency.jschema
                kwargs['dependencies'][name] = schema.asdict(root=False)
                for name in schema.definitions:
                    definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        kwargs['type'] = 'object'
        super(Object, self).__init__(**kwargs)


class String(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        kwargs['type'] = 'string'
        super(String, self).__init__(**kwargs)


class Empty(JSchema, metaclass=JSchemaMeta):
    def __init__(self, **kwargs):
        definitions = {}
        all_of = kwargs.pop('all_of', [])
        for type in all_of:
            schema = type.jschema
            if 'all_of' not in kwargs:
                kwargs['all_of'] = []
            kwargs['all_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        any_of = kwargs.pop('any_of', [])
        for type in any_of:
            schema = type.jschema
            if 'any_of' not in kwargs:
                kwargs['any_of'] = []
            kwargs['any_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        one_of = kwargs.pop('one_of', [])
        for type in one_of:
            schema = type.jschema
            if 'one_of' not in kwargs:
                kwargs['one_of'] = []
            kwargs['one_of'].append(schema.asdict(root=False))
            for name in schema.definitions:
                definitions[name] = schema.definitions[name]
        if definitions:
            kwargs['definitions'] = definitions
        super(Empty, self).__init__(**kwargs)
