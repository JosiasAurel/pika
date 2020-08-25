

## When you query your tiny database with a specific field (search), it rrturns you a single list containing all matches. 

```python
>>> from tinydb import TinyDB, query
>>> db.inder({'name':'John', 'age':'47'})
>>> db.search(User.name == 'John')
[{'name':'John', 'age':'47'}]
```

Nice one 