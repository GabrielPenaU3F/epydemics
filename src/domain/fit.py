class Fit:

    def __init__(self, country, dataset_type, x, y, explained, params, rsq):
        self.country = country
        self.dataset_type = dataset_type
        self.x_data = x
        self.y_data = y
        self.explained = explained
        self.params = params
        self.rsq = rsq

    def get_dataset_type(self):
        return self.dataset_type

    def get_x_data(self):
        return self.x_data

    def get_y_data(self):
        return self.x_data

    def get_params(self):
        return self.params

    def get_rsq(self):
        return self.rsq

    def get_country(self):
        return self.country
