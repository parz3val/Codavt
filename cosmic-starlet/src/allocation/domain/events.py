from dataclasses import dataclass

# These events are the dataclassees which will be raise by the model
# These events are being used for the control flow.
# Using Exceptions for the control flow is the sign of smelly code
class Event:
    pass


@dataclass
class OutOfStock(Event):
    sku: str
