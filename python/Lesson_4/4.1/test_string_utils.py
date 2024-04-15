import pytest
from string_utils import StringUtils

atringutals = StringUtils()

# Тесты по преобразованию первой буквы строки в заглавную (Позитивные)
@pytest.mark.parametrize('string, result', [('text', 'Text'), 
                                            ('two words', 'Two words'),
                                            ('Go', 'Go'),
                                            ('123', '123'),
                                            ('04 апреля 2023', '04 апреля 2023') 
                                            ])
def test_capitalize_positive(string, result):
    stringutals = StringUtils()
    res = stringutals.capitilize(string)
    assert res == result

# Тесты по преобразованию первой буквы строки в заглавную (Негативные)
@pytest.mark.parametrize('string, result', [ 
                                            ('', ''),
                                            (' ', ' '),
                                pytest.param('test', None, marks=pytest.mark.xfail(reason='Ответом не может быть None')),
                                pytest.param(123, TypeError, marks=pytest.mark.xfail(reason='Значение не является строкой')),
                                            (None, AttributeError)])
def test_capitalize_negative(string, result):
    stringutals = StringUtils()
    if string is None:
        pytest.xfail("Capitalize возвращает ошибку для ввода None")
    res = stringutals.capitilize(string)
    assert res == result

# Тесты для удаления пробелов вначале строки (Позитивные)
@pytest.mark.parametrize('string, result', [(' Text', 'Text'), 
                                            ('  two spaces', 'two spaces'), 
                                            ('123', '123'), 
                                            ('04 апреля 2023', '04 апреля 2023')])
def test_trim_positive(string, result):
    stringutals = StringUtils()   
    res = stringutals.trim(string)
    assert res == result

# Тесты для удаления пробелов вначале строки (Негативные)
@pytest.mark.parametrize('string, result', [('', ''),
                                            (' ', ''),
                                pytest.param('test', None, marks=pytest.mark.xfail(reason="result is None")),
                                pytest.param(123, AttributeError, marks=pytest.mark.xfail(reason='Строка не может быть числом')),
                                pytest.param([1, 2, 3], AttributeError, marks=pytest.mark.xfail(reason='Строка не может быть списком')),
                                            (None, AttributeError)])
def test_trim_negative(string, result):
    stringutals = StringUtils()
    if string is None:
        pytest.xfail("trim возвращает ошибку для ввода None")
    elif string is int:
        pytest.xfail('Строка не может быть числом')    
    res = stringutals.trim(string)
    assert res == result

# Обработка текста с разделителем и возвращение списка строк (Позитивные)
@pytest.mark.parametrize('string, delimiter, result', 
                        [('text, and, next-text', ',', ['text', ' and', ' next-text']),
                        ('a,b,c,d', ',', ['a', 'b', 'c', 'd']),
                        ('1:2:3', ':', ['1', '2', '3']),
                        ('text with space', ' ',['text', 'with', 'space'])])
def test_to_list_positive(string, delimiter, result):
    stringutals = StringUtils()    
    res = stringutals.to_list(string, delimiter)
    assert res == result
    
# Обработка текста с разделителем и возвращение списка строк (Негативыне)
@pytest.mark.parametrize('string, delimiter, result', 
                        [(' ', '', []),
                        (' ', ',', []),
                        (None, ',', AssertionError),
                        ('another text', None, 'another text')])
def test_to_list_negative(string, delimiter, result):
    stringutals = StringUtils()
    if string is None:
        pytest.xfail("to_list возвращает ошибку для ввода None") 
    elif delimiter is None:
         pytest.xfail("to_list возвращает ошибку для ввода None")
    res = stringutals.to_list(string, delimiter)
    assert res == result   


# Возвращение `True`, если строка содержит искомый символ и `False` - если нет (Позитивные)
@pytest.mark.parametrize('string, symbol, result', 
                        [('special * symbol', '*', True),
                        ('text and, next-text', ' and', True),
                        ('abcd', 'g', False),
                        ('04 апреля 2023', '04', True)])
def test_contains_positive(string, symbol, result):
    stringutals = StringUtils()
    res = stringutals.contains(string, symbol)
    assert res == result

# Возвращение `True`, если строка содержит искомый символ и `False` - если нет (Негативыне)
@pytest.mark.parametrize('string, symbol, result', 
                        [('', '', True),
                        (' ', '', True),
                        ('with None', None, TypeError),
                        (None, None, AttributeError)])
def test_contains_negative(string, symbol, result):
    stringutals = StringUtils()
    if string is None:
        pytest.xfail("Contains возвращает ошибку для ввода None в строку")
    elif symbol is None:
        pytest.xfail("Contains возвращает ошибку для ввода None в символ")
    else:
        res = stringutals.contains(string, symbol)
        assert res == result


# Удаление подстрок из строки (Позитивный)
@pytest.mark.parametrize('string, symbol, result', 
                        [('text and, next-text', ' and', 'text, next-text'),
                        ('text with spaces', ' ', 'textwithspaces'),
                        ('04 апреля 2023', '04', ' апреля 2023'),
                        ("SkyPro", "", "SkyPro"),
                        ("SkyPro", "x", "SkyPro")])
def test_delete_symbol_positive(string, symbol, result):
    stringutals = StringUtils()
    res = stringutals.delete_symbol(string, symbol)
    assert res == result

# Удаление подстрок из строки (Негативный). 
@pytest.mark.parametrize('string, symbol, result', [
                        (None, "k", AttributeError),
                        ("SkyPro", None, TypeError),
                        ("", "k", ""),
                        ('', '', ''),
                        (' ', ' ', ''),
                        (123, "k", AttributeError),
                        ("SkyPro", 123, TypeError)])
def test_delete_symbol_negative(string, symbol, result):
    stringutals = StringUtils()
    # Далее я добавил исключения ошибок Типа и Атрибута. 
    # Т.к. их появление является корректным результатом.
    if result == TypeError:
        with pytest.raises(TypeError):
            stringutals.delete_symbol(string, symbol)
    elif result == AttributeError:
        with pytest.raises(AttributeError):
            stringutals.delete_symbol(string, symbol)
    else:
        res = stringutals.delete_symbol(string, symbol)
        assert res == result

# Второй вариант негативных проверок с маркеровкой при параметризации
# На мой взгляд этот тест будет более корректно отображать суть проверок
@pytest.mark.parametrize('string, symbol, result', [
                        ("SkyPro", "k", "SyPro"),
                        ("SkyPro", "Pro", "Sky"),
            pytest.param(None, "k", AttributeError, marks=pytest.mark.xfail(reason="string is None")),
            pytest.param("SkyPro", None, TypeError, marks=pytest.mark.xfail(reason="symbol is None")),
            pytest.param(123, "k", TypeError, marks=pytest.mark.xfail(reason="string is not a string")),
            pytest.param("SkyPro", 123, TypeError, marks=pytest.mark.xfail(reason="symbol is not a string"))
                        ])
def test_delete_symbol_negative_v2(string, symbol, result):
    stringutals = StringUtils()
    res = stringutals.delete_symbol(string, symbol)
    assert res == result


# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет (Позитивные)
@pytest.mark.parametrize('string, symbol, result', [
                        ('Text', 'T', True),
                        ('Text', 't', False),
                        ('123', '12', True),
                        (' with space', ' ', True)
                        ])
def test_starts_with_positive(string, symbol, result):
    stringutals = StringUtils()
    res = stringutals.starts_with(string, symbol)
    assert res == result

# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет (Негативные)
@pytest.mark.parametrize('string, symbol, result', [
                        ('', '', True),
                        (' ', ' ', True),
            pytest.param("SkyPro", None, "SkyPro", marks=pytest.mark.xfail(reason="symbol is None")),
            pytest.param(None, None, True, marks=pytest.mark.xfail(reason="string and symbol is None")),
            pytest.param(None, "k", False, marks=pytest.mark.xfail(reason="string is None")),
            pytest.param(123, "k", "SyPro", marks=pytest.mark.xfail(reason="string is not a string")),
            pytest.param("SkyPro", 123, "SkyPro", marks=pytest.mark.xfail(reason="symbol is not a string"))
                        ])
def test_starts_with_negative(string, symbol, result):
    stringutals = StringUtils()
    res = stringutals.starts_with(string, symbol)
    assert res == result

# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет (Позитивные)
@pytest.mark.parametrize('string, symbol, result', [
                        ('Text', 't', True),
                        ('texTTT', 'TTT', True),
                        ('123', '23', True),
                        ('end with space ', ' ', True),
                        ('Text', 'x', False),
                        ('SkyPro', 'Sky', False)
                        ])
def test_end_with_positive(string, symbol, result):
    stringutals = StringUtils()
    res = stringutals.end_with(string, symbol)
    assert res == result

# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет (Негативные)
@pytest.mark.parametrize('string, symbol, result', [
                        ('', '', True),
                        (' ', ' ', True),
            pytest.param("SkyPro", None, TypeError, marks=pytest.mark.xfail(reason="symbol is None")),
            pytest.param(None, None, AttributeError, marks=pytest.mark.xfail(reason="string and symbol is None")),
            pytest.param(None, "k", AttributeError, marks=pytest.mark.xfail(reason="string is None")),
            pytest.param(123, "k", AttributeError, marks=pytest.mark.xfail(reason="string is not a string")),
            pytest.param("SkyPro", 123, TypeError, marks=pytest.mark.xfail(reason="symbol is not a string"))
                        ])
def test_end_with_negative(string, symbol, result):
    stringutals = StringUtils()
    res = stringutals.end_with(string, symbol)
    assert res == result

# Возвращает `True`, если строка пустая и `False` - если нет (Позитивные)
@pytest.mark.parametrize('string, result', [
                        ('Text', False),
                        (' ///', False),
                        ('123', False),
                        ('', True)
                        ])
def test_is_empty_positive(string, result):
    stringutals = StringUtils()
    res = stringutals.is_empty(string)
    assert res == result

# Возвращает `True`, если строка пустая и `False` - если нет (Негативные)
@pytest.mark.parametrize('string, result', [
                        ('', True),
                        (' ', True),
            pytest.param(None, AttributeError, marks=pytest.mark.xfail(reason="string is None")),
            pytest.param(123, TypeError, marks=pytest.mark.xfail(reason="string is not a string")),
                        ('()#%@^!&*', False),
                        ])
def test_is_empty_negative(string, result):
    stringutals = StringUtils()
    res = stringutals.is_empty(string)
    assert res == result


# Преобразует список элементов в строку с указанным разделителем
# Проверка использования значения разделителя присваемого автоматически в самой функции
def test_list_to_string_default_joiner():
    stringutals = StringUtils()
    lst = ["Hello", "World"]
    res = stringutals.list_to_string(lst)
    assert res == "Hello, World"
# Позитивные
@pytest.mark.parametrize('lst, joiner, result', [
                        ([1,2,3,4], ' , ', '1 , 2 , 3 , 4'),
                        (['Sky', 'Pro'], '-', 'Sky-Pro'),
                        (['hello', 'world'], '', 'helloworld'),
                        (["one", 2, 3, 4, 'five'], ' ', 'one 2 3 4 five')
                        ])
def test_list_to_string_positive(lst, joiner, result):
    stringutals = StringUtils()
    res = stringutals.list_to_string(lst, joiner)
    assert res == result
# Негативные
@pytest.mark.parametrize('lst, joiner, result', [
                        ([1.2,2.2,3.2], '', '1.22.23.2'),
                        (['*', 2, 'hi', '&$(!)#$'], ' and ', "* and 2 and hi and &$(!)#$"),
                        ([1,2,3], None, 'error'),
                        (None, '', '123'),
            pytest.param('not list', ' ', AttributeError, marks=pytest.mark.xfail(reason="Lst is not a list")),
            pytest.param([1,2,3,4], [1,2,3], AttributeError, marks=pytest.mark.xfail(reason="Joiner is not a string"))
                        ])
def test_list_to_string_negative(lst, joiner, result):
    stringutals = StringUtils()
    if lst is None:
        pytest.xfail('List is None')
    elif joiner is None:
        pytest.xfail('Joiner is None')
    res = stringutals.list_to_string(lst, joiner)
    assert res == result