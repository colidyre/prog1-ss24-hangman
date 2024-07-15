from main import choose_word


def test_choose_word_with_empty_list():
    func_input = []
    expected_output = "Python"
    result = choose_word(func_input)
    assert result == expected_output


def test_choose_word_with_only_one_word():
    func_input = ["Rust"]
    expected_output = "Rust"
    result = choose_word(func_input)
    assert result == expected_output


def test_choose_word_with_multiple_words():
    func_input = ["Rust", "Python"]
    for _ in range(100):
        result = choose_word(func_input)
        assert "Rust" in result or "Python" in result


def test_choose_word_with_newlines():
    func_input = ["  Python\n"]
    expected_output = "Python"
    result = choose_word(func_input)
    assert result == expected_output
