from src.main import get_first_processed


def test_get_first_processed(mocker):
    mock_fetch_from_source = mocker.patch('src.main.fetch_from_source', return_value=["a", "b", "c"])
    mock_process_list = mocker.patch('src.main.process_list', return_value=["pa", "pb", "pc"])
    mock_get_first_in_list = mocker.patch('src.main.get_first_in_list', return_value="pa")

    assert get_first_processed() == "pa"

    mock_fetch_from_source.assert_called_once()
    mock_process_list.assert_called_once_with(["a", "b", "c"])
    mock_get_first_in_list.assert_called_once_with(["pa", "pb", "pc"])








