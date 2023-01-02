from py_crc32c import crc32c


def test_crc32c():
    assert crc32c("testing-crc32c".encode("utf-8")) == 4017753803
