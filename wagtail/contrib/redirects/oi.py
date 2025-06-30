class RedirectsImporter:
    def __init__(self):
        self._storage = []

    def import_from_file(self, filename):
        self._storage.extend([1, 2, 3, 4, 5])
        self.clear_cache()

    def clear_cache(self):
        self._storage.clear()
