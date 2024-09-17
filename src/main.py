from src.fetch_from_source import fetch_from_source
from src.get_first_in_list import get_first_in_list
from src.process_list import process_list


def get_first_processed() -> str:
    source_list = fetch_from_source()
    processed_list = process_list(source_list)
    return get_first_in_list(processed_list)


if __name__ == '__main__':
    print(get_first_processed())
