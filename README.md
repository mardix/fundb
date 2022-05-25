# FunDB

WIP

A document store build on SQLite, leveraging the power of SQLite and JSON



### Install

```
pip install python-fundb
```

### Usage

```
from fundb import fundb


fun = fundb()

# insert
f = fun.mycollection.insert({
  "name": "Fun",
  "type": "DB"
})

f.name # -> fun 
f.type # -> DB


```



