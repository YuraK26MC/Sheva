import datetime
from price_analysis import read_data, analyze_price_changes
from freezegun import freeze_time
import pytest

@freeze_time("2023-04-13")
def test_read_data(monkeypatch):
    test_data = [
        ("Soda", "2022-07-11", "2.00"),
        ("Soda", "2022-08-13", "2.00"),
        ("Soda", "2022-09-15", "2.50")
    ]
    # Функція для мокування читання файлу
    def mock_open(*args, **kwargs):
        from io import StringIO
        content = '\n'.join([','.join(row) for row in test_data])
        return StringIO(content)

    monkeypatch.setattr("builtins.open", mock_open)
    results = read_data("dummy_path.txt", "Milk")
    assert results == [(datetime.date(2023, 4, 10), 1.25), (datetime.date(2023, 4, 12), 1.30)]

def test_analyze_price_changes():
    data = [(datetime.date(2023, 4, 10), 1.25), (datetime.date(2023, 4, 12), 1.30)]
    result = analyze_price_changes(data)
    assert result['start_price'] == pytest.approx(1.25)
    assert result['end_price'] == pytest.approx(1.30)
    assert result['price_change'] == pytest.approx(0.05)
    