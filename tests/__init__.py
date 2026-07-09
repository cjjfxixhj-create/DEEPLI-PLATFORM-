"""Tests for DEEPLI platform."""

from deepli import hello, Platform


def test_hello():
    assert hello() == "Hello from DEEPLI"


def test_platform_status():
    p = Platform("Test")
    assert p.status() == "Test is running"
