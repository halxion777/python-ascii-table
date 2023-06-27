from ascii_table import CreateAsciiTable



if __name__ == "__main__":
    data = a = [{
"first_name": "John",
"last_name": "Doe",
"age": 15 ,
"gender": "male"
}]
    ascii_table = CreateAsciiTable()
    table = ascii_table.create_table(data, keys=("first_name","last_name"))
    print(table)