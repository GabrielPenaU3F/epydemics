class Fit:

    def __init__(self, source, location, dataset_type, x, y, explained, params, rsq):
        self.source = source
        self.location = location
        self.dataset_type = dataset_type
        self.x_data = x
        self.y_data = y
        self.explained = explained
        self.params = params
        self.rsq = rsq

    def get_source(self):
        return self.source

    def get_dataset_type(self):
        return self.dataset_type

    def get_explained_data(self):
        return self.explained

    def get_x_data(self):
        return self.x_data

    def get_y_data(self):
        return self.y_data

    def get_params(self):
        return self.params

    def get_rsq(self):
        return self.rsq

    def get_location(self):
        return self.location
