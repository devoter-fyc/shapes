## Lines
* Line is a module that provides support for lines.
* This is still **BASIC** , so do **_not_** use it in **PRODUCTION USE**.
## Basic usage
* To initialize a "Line",or **LENGTHED** line,use this:
```python
>>>import lines
>>>a = line.Line(10)
```
* Good.You initialized a line.Now you should use it for other purposes:
```python
>>>a.len()
10
>>>len(a)
10
```
* You could use either len(x) or x.len() to get the length.
* Another way of getting length is also supported:
```python
>>>a.getlen()
10
```
* However,this is not favoured by the author and **WILL** be deprecated in the future.
* This is the whole basic use.
## Advanced
* You can initialize the line with **TWO** and **ONLY TWO** points:
```python
>>>b = line.Line(10,"Hi","Goodbye")
```
* Use x.getpoint() to get that:
```python
>>>b.getpoint()
['Hi','Goodbye']
```
* You can change the length and the points,respectively using x.mutlen() and x.mutpoint():
```python
>>>a.mutlen(1)
>>>a.len()
1
>>>b.mutpoint("A","B")
>>>b.getpoint()
['A','B']
```
* Points are set to default "\["A","B"]".
### NoLengthLine
* You can create a line with an infinity length(in chinese,"直线".)
* Do this by:
```python
>>>import lines
>>>c = lines.NoLengthLine()
```
#### NoLengthLineAdvancedOptions
* NoLengthLine accept a list as "points".
```python
>>>d = lines.NoLengthLine(["A","B"])
```
* You can mutate & get points like:
```python
>>>d.getpoints()
["A","B"]
>>>d.mutpoints(["C","D"])
>>>d.getpoints()
["C","D"]
```
