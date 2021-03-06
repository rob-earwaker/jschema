import unittest

import jsch


class SchemaValidationTestCase(unittest.TestCase):
    def assertRaisesSchemaValidationError(self, message):
        regex = '^{0}$'.format(message)
        return self.assertRaisesRegex(jsch.SchemaValidationError, regex)


class TestAdditionalItemsValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jsch.Schema(additional_items=True)

    def test_passes_when_schema(self):
        jsch.Schema(additional_items=jsch.Schema())

    def test_fails_when_not_bool_or_schema(self):
        message = "'additional_items' must be a bool or a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(additional_items='False')


class TestAdditionalPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jsch.Schema(additional_properties=True)

    def test_passes_when_schema(self):
        jsch.Schema(additional_properties=jsch.Schema())

    def test_fails_when_not_bool_or_schema(self):
        message = "'additional_properties' must be a bool or a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(additional_properties='False')


class TestAllOfValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jsch.Schema(all_of=[jsch.Schema(), jsch.Schema()])

    def test_fails_when_not_list(self):
        message = "'all_of' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(all_of='[]')

    def test_fails_when_list_empty(self):
        message = "'all_of' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(all_of=[])

    def test_fails_when_list_item_not_schema(self):
        message = "'all_of' list item must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(all_of=[jsch.Schema(), '{}'])


class TestAnyOfValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jsch.Schema(any_of=[jsch.Schema(), jsch.Schema()])

    def test_fails_when_not_list(self):
        message = "'any_of' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(any_of='[]')

    def test_fails_when_list_empty(self):
        message = "'any_of' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(any_of=[])

    def test_fails_when_list_item_not_schema(self):
        message = "'any_of' list item must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(any_of=[jsch.Schema(), '{}'])


class TestDefaultValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jsch.Schema(default=['a', {}, 8])

    def test_passes_when_bool(self):
        jsch.Schema(default=True)

    def test_passes_when_int(self):
        jsch.Schema(default=6)

    def test_passes_when_float(self):
        jsch.Schema(default=5.9)

    def test_passes_when_dict(self):
        jsch.Schema(default={'h': [7], 9: {'g': []}})

    def test_passes_when_str(self):
        jsch.Schema(default='name')

    def test_fails_when_not_primitive_type(self):
        message = "'default' must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(default=('a', 'b'))

    def test_fails_when_list_item_not_primitive_type(self):
        message = "'default' must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(default=[{'a', 'b'}])

    def test_fails_when_dict_key_not_primitive_type(self):
        message = "'default' must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(default={8j: 'value'})

    def test_fails_when_dict_value_not_primitive_type(self):
        message = "'default' must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(default={'name': b'\xff\xde'})


class TestDefinitionsValidation(SchemaValidationTestCase):
    def test_passes_when_dict(self):
        jsch.Schema(definitions={'name': jsch.Schema()})

    def test_fails_when_not_dict(self):
        message = "'definitions' must be a dict"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(definitions=True)

    def test_fails_when_dict_key_not_str(self):
        message = "'definitions' dict key must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(definitions={7: jsch.Schema()})

    def test_fails_when_dict_value_not_schema(self):
        message = "'definitions' dict value must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(definitions={'name': '{}'})


class TestDependenciesValidation(SchemaValidationTestCase):
    def test_passes_when_dict_with_schema_values(self):
        jsch.Schema(dependencies={'name': jsch.Schema()})

    def test_passes_when_dict_with_list_values(self):
        jsch.Schema(dependencies={'name': ['age', 'height']})

    def test_fails_when_not_dict(self):
        message = "'dependencies' must be a dict"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(dependencies=['name'])

    def test_fails_when_dict_key_not_str(self):
        message = "'dependencies' dict key must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(dependencies={7: jsch.Schema()})

    def test_fails_when_dict_value_not_schema_or_list(self):
        message = "'dependencies' dict value must be a schema or a list"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(dependencies={'name': False})

    def test_fails_when_dict_list_value_empty(self):
        message = "'dependencies' dict value list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(dependencies={'name': []})

    def test_fails_when_dict_list_value_item_not_str(self):
        message = "'dependencies' dict value list item must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(dependencies={'name': [7]})

    def test_fails_when_dict_list_value_item_str_not_unique(self):
        message = "'dependencies' dict value list item str must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(dependencies={'name': ['a', 'b', 'a']})


class TestDescriptionValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jsch.Schema(description='Height in cm')

    def test_fails_when_not_str(self):
        message = "'description' must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(description=90)


class TestEnumValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jsch.Schema(enum=['name', True, None, 8, {}, ['a']])

    def test_fails_when_not_list(self):
        message = "'enum' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum='[]')

    def test_fails_when_list_empty(self):
        message = "'enum' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[])

    def test_fails_when_list_item_not_primitive_type(self):
        message = "'enum' list item must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[('a', 'b')])

    def test_fails_when_list_item_list_item_not_primitive_type(self):
        message = "'enum' list item must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[[{'a', 'b'}]])

    def test_fails_when_list_item_dict_key_not_primitive_type(self):
        message = "'enum' list item must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[{8j: 'value'}])

    def test_fails_when_list_item_dict_value_not_primitive_type(self):
        message = "'enum' list item must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[{'name': b'\xff\xde'}])

    def test_fails_when_list_item_list_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[['a', 'b'], ['a', 'b'], ['b', 'c']])

    def test_fails_when_list_item_bool_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[True, True, False])

    def test_fails_when_list_item_int_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[5, 5, 67])

    def test_fails_when_list_item_null_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[None, None])

    def test_fails_when_list_item_float_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[4.8, 4.8, 1.9])

    def test_fails_when_list_item_dict_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=[{'a': 'b'}, {'a': 'b'}, {'b': 'c'}])

    def test_fails_when_list_item_str_not_unique(self):
        message = "'enum' list item must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(enum=['name', 'name', 'age'])


class TestExclusiveMaximumValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jsch.Schema(maximum=1, exclusive_maximum=True)

    def test_fails_when_not_bool(self):
        message = "'exclusive_maximum' must be a bool"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(maximum=1, exclusive_maximum='True')


class TestExclusiveMinimumValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jsch.Schema(minimum=1, exclusive_minimum=True)

    def test_fails_when_not_bool(self):
        message = "'exclusive_minimum' must be a bool"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(minimum=1, exclusive_minimum='True')


class TestIdValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jsch.Schema(id='#def')

    def test_fails_when_not_str(self):
        message = "'id' must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(id=90)


class TestItemsValidation(SchemaValidationTestCase):
    def test_passes_when_schema(self):
        jsch.Schema(items=jsch.Schema())

    def test_passes_when_list(self):
        jsch.Schema(items=[jsch.Schema(), jsch.Schema()])

    def test_fails_when_not_schema_or_list(self):
        message = "'items' must be a schema or a list"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(items=9.6)

    def test_fails_when_list_item_not_schema(self):
        message = "'items' list must contain only schemas"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(items=[jsch.Schema(), '{}'])


class TestMaximumValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(maximum=5)

    def test_passes_when_float(self):
        jsch.Schema(maximum=7.6)

    def test_fails_when_not_int_or_float(self):
        message = "'maximum' must be an int or float"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(maximum='5')

    def test_fails_when_not_present_with_exclusive_maximum_defined(self):
        message = "'maximum' must be present if 'exclusive_maximum' is defined"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(exclusive_maximum=True)


class TestMaxItemsValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(max_items=5)

    def test_fails_when_not_int(self):
        message = "'max_items' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(max_items=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'max_items' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(max_items=-1)


class TestMaxLengthValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(max_length=5)

    def test_fails_when_not_int(self):
        message = "'max_length' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(max_length=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'max_length' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(max_length=-1)


class TestMaxPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(max_properties=5)

    def test_fails_when_not_int(self):
        message = "'max_properties' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(max_properties=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'max_properties' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(max_properties=-1)


class TestMinimumValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(minimum=5)

    def test_passes_when_float(self):
        jsch.Schema(minimum=7.6)

    def test_fails_when_not_int_or_float(self):
        message = "'minimum' must be an int or float"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(minimum='5')

    def test_fails_when_not_present_with_exclusive_minimum_defined(self):
        message = "'minimum' must be present if 'exclusive_minimum' is defined"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(exclusive_minimum=True)


class TestMinItemsValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(min_items=5)

    def test_fails_when_not_int(self):
        message = "'min_items' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(min_items=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'min_items' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(min_items=-1)


class TestMinLengthValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(min_length=5)

    def test_fails_when_not_int(self):
        message = "'min_length' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(min_length=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'min_length' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(min_length=-1)


class TestMinPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(min_properties=5)

    def test_fails_when_not_int(self):
        message = "'min_properties' must be an int"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(min_properties=0.5)

    def test_fails_when_less_than_zero(self):
        message = "'min_properties' must be greater than or equal to zero"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(min_properties=-1)


class TestMultipleOfValidation(SchemaValidationTestCase):
    def test_passes_when_int(self):
        jsch.Schema(multiple_of=5)

    def test_passes_when_float(self):
        jsch.Schema(multiple_of=7.6)

    def test_fails_when_not_int_or_float(self):
        message = "'multiple_of' must be an int or float"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(multiple_of='2.3')

    def test_fails_when_not_greater_then_zero(self):
        message = "'multiple_of' must be greater than zero"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(multiple_of=0)


class TestNotValidation(SchemaValidationTestCase):
    def test_passes_when_schema(self):
        jsch.Schema(not_=jsch.Schema())

    def test_fails_when_not_schema(self):
        message = "'not_' must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(not_='{}')


class TestOneOfValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jsch.Schema(one_of=[jsch.Schema(), jsch.Schema()])

    def test_fails_when_not_list(self):
        message = "'one_of' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(one_of='[]')

    def test_fails_when_list_empty(self):
        message = "'one_of' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(one_of=[])

    def test_fails_when_list_item_not_schema(self):
        message = "'one_of' list item must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(one_of=[jsch.Schema(), '{}'])


class TestPatternValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jsch.Schema(pattern='^name$')

    def test_fails_when_not_str(self):
        message = "'pattern' must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(pattern=8)


class TestPatternPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_dict(self):
        jsch.Schema(pattern_properties={'^name$': jsch.Schema()})

    def test_fails_when_not_dict(self):
        message = "'pattern_properties' must be a dict"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(pattern_properties=[9])

    def test_fails_when_dict_key_not_str(self):
        message = "'pattern_properties' dict key must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(pattern_properties={8: jsch.Schema()})

    def test_fails_when_dict_value_not_schema(self):
        message = "'pattern_properties' dict value must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(pattern_properties={'name': '{}'})


class TestPropertiesValidation(SchemaValidationTestCase):
    def test_passes_when_dict(self):
        jsch.Schema(properties={'name': jsch.Schema()})

    def test_fails_when_not_dict(self):
        message = "'properties' must be a dict"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(properties=[9])

    def test_fails_when_dict_key_not_str(self):
        message = "'properties' dict key must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(properties={8: jsch.Schema()})

    def test_fails_when_dict_value_not_schema(self):
        message = "'properties' dict value must be a schema"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(properties={'name': '{}'})


class TestRefValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jsch.Schema(ref='#/definitions/name')

    def test_fails_when_not_str(self):
        message = "'ref' must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(ref=90)


class TestRequiredValidation(SchemaValidationTestCase):
    def test_passes_when_list(self):
        jsch.Schema(required=['name', 'age'])

    def test_fails_when_not_list(self):
        message = "'required' must be a list"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(required='[]')

    def test_fails_when_list_empty(self):
        message = "'required' list must not be empty"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(required=[])

    def test_fails_when_list_item_not_str(self):
        message = "'required' list item must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(required=[8])

    def test_fails_when_list_str_item_not_unique(self):
        message = "'required' list item str must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(required=['a', 'b', 'c', 'a'])


class TestSchemaValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jsch.Schema().asdict(root=True, schema='http://org/sch#')

    def test_fails_when_not_str(self):
        message = "'schema' must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema().asdict(root=True, schema=76)


class TestTitleValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jsch.Schema(title='Height')

    def test_fails_when_not_str(self):
        message = "'title' must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(title=90)


class TestTypeValidation(SchemaValidationTestCase):
    def test_passes_when_str(self):
        jsch.Schema(type='number')

    def test_passes_when_list(self):
        jsch.Schema(type=['array', 'object', 'integer', 'null', 'string'])

    def test_fails_when_not_str_or_list(self):
        message = "'type' must be a str or a list"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(type=45)

    def test_fails_when_str_not_primitive_type(self):
        message = "'type' str must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(type='float')

    def test_fails_when_list_item_not_str(self):
        message = "'type' list item must be a str"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(type=['string', 7])

    def test_fails_when_list_item_str_not_primitive_type(self):
        message = "'type' list item str must be a primitive type"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(type=['string', 'float'])

    def test_fails_when_list_item_str_not_unique(self):
        message = "'type' list item str must be unique"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(type=['string', 'null', 'null'])


class TestUniqueItemsValidation(SchemaValidationTestCase):
    def test_passes_when_bool(self):
        jsch.Schema(unique_items=False)

    def test_fails_when_not_bool(self):
        message = "'unique_items' must be a bool"
        with self.assertRaisesSchemaValidationError(message):
            jsch.Schema(unique_items='True')


if __name__ == '__main__':
    unittest.main()
