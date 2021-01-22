import scipy.optimize as opt


class ContagionModel:

    def fit(self, x, y):
        params, cov = opt.curve_fit(self.mean_value_function, x, y, p0=(0.1, 1), method='lm')
        return params

    def mean_value_function(self, x, a, b):
        return ((1 + a * x)**b - 1)/b

    def calculate_mtb(self, data, start_from):
        mtbs = []
        t_sequence = data.get_days()[start_from:len(data.get_days())]
        for day in t_sequence:
            a, b = self.determine_coefficients_until(data, day)
            mtb = self.calculate_estimated_mtb(a, b, day)
            mtbs.append(mtb)
        return mtbs

    def determine_coefficients_until(self, data, until_day):
        days = data.get_days()[0:until_day - 1]
        values = data.get_values()[0:until_day - 1]
        return self.fit(days, values)

    def calculate_estimated_mtb(self, a, b, day):
        parenthesis = 1 + a * day
        mtb = parenthesis / (a * (parenthesis**b - 1))
        return mtb
