"""Dictionary Problems - Testing student capability with dictionary operations."""


def dictionary_operations(dict1, dict2):
    """Perform basic operations on two dictionaries."""
    merged = {**dict1, **dict2}
    common_keys = set(dict1.keys()) & set(dict2.keys())
    unique_keys = set(dict1.keys()) ^ set(dict2.keys())

    return {
        "merged": merged,
        "common_keys": common_keys,
        "unique_keys": unique_keys
    }


def count_word_frequency(text):
    """Count the frequency of each word in a text string."""
    words = text.split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def dictionary_filtering(students_grades):
    """Filter students based on their grades."""
    return {name: grade for name, grade in students_grades.items() if grade >= 70}


def nested_dictionary_access(nested_dict, keys_path):
    """Access value in nested dictionary using a list of keys."""
    current = nested_dict

    for key in keys_path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None

    return current


if __name__ == "__main__":
    print("Testing dictionary_operations...")
    result = dictionary_operations({"a": 1, "b": 2}, {"b": 3, "c": 4})
    expected = {"merged": {"a": 1, "b": 3, "c": 4}, "common_keys": {"b"}, "unique_keys": {"a", "c"}}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing count_word_frequency...")
    result = count_word_frequency("hello world hello python world")
    expected = {"hello": 2, "world": 2, "python": 1}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing dictionary_filtering...")
    result = dictionary_filtering({"Alice": 85, "Bob": 65, "Charlie": 90, "Diana": 45})
    expected = {"Alice": 85, "Charlie": 90}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing nested_dictionary_access...")
    nested = {"level1": {"level2": {"level3": "found"}}}
    result = nested_dictionary_access(nested, ["level1", "level2", "level3"])
    assert result == "found"

    result = nested_dictionary_access(nested, ["level1", "nonexistent"])
    assert result is None

    print("All tests passed!")