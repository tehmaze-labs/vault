from vault import Vault
import unittest

class Options(object):
    filename = '.testvault'
    keyfile = ''
    verbose = True

class VaultTest(unittest.TestCase):
    def setUp(self):
        self.vault = Vault(Options)
        self.vault.secret = 'secret'
        self.vault.check_crypt()

    def testEncrypt(self):
        plain = 'hello world'
        for x in xrange(0, 10):
            tests = ''.join([plain, str(x)])
            crypt = self.vault.encrypt(tests)
            print tests
            print crypt
            self.assertEqual(tests, self.vault.decrypt(crypt))

    def __del__(self):
        self.vault.destroy_vault()

if __name__ == '__main__':
    unittest.main()

