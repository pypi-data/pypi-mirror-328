import unittest
from pyunixlzw import decompress

TEST_DATA_DIR = './data'

def get_testfile_data(filename, src='pyunixlzw', maxbits=None):
    ufilepath = f"{TEST_DATA_DIR}/original/{filename}"
    
    if maxbits is not None:
        cfilepath = f"{TEST_DATA_DIR}/{src}/{filename.split('.')[0]}_maxbits{maxbits}.txt.Z"
    else:
        cfilepath = f"{TEST_DATA_DIR}/{src}/{filename}.Z"
    with open(ufilepath, 'rb') as f:
        decompressed_data = f.read()
    with open(cfilepath, 'rb') as f:
        compressed_data = f.read()
    
    return (compressed_data, decompressed_data)
    

class Test_decompress(unittest.TestCase):

    def test_empty(self):
        """Verify valid compression of empty data."""
        compressed_data, decompressed_data = get_testfile_data('empty')
        test_output = decompress(compressed_data)
        self.assertEqual(test_output, decompressed_data)
    
    def test_small(self):
        """Verify valid compression of small text data."""
        compressed_data, decompressed_data = get_testfile_data('small.txt')
        test_output = decompress(compressed_data)
        self.assertEqual(test_output, decompressed_data)
    
    def test_large(self):
        """Verify valid compression of large text data."""
        compressed_data, decompressed_data = get_testfile_data('large.txt')
        test_output = decompress(compressed_data)
        self.assertEqual(test_output, decompressed_data)
    
    def test_ascii(self):
        """Verify valid compression of ascii data."""
        compressed_data, decompressed_data = get_testfile_data('full_ascii.bin')
        test_output = decompress(compressed_data)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_10(self):
        """Verify valid compression of large text data with a maximum bit length of 10."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', maxbits='10')
        test_output = decompress(compressed_data, max_bit_len=10)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_11(self):
        """Verify valid compression of large text data with a maximum bit length of 11."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', maxbits='11')
        test_output = decompress(compressed_data, max_bit_len=11)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_12(self):
        """Verify valid compression of large text data with a maximum bit length of 12."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', maxbits='12')
        test_output = decompress(compressed_data, max_bit_len=12)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_13(self):
        """Verify valid compression of large text data with a maximum bit length of 13."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', maxbits='13')
        test_output = decompress(compressed_data, max_bit_len=13)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_14(self):
        """Verify valid compression of large text data with a maximum bit length of 14."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', maxbits='14')
        test_output = decompress(compressed_data, max_bit_len=14)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_15(self):
        """Verify valid compression of large text data with a maximum bit length of 15."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', maxbits='15')
        test_output = decompress(compressed_data, max_bit_len=15)
        self.assertEqual(test_output, decompressed_data)


class Test_ncompress(unittest.TestCase):

    def test_empty(self):
        """Verify valid compression of empty data."""
        compressed_data, decompressed_data = get_testfile_data('empty', src='ncompress')
        test_output = decompress(compressed_data)
        self.assertEqual(test_output, decompressed_data)
    
    def test_small(self):
        """Verify valid compression of small text data."""
        compressed_data, decompressed_data = get_testfile_data('small.txt', src='ncompress')
        test_output = decompress(compressed_data)
        self.assertEqual(test_output, decompressed_data)
    
    def test_large(self):
        """Verify valid compression of large text data."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', src='ncompress')
        test_output = decompress(compressed_data)
        self.assertEqual(test_output, decompressed_data)
    
    def test_ascii(self):
        """Verify valid compression of ascii data."""
        compressed_data, decompressed_data = get_testfile_data('full_ascii.bin', src='ncompress')
        test_output = decompress(compressed_data)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_10(self):
        """Verify valid compression of large text data with a maximum bit length of 10."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', src='ncompress', maxbits='10')
        test_output = decompress(compressed_data, max_bit_len=10)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_11(self):
        """Verify valid compression of large text data with a maximum bit length of 11."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', src='ncompress', maxbits='11')
        test_output = decompress(compressed_data, max_bit_len=11)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_12(self):
        """Verify valid compression of large text data with a maximum bit length of 12."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', src='ncompress', maxbits='12')
        test_output = decompress(compressed_data, max_bit_len=12)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_13(self):
        """Verify valid compression of large text data with a maximum bit length of 13."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', src='ncompress', maxbits='13')
        test_output = decompress(compressed_data, max_bit_len=13)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_14(self):
        """Verify valid compression of large text data with a maximum bit length of 14."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', src='ncompress', maxbits='14')
        test_output = decompress(compressed_data, max_bit_len=14)
        self.assertEqual(test_output, decompressed_data)
    
    def test_maxbits_15(self):
        """Verify valid compression of large text data with a maximum bit length of 15."""
        compressed_data, decompressed_data = get_testfile_data('large.txt', src='ncompress', maxbits='15')
        test_output = decompress(compressed_data, max_bit_len=15)
        self.assertEqual(test_output, decompressed_data)
    

if __name__ == '__main__':
    unittest.main()