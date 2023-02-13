from crcset.crcset_wasi import crc16xmodem, crc32c


def test_crc32c():
    assert crc32c("testing-crc32c".encode("utf-8")) == 4017753803


def test_crc16xmodem():
    assert crc16xmodem("testing-crc16-xmodem".encode("utf-8")) == 26763
