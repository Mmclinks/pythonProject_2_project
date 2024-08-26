from src.user_interface import delete_vacancy, filter_data, search_query


def test_search_query(monkeypatch):
    inputs = iter(["Python", 20, 2])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    results = search_query()
    assert results == ("Python", 2, 20)


def test_search_query_invalid_data(monkeypatch):
    inputs = iter(["Python", "abc", 2])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    results = search_query()
    assert results is None


def test_filter_data(monkeypatch):
    inputs = iter(["Python", 100, 5])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    results = filter_data()
    assert results == ("Python", 100, 5)


def test_filter_data_not_salary(monkeypatch):
    inputs = iter(["Python", "", 5])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    results = filter_data()
    assert results == ("Python", 0, 5)


def test_filter_data_invalid_salary(monkeypatch):
    inputs = iter(["Python", "abc", 5])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    results = filter_data()
    assert results is None


def test_filter_data_invalid_top_n(monkeypatch):
    inputs = iter(["Python", 100, "abc"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    results = filter_data()
    assert results is None


def test_delete_vacancy(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 100)

    results = delete_vacancy()
    assert results == 100


def test_delete_vacancy_invalid_data(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "abc")

    results = delete_vacancy()
    assert results is None
