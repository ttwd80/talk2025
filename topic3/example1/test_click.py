import pytest
from topic3.example1.click import get_hyperlinks


def test_click_good_one():
    # test valid page with one link
    links = get_hyperlinks("http://example.com")
    assert links == ["https://www.iana.org/domains/example"]


def test_click_good_different():
    # test valid page with one link
    links = get_hyperlinks("https://www.q.wa-k12.net/lkwashSTS")
    assert links == ["/lkwashSTS/Account/ForgotPassword"]


def test_click_not_ound():
    # test valid domain, 404 error
    links = get_hyperlinks("https://www.google.com/not-found.html")
    assert links == []


def test_click_bad_domain():
    # test bad domain
    # Typo on purpose
    links = get_hyperlinks("https://not-uitm.ecu.ny")
    assert links == []
