import uuid


class Reference(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def asdict(self):
        return {'$ref': '#/definitions/{0}'.format(self.name)}


class JSchema(object):
    FIELD_NAMES = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'schema': '$schema',
        'default': 'default',
        'additional_items': 'additionalItems',
        'items': 'items',
        'max_items': 'maxItems',
        'min_items': 'minItems',
        'unique_items': 'uniqueItems',
        'multiple_of': 'multipleOf',
        'maximum': 'maximum',
        'exclusive_maximum': 'exclusiveMaximum',
        'minimum': 'minimum',
        'exclusive_minimum': 'exclusiveMinimum',
        'max_properties': 'maxProperties',
        'min_properties': 'minProperties',
        'required': 'required',
        'additional_properties': 'additionalProperties',
        'properties': 'properties',
        'pattern_properties': 'patternProperties',
        'dependencies': 'dependencies',
        'max_length': 'maxLength',
        'min_length': 'minLength',
        'pattern': 'pattern',
        'definitions': 'definitions'
    }

    def __init__(self, type, **kwargs):
        self._ref = Reference(kwargs['ref']) if 'ref' in kwargs else None
        self._dict = {'type': type}
        for field in self.FIELD_NAMES:
            if field in kwargs:
                self._dict[self.FIELD_NAMES[field]] = kwargs[field]
        if 'additionalItems' in self._dict:
            additional_items = self._dict['additionalItems']
            if hasattr(additional_items, 'jschema'):
                schema = additional_items.jschema
                if schema.ref is not None:
                    self._dict['additionalItems'] = schema.ref.asdict()
                    self.add_definition(schema.ref.name, schema.asdict())
                else:
                    self._dict['additionalItems'] = schema.asdict()
        if 'items' in self._dict:
            items = self._dict['items']
            if isinstance(items, list):
                self._dict['items'] = []
                for item in items:
                    schema = item.jschema
                    if schema.ref is not None:
                        self._dict['items'].append(schema.ref.asdict())
                        self.add_definition(schema.ref.name, schema.asdict())
                    else:
                        self._dict['items'].append(schema.asdict())
            if hasattr(items, 'jschema'):
                schema = items.jschema
                if schema.ref is not None:
                    self._dict['items'] = schema.ref.asdict()
                    self.add_definition(schema.ref.name, schema.asdict())
                else:
                    self._dict['items'] = schema.asdict()
        if 'additionalProperties' in self._dict:
            properties = self._dict['additionalProperties']
            if hasattr(properties, 'jschema'):
                schema = properties.jschema
                if schema.ref is not None:
                    self._dict['additionalProperties'] = schema.ref.asdict()
                    self.add_definition(schema.ref.name, schema.asdict())
                else:
                    self._dict['additionalProperties'] = schema.asdict()
        if 'properties' in self._dict:
            properties = self._dict['properties']
            for name in properties:
                schema = properties[name].jschema
                if schema.asdict().pop('required', False):
                    if 'required' not in self._dict:
                        self._dict['required'] = []
                    self._dict['required'].append(name)
                if schema.ref is not None:
                    self._dict['properties'][name] = schema.ref.asdict()
                    self.add_definition(schema.ref.name, schema.asdict())
                else:
                    self._dict['properties'][name] = schema.asdict()
        if 'patternProperties' in self._dict:
            properties = self._dict['patternProperties']
            for name in properties:
                schema = properties[name].jschema
                if schema.ref is not None:
                    self._dict['patternProperties'][name] = schema.ref.asdict()
                    self.add_definition(schema.ref.name, schema.asdict())
                else:
                    self._dict['patternProperties'][name] = schema.asdict()
        if 'dependencies' in self._dict:
            for name in self._dict['dependencies']:
                dependency = self._dict['dependencies'][name]
                if hasattr(dependency, 'jschema'):
                    schema = dependency.jschema
                    if schema.ref is not None:
                        self._dict['dependencies'][name] = schema.ref.asdict()
                        self.add_definition(schema.ref.name, schema.asdict())
                    else:
                        self._dict['dependencies'][name] = schema.asdict()

    def add_definition(self, name, schema):
        if self.definitions is None:
            self._dict['definitions'] = {}
        self._dict['definitions'][name] = schema

    @property
    def ref(self):
        return self._ref

    @property
    def definitions(self):
        return self._dict.get('definitions', None)

    @classmethod
    def array(cls, **kwargs):
        return cls('array', **kwargs)

    @classmethod
    def boolean(cls, **kwargs):
        return cls('boolean', **kwargs)

    @classmethod
    def integer(cls, **kwargs):
        return cls('integer', **kwargs)

    @classmethod
    def null(cls, **kwargs):
        return cls('null', **kwargs)

    @classmethod
    def number(cls, **kwargs):
        return cls('number', **kwargs)

    @classmethod
    def object(cls, **kwargs):
        return cls('object', **kwargs)

    @classmethod
    def string(cls, **kwargs):
        return cls('string', **kwargs)

    def asdict(self):
        return self._dict


def uname():
    return uuid.uuid4().get_hex()


def Properties(**kwargs):
    return kwargs


def Dependencies(**kwargs):
    return kwargs


class JSchemaMeta(type):
    def __call__(cls, *args, **kwargs):
        jschema = super(JSchemaMeta, cls).__call__(*args, **kwargs)
        return type(uname(), (object,), {'jschema': jschema})


class Array(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Array, self).__init__('array', **kwargs)


class Boolean(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Boolean, self).__init__('boolean', **kwargs)


class Integer(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Integer, self).__init__('integer', **kwargs)


class Null(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Null, self).__init__('null', **kwargs)


class Number(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Number, self).__init__('number', **kwargs)


class Object(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(Object, self).__init__('object', **kwargs)


class String(JSchema):
    __metaclass__ = JSchemaMeta

    def __init__(self, **kwargs):
        super(String, self).__init__('string', **kwargs)
