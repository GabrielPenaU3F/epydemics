from src.analyzers.contagion_fitter import ContagionFitter


class ParameterAnalyzer:

    def analyze_parameters_over_time(self, data, start_from):

        a_params = []
        b_params = []
        t_sequence = data.get_days()[start_from:len(data.get_days())]

        for day in t_sequence:
            fitter = ContagionFitter()
            a, b = fitter.determine_coefficients_until(data, day)
            a_params.append(a)
            b_params.append(b)

        return a_params, b_params

