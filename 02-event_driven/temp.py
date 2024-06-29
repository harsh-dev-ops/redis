from pydantic import BaseModel
import inspect


def optional(*fields, deep: bool = True):
    """
    Makes specified fields optional.
    If no fields are specified, makes all fields optional.
    To not recursively make all fields of nested models optional as well, pass deep=False
    """
    # Work is done inside optionalize
    def optionalize(_cls):
        for field in fields:
            subfield = _cls.__fields__[field]
            if deep and inspect.isclass(subfield.type_) and issubclass(subfield.type_, BaseModel):
                # Must pass through optional so that fields variable gets prepared
                optional(subfield.type_, deep=deep)
            subfield.required = False
        return _cls

    # Decorator (only used if parameters are passed to optional)
    def decorator(_cls):
        return optionalize(_cls)

    # If no parameters are passed to optional, return the result of optionalize (which is a class callable)
    if fields and inspect.isclass(fields[0]) and issubclass(fields[0], BaseModel):
        cls = fields[0]
        fields = cls.__fields__
        return optionalize(cls)
    # Else, return the generated decorator
    return decorator


class Book(BaseModel):
    author: str
    available: bool
    isbn: str


@optional
class BookUpdate(Book):
    pass


@optional('val1', 'val2')
class Model(BaseModel):
    val1: str
    val2: str
    captcha: str