"""
@brief      test log(time=3s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.filehelper import get_url_content_timeout


class TestExam20161Ahttp(unittest.TestCase):

    def test_hash_http(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def get_code(mail):
            import hashlib
            m = hashlib.md5()
            m.update(mail)
            b = m.digest()
            return int(b[0])

        for bbb in [b"a", b"a@a", b"any@ensae.fr", b"ensae.frs"]:
            code = get_code(bbb)
            url = "http://www.xavierdupre.fr/enseignement/examens/1A_2016/enonce_%d.txt" % code
            content = get_url_content_timeout(url)
            assert 0 <= code <= 255
            assert len(content) > 0


if __name__ == "__main__":
    unittest.main()
