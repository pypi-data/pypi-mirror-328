# SPDX-FileCopyrightText: 2022-2025 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import unittest
from sphinx.application import Sphinx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocTest(unittest.TestCase):

    def setUp(self):
        self.source_dir = u'docs/source'
        self.config_dir = u'docs/source'
        self.output_dir = u'docs/build/_html'
        self.doctree_dir = u'docs/build/_html/.doctrees'
        self.all_files = 1

    def test_html_documentation(self):
        app = Sphinx(self.source_dir,
                     self.config_dir,
                     self.output_dir,
                     self.doctree_dir,
                     buildername='html',
                     warningiserror=True,
        )
        app.build(force_all=self.all_files)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
