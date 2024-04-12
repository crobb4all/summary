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
                                            (None, None),
                                            (None, '')])
def test_capitalize_negative(string, result):
    if string is None:
        pytest.xfail("Capitalize возвращает ошибку для ввода None")


# Тесты для удаления пробелов вначале строки
@pytest.mark.parametrize('string, result', [(' Text', 'Text'), 
                                            ('two words', 'two words'), 
                                            ('123', '123'), 
                                            ('04 апреля 2023', '04 апреля 2023'), 
                                            ('', ''),
                                            (' ', ''),
                                            (None, None)])
def test_trim(string, result):
    stringutals = StringUtils()
    if string is None:
        pytest.xfail("trim должен возвращать None для ввода None")    
    res = stringutals.trim(string)
    assert res == result

# Обработка текста с разделителем и возвращение списка строк
@pytest.mark.parametrize('string, delimiter, result', 
                        [('text, and, next-text', ',', ['text', ' and', ' next-text']),
                        ('a,b,c,d', ',', ['a', 'b', 'c', 'd']),
                        ('1:2:3', ':', ['1', '2', '3']),
                        ('', ',', []),
                        (' ', ',', []),
                        (None, ',', None)])
def test_to_list(string, delimiter, result):
    stringutals = StringUtils()
    if string is None:
        pytest.xfail("to_list должен возвращать None для ввода None")     
    res = stringutals.to_list(string, delimiter)
    assert res == result

# Возвращение `True`, если строка содержит искомый символ и `False` - если нет
@pytest.mark.parametrize('string, symbol, result', 
                        [('text and, next-text', ' and', True),
                        ('abcd', 'g', False),
                        ('04 апреля 2023', '04', True),
                        ('', '', True),
                        (' ', '', True),
                        (None, None, True)])
def test_contains(string, symbol, result):
    stringutals = StringUtils()
    if string is None:
        pytest.xfail("Contains должен возвращать None для ввода None")
    res = stringutals.contains(string, symbol)
    assert res == result

# Удаление подстрок из строки (Позитивный)
@pytest.mark.parametrize('string, symbol, result', 
                        [('text and, next-text', ' and', 'text, next-text'),
                        ('04 апреля 2023', '04', ' апреля 2023'),
                        ('', '', ''),
                        (' ', ' ', '')])
def test_delete_symbol_positive(string, symbol, result):
    stringutals = StringUtils()
    if string is None:
        pytest.xfail("Delete_symbol должен возвращать None для ввода None")
    res = stringutals.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
                        (None, "k", AttributeError),
                        ("SkyPro", None, TypeError),
                        ("", "k", ""),
                        ("SkyPro", "", "SkyPro"),
                        ("SkyPro", "x", "SkyPro"),
                        (123, "k", AttributeError),
                        ("SkyPro", 123, TypeError)])
def test_delete_symbol_negative(string, symbol, result):
    stringutals = StringUtils()
    if result == TypeError:
        with pytest.raises(TypeError):
            stringutals.delete_symbol(string, symbol)
    elif result == AttributeError:
        with pytest.raises(AttributeError):
            stringutals.delete_symbol(string, symbol)
    else:
        res = stringutals.delete_symbol(string, symbol)
        assert res == result
