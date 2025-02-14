import pytest
from topic3.example1.click import get_hyperlinks    


def test_click_good():
    links = get_hyperlinks("http://example.com")
    assert links == ["https://www.iana.org/domains/example"]

def test_click_not_ound():
    links = get_hyperlinks("https://www.google.com/not-found.html")
    assert links == []

def test_click_not_ound():
    # Typo on purpose
    links = get_hyperlinks("https://uitm.edu.ny")
    assert links == []
