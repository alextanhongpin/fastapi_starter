# Custom Exception

In Python, you can define a custom exception this way:

```python
class AppError(Exception):
    def __init__(self, reason, message="An error has occured"):
        self.code = self.__class__.__name__
        self.reason = reason
        self.message = message
        super().__init__(self.message)
```



Note that we assign the `self.code` with the class name. So the following will be true:

```python
exc = AppError('You do not have access')
assert exc.code == 'AppError'
```


You can now extend the `AppError` to create other errors that fits your application:

```python
class AlreadyExistsError(AppError):
    def __init__(self, reason, message="Resource already exist"):
        super().__init__(reason, message)
```


These errors will be instance of the `AppError`. You can use the `isinstance` function to verify them:

```python
assert isinstance(AlreadyExistsError('User'), AppError) == True
```
