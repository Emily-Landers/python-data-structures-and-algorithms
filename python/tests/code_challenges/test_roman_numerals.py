from code_challenges.roman_numerals import roman_to_arabic, convert_character, printRoman

def test_exists():
    assert roman_to_arabic
    assert convert_character
    assert printRoman
    
def test_roman_to_arabic():
    num = roman_to_arabic('XI')
    assert num == 11

def test_roman_to_arabic2():
    num = roman_to_arabic('MI')
    assert num == 1001
    
def test_convert_character():
    num = convert_character('M')
    assert num == 1000
    

