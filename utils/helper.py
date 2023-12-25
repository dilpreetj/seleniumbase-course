def assert_list_text(base_case, list_selector, expected_text):
    """
    Verifies the text of each element in a list matches the expected text
    :param base_case: Instance of BaseCase.
    :param list_selector: CSS selector for the list elements.
    :param expected_text: List of expected text for each element.

    Usage:
    assert_list_text(base_case, ".menu_item", ["Home", "About"])
    """
    for i, text in enumerate(expected_text, start=1):
        base_case.assert_text(text, f'{list_selector}:nth-child({i})')
