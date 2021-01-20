class Sheet:

    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.columns = self.build_columns()

    def get_column(self, col_name):
        return self.columns.get(col_name)

    def build_columns(self):
        columns = {}
        colnames = self.data[0]
        for i in range(len(colnames)):
            column = []
            for j in range(1, len(self.data)):
                column.append(self.data[j][i])
            columns[colnames[i]] = column
        return columns

    def get_raw_data(self):
        return self.data
