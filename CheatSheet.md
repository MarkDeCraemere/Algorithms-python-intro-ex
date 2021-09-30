# Cheatsheet
## Loops
```C#
for (int i = 0; i <= 5; i++) { 
    // Code 
}

while (true) {
    // Code
}

foreach (item in List){
    // Code
}

do{
    // Code
} while (true);
```

```python
for i in range(0, 5):
    # Code

while True:
    # Code

for item in List:
    # Code

# No do While loop in python
```

## Classes

```C#
public class Class
{
    public Class() {}

    public Class(myValue)
    {
        classValue = myValue;
    }

    private int classValue;

    public int ClassFunction(){
        return classValue;
    }
}

Class myClass = new Class();
Class mySecondClass = new Class(5);

mySecondClass.ClassFunction();
```

```python
class Class:
    def __init__(self):
        pass

    def __init__(self, value):
        self.classValue = value

    def ClassFunction(self):
        return self.classValue

myClass = Class()
mySecondClass = Class(5)

mySecondClass.ClassFunction()
```


```C#
```

```python
```