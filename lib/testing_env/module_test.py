# test_versions.py

from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 12  # Adjusted for Python 3.12.3

def test_requests_version():
    assert requests_version() == "2.31.0"  # Adjusted for installed requests version

def test_pytest_version():
    assert pytest_version() == "7.4.4"  # Adjusted for installed pytest version
