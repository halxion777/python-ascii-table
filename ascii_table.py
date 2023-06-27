class CreateAsciiTable:
    def create_table(self, data, keys=None):
        if keys:
            new_data = []
            for row in data:
                new_data.append({key: row[key] for key in keys})
        else:
            new_data = data
        return "\n".join(self._create_ascii_table(new_data))

    def _create_ascii_table(self, table):
        table_keys = {header: [] for header in table[0].keys()}
        for row in table:
            for header, value in row.items():
                table_keys[header].append(value)

        ascii_table = []
        for key, value in table_keys.items():
            ascii_table.append(self._create_ascii_column(key, value))
        ascii_table.append(self._create_ends(len(ascii_table[0]) - 3))
        return ["".join(item) for item in zip(*ascii_table)]

    def _create_ends(self, num_items):
        ends = ["+", "|", "+"]
        for item in range(num_items - 1):
            ends.append("|")
        ends.append("+")
        return ends

    def _center_item(self, max_len, item):
        space_left = max_len - len(item)
        left_space = space_left // 2
        right_space = max_len - (left_space + len(item))
        item = f'|{" " * left_space}{item}{" " * right_space}'
        return item

    def _create_ascii_column(self, header, values):
        items = [header, *list(values)]
        max_len_string = min(60, len(max(items, key=lambda item: len(str(item))))) + 2
        ascii_column = []
        dashes = f"+{'-' * (max_len_string)}"
        ascii_column.append(dashes)
        header_area = self._center_item(max_len_string, header)
        ascii_column.append(header_area)
        ascii_column.append(dashes)
        for value in values:
            value_len = 60 if len(str(value)) > 60 else len(str(value))
            if value_len == 60:
                value = f"{value[:57]}..."
            ascii_column.append(f'| {value}{" " * ((max_len_string - value_len) - 1)}')
        ascii_column.append(dashes)
        return ascii_column

