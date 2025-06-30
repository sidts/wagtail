import pytest
from wagtail.contrib.redirects.oi import RedirectsImporter

def test_importer_clears_cache_after_multiple_imports():
    importer = RedirectsImporter()
    importer.import_from_file("dummy1.csv")
    importer.import_from_file("dummy2.csv")
    assert len(importer._storage) == 0


