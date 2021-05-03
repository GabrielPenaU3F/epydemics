class FullDataset:

    source_id = None
    raw_data = None

    def __init__(self, source_id, raw_data):
        self.source_id = source_id
        self.raw_data = raw_data

    def get_source_id(self):
        return self.source_id

    def get_raw_data(self):
        return self.raw_data
