# -*- coding: utf-8 -*-
"""
@brief      test log(time=18s)
"""
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, add_missing_development_version
import ensae_teaching_cs


class TestLONGNotebookRunner2aEco(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner_2a_eco_nlp_long(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # Requires authentification.
            return

        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_eco_nlp_long")
        keepnote = ls_notebooks("td2a_eco")
        shutil.copy(simple_database(), temp)

        folder = os.path.join(temp, "ressources_googleplus")
        if not os.path.exists(folder):
            os.mkdir(folder)
        jsfile = os.path.join(os.path.dirname(keepnote[0]),
                              "ressources_googleplus", "107033731246200681024.json")
        shutil.copy(jsfile, folder)

        def filter(i, n):
            if "td2a_TD5_Traitement_automatique_des_langues_en_Python" in n:
                return True
            return False

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
