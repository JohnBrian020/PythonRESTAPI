
from unittest.mock import patch
import cli


@patch("cli.requests.get")
def test_show_inventory(mock_get):
    mock_get.return_value.json.return_value = [
        {"id": 1, "name": "Milk"}
    ]

    cli.show_inventory()

    mock_get.assert_called_once_with(
        "http://127.0.0.1:5555/inventory"
    )


@patch("cli.requests.post")
@patch("builtins.input")
def test_add_item(mock_input, mock_post):
    mock_input.side_effect = ["Bread", "Tuskys", "100", "5"]

    cli.add_item()

    mock_post.assert_called_once()