import unittest
from stream_cyphers import RC4
from pathlib import Path


class Test_StreamCyphers_RC4(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Get path for relevant test files
        project_root = Path(__file__).resolve().parents[2]
        big_file_path = project_root / 'test_data' / 'KJV.txt'
        with open(big_file_path, 'rb') as f:
            cls.large_input = f.read()

    def test_encrypt_decrypt(self):
        testText = "Plain text test. Testing.".encode('utf-8')
        testKey = "testkey"
        encripted = RC4.encrypt(testText, testKey)
        decripted = RC4.decrypt(encripted, testKey)
        self.assertEqual(decripted, testText)

    # Empty, small and large inputs. For large inputs use KJV?
    def test_empty_message(self):
        testText = "".encode('utf-8')
        testKey = "testKey"
        encrypted = RC4.encrypt(testText, testKey)
        decrypted = RC4.decrypt(encrypted, testKey)
        self.assertEqual(decrypted, testText)

    def test_large_message(self):
        testKey = "testKey"
        encripted = RC4.encrypt(self.large_input, testKey)
        decrypted = RC4.decrypt(encripted, testKey)
        self.assertEqual(decrypted, self.large_input)

if __name__ == "__main__":
    unittest.main()