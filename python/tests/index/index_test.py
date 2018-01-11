# -*- coding: utf-8 -*-
# Usage: py.test tests

import keyvi
import os
import shutil
import tempfile


def test_open_index():
    test_dir = os.path.join(tempfile.gettempdir(), "index_writer_test", "index")
    try:
        os.makedirs(test_dir)
        index = keyvi.Index(os.path.join(test_dir, "index"))
        index.Set("a", "{}")
        del index
    finally:
        shutil.rmtree(test_dir)
    