# python-ascii-table
**a simple ascii table creator python**

### No filter sample:
```
a = [{
"first_name": "John",
"last_name": "Doe",
"age": 15 ,
"gender": "male"
}]
ascii_table = CreateAsciiTable()
table = ascii_table.create_table(data)
print(table)
```


<pre>+------------+-----------+-----+--------+
| first_name | last_name | age | gender |
+------------+-----------+-----+--------+
| John       | Doe       | 15  | male   |
+------------+-----------+-----+--------+</pre>

### filter sample:
```
a = [{
"first_name": "John",
"last_name": "Doe",
"age": 15 ,
"gender": "male"
}]
ascii_table = CreateAsciiTable()
table = ascii_table.create_table(data, keys=("first_name","last_name"))
print(table)
```

<pre>+------------+-----------+
| first_name | last_name |
+------------+-----------+
| John       | Doe       |
+------------+-----------+</pre>