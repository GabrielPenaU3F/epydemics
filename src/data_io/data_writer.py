class DataWriter:

    @classmethod
    def write_to_csv(cls, data, path):
        data.to_csv(path)
