from crcset import crc16, crc32c


def test_crc32c():
    assert crc32c("testing-crc32c".encode("utf-8")) == 4017753803


def test_crc16():
    assert crc16("testing-crc16-xmodem".encode("utf-8")) == 26763
