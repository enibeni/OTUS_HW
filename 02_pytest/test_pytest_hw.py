import string


class TestClass:

    def test_sum_of_two_numbers(self):
        """ sum of two numbers returns right result
        """
        assert 2 + 3 == 5

    def test_float_is_type_of_division_result(self):
        """ division gives float type as a result
        """
        assert isinstance(2/3, float)

    def test_string_capitalization(self, name_in_lowercase):
        """ str.capitalize() works properly
        """
        name = name_in_lowercase
        capitalized_name = name.capitalize()
        assert capitalized_name == "Batman"

    def test_string_contains_all_chars_from_alphabet(self):
        """ string with all chars from alphabet
        """
        sentence = "The quick brown fox jumps over the lazy dog"
        eng_alphabet = string.ascii_lowercase
        for letter in eng_alphabet:
            assert letter in sentence

    def test_list_of_even_numbers_not_in_odds(self, even_and_odds):
        """ list of odds doesn't contain any even numbers
        """
        even, odds = even_and_odds
        for number in even:
            assert number not in odds

    def test_list_copy_by_reference(self, numbers):
        """ copied by reference lists hold one space in memory
        """
        numbers = numbers
        copied_by_reference_numbers = numbers
        assert id(numbers) == id(copied_by_reference_numbers)

    def test_list_copy_by_value(self, numbers):
        """ copied by value lists hold different spaces in memory
        """
        numbers = numbers
        copied_by_value_numbers = numbers.copy()
        assert not id(numbers) == id(copied_by_value_numbers)

    def test_tuple_creation(self):
        """ different means of tuple creation give the same object type
        """
        tuple_one = (1, 2, 3)
        tuple_two = tuple((1, 2, 3))
        assert type(tuple_one) == type(tuple_two)

    def test_set_removes_duplicates(self, numbers_with_duplicates):
        """ set contains only unique values
        """
        numbers_with_duplicates = numbers_with_duplicates
        numbers_without_duplicates = list(set(numbers_with_duplicates))
        assert not any(numbers_without_duplicates.count(x) > 1 for x in numbers_without_duplicates)

    def test_dict_is_insertion_ordered(self, dict_with_keys_inserted_one_by_one):
        """ dict keys are ordered by insertion
        """
        dict_with_keys_inserted_one_by_one = dict_with_keys_inserted_one_by_one
        keys = list(dict_with_keys_inserted_one_by_one.keys())
        assert keys == ["first", "second", "third", "fourth", "fifth", "last"]
