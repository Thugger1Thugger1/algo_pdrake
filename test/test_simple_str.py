from simple_str import find

def test_works_with_single_char():
    string = 'bruh'
    assert find(string, 'h') == 3

def test_works_with_long_word():
    string = 'the is how we do it'
    assert find(string, 'how') == 7    