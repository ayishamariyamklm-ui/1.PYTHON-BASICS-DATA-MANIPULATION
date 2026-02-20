def remove_duplicates(data):
    return list(set(data))


def filter_positive_numbers(data):
    return [x for x in data if x > 0]


def clean_data(data):
    unique_data = remove_duplicates(data)
    filtered_data = filter_positive_numbers(unique_data)
    return filtered_data


if __name__ == "__main__":
    raw_data = [10, -5, 20, 10, 30, -1, 20, 40]
    cleaned_data = clean_data(raw_data)

    print("Original Data:", raw_data)
    print("Cleaned Data:", cleaned_data)
