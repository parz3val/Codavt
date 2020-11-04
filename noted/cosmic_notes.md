# Notes from cosmic python

- Written by Bob, Ian Cooper, and Harry JW. Percival

- Mainly an intro to the DDD (Domain Driven Design)

- Other books to take a look:

    a. TDD with Python: Harry JW. Percival  `http://www.obeythetestinggoat.com/`

    b. DDD : Eric Evans 

    c. Patterns of Enterprise Application 
    Architecture: Martin Fowler
    d. Fowler's refactorning : Martin Fowler


- The book provides notes on managing complexity of a business domain application. In general we use,:
    1. **TDD** : TDD is RGR (Red Green Refactor) methodology where we can write test to cover the functionalities of our application without fear of regression.
    
    2. **DDD** : DDD is a strategy of focusing on building model of our core business logic.

    3. **Loosely occupied services integrated via messages** or reactive microservices: Is an established way of managing complexity and infrastructure across variety of applications. Isn't that much clear as a lot of python projects are built as monoliths. 

- Map
    
    a. Domain modeling and DDD 

    b. Event-driven architecture

    c. Epilogue

- Code examples

    - Branch history:`https://github.com/cosmicpython/code/branches/all`

- Building DDD support arch/ Design Patterns
    - The Repository Pattern - ps abastraction
    - Service layer patteern - separates use cases from logic
    - Unit of work pattern - for atomic ops
    - The aggregate pattern - enforce integrity of our data

- Create UML from text desc: `https://plantuml.com/`


## Part 1: Domain models

- Domain: The domain is a fancy way of saying the problem you’re trying to solve.

- Model : A model is a map of a process or phenomenon that captures a useful property.

- The domain model is the mental map that business owners have of their businesses. 

- Hence domain modelling is solving problems by capturing the requirement and specifications from the class attributes of the system.

- Jargon arises naturally among people who are collaborating on complex systems. 

- **This Is Not a DDD Book. You Should Read a DDD Book.**

    - Implementing Domain-Driven Design by Vaughn Vernon (`red book`)

    - DDD by Eric Evans (`blue book`)

- DDD has inspired many arch patterns like Entity, Value Object, Aggregate and Repository

- DDD >> "the most important thing about software is that it provides useful model of our problem"

- The terminology used by business stakeholders represents a distilled understanding of the domain model, where complex ideas and processes are boiled down to a single word or phrase. When we hear our business stakeholders using unfamiliar words, or using terms in a specific way, we should listen to understand the deeper meaning and encode their hard-won experience into our software.


### The domain language

- intro : set of symbols and terminologies in the domain to accurately describe the problem or problem set. Contains set of data definitions for the model, all of the definitions are trivial however and only hold the ground in the domain.

- creating notes for the models in terms of domain is helpful to make models that are clear and easily understood.

- Typing hints:
    - Typing hints are important because they help us to understand our models better.
    - We can use `Pydantic` or `typing` library from python to get the definition and hinting of our primitives.
    - We can also define our own types with typing module and take things too far.

- taking it too far: Here we define new types for our data.

```python
from dataclasses import dataclass
from typing import NewType

Quantity = NewType("Quantity", int)
Sku = NewType("Sku", str)
Reference = NewType("Reference", str)
...

class Batch:
    def __init__(self, ref: Reference, sku: Sku, qty: Quantity):
        self.sku = sku
        self.reference = ref
        self._purchased_quantity = qty
```

- **DataClasses** 
    - the data classes are very primitive class definitions, similar to structs in C and C++, and they are virtually same as namedtuples.
    - data classes are useful to represent entities which have data but no unique references.
    - data classes are used to hold value objects
    - value objects are domain obects with unique data identifty. We make them immutable.
    - **don't forget difference between Value objects and entites and where to best use them**

- Domain Service Function: Not everything has to be an object
    - We can use magic methods from python to turn our value objects into functions/methods
    - stuff that takes in data, does something to it, and returns them sounds like a function and is represented well.
    - Few important magic methods for implementing the domain service function
        - `__gt__` 
        - `__hash__` 
        >> For value objects, the hash should be based on all the value attributes, and we should ensure that the objects are immutable. We get this for free by specifying @frozen=True on the dataclass.
        - `__eq__` 
        - datamodel methods docs: `https://docs.python.org/3/reference/datamodel.html#object.__eq__` 

        - types ref : `https://docs.python.org/3/library/stdtypes.html#frozenset` 



>> "Sometime it just isn't thing" -- Eric Evans

```
Evans discusses the idea of Domain Service operations that 
don’t have a natural home in an entity or value object.
A thing that allocates an order line, given a set of batches, 
sounds a lot like a function, and we can take advantage 
of the fact that Python is a multiparadigm language and just 
make it a function.
```


- Exceptions Can Express Domain Concepts Too
    - for instance : for a tasklist app, exceptions like taskalreadyset or tasknot found, can represent domain concepts.


### Summary

**Domain Modelling** 

part of code that is closet to business, is most likely to change and delivers the value to business. *make it easy to understand and modify*

**Differentiate entities from value objects** 

best represented as immutable objects, value objects are defined by its attributes. If you change an attribute on VO its a different object. having a separation of entities and value objects goes long way towards better models.

**Not everything has to be an object**

Because python is a multiparadigm language, it implement `verbs` as the `functions` in our models. For every FooManager, BarBuilder, or BazFactory, there’s often a more expressive and readable manage_foo(), build_bar(), or get_baz() waiting to happen.

**Do better OOP**

modelling is where you show off your oop skills, revisit SOLID principles and other good heuristics.

**Think about consistency boundaries and aggregates**


## Repository Pattern

- an abstraction over persistent storage, hides complexities of database and makes it easier to test.

- in this model, we build a `repository` object which sits between our domain model and storage solutions.

- why need this
    - we need to have persistence for our models
    - we want to hide the data layer logic

- we can use any architecture we like like `onion`, `clean` or any as long as they provide the separation between our domain models and the db access logic.

- in fact, we want our models to be independent and unaware of where the data  dumps to and loads from.

- we can use ORM to achieve this goal, but we need to make sure that there aren't unnecessary complexities and dependencies with the ORM library, ORMs bridge the gap between the world of logic, models and objects to that of pure algebric relations that we need for our dbs.
    - e.g. 
    
```python
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Order(Base):
    id = Column(Integer, primary_key=True)

class OrderLine(Base):
    id = Column(Integer, primary_key=True)
    sku = Column(String(250))
    qty = Integer(String(250))
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship(Order)

class Allocation(Base):
    ...
```
- in the above example, we are using the `SQLalchemy` ORM library but all of our models are coupled with the columns of our db, so its not independent of the db layer or the complexity that comes with it.

- DIP : Dependency Inversion Principle
    - Robert C Martin
    - One of the foundations of solid principles
    - High level modules shouldn't depend on low level modules
    - abstractions shouldn't depened on details, details should depend on abstractions

- Code that violates DIP:
```python
class Book:
    def __init__(self, content: str):
        self.content = content

class Formatter:
    def format(self, book: Book) -> str:
        return book.content

class Printer:
    def print(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        ... 
        # Printing the book
```
Here the models like printer and formatter are dependent on the book and hence can't be used with other books.
They have concretions instead of abstractions.

- We can use `Protocols: ` to write DIP code. The above code with proper DIP and dataclass decorators would be.
    - `https://mypy.readthedocs.io/en/stable/protocols.html#simple-user-defined-protocols`

```python
# Protocol for the book
@dataclass
class HasContentProtocol(Protocol):
    content: str

@dataclass
class Book(HasContentProtocol):
    def __init__(self, content):
        self.content = content

@dataclass
class FormatterProtocol(Protocol):
    def format(self, has_content: HasContentProtocol):
        ...

# Protocol for the Formatter
class A4Formatter(FormatterProtocol):
    def format(self, has_content: HasContentProtocol):
        return has_content.content # This should obviously contain logic to format

# Now we inject protocols into the printer class
class Printer:
    def __init__(self, formatter: FormatterProtocol):
        self.formatter = formatter

    def print(self, has_content: HasContentProtocol):
        formatted_book = self.formatter.format(has_content)

# Printing the book
book = Book("Amazing book content") # Book is a concretion of HasContentProtocol

formatter = A4Formatter()
printer = Printer(formatter)
```

- **Dependency Injection**
    - dependency injection is design pattern used to implement the IoC(inversion of control), here dependencies are handled by creating dependent objects outside the class and injecting them back into class for the functionality

    -  DI involves three different types of classes 
        - Client class : the class(dependent class) on which the dependencies arise from
        - Service class : service class (dependency) is the class which provides service to client class.
        - Injection class : injector class to inject service class object into client class
    
    - Types of DI
        - constructor injection
        - property injection
        - method injection

- **Inverting the dependencies: ORM depends on the model**
In the SQL alchemy code example above, our models are coupled with the ORM dependencies. We can either use dependency injection to achieve DIP and get our core models and db logic loosely coupled.

```python
from sqlalchemy.orm import mapper, relationship

import model  #(1)


metadata = MetaData()

order_lines = Table(  #(2)
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255)),
)

...

def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)  #(3)  
```
1. The ORM imports (or "depends on" or "knows about") the domain model, and not the other way around.

2. We define our database tables and columns by using SQLAlchemy’s abstractions.

3. When we call the mapper function, SQLAlchemy does its magic to bind our domain model classes to the various tables we’ve defined.

- The other benefit of using ORM like this is that we can write tests with good coverage. But we won't keep such tests as it only aims to guide in developing repo pattern, which is the one we want to test against and is easy to do.


**The Repository Pattern**
The repo pattern is abstraction over persistent storage. To a pythonista, it might just mean a python object with `.get` and `.add` methods available to it. It hides all the details of implementation by pretending all of our data is in memory.

- Duck Typing - Dynamic typing in python with just implicit typing.

**"If it looks like a duck and quacks like a duck. Then it might be a duck."**

**"If it looks like a duck and quacks like a duck, but requires batteries. Then maybe something is wrong in your abstraction."**

- Static duck typing - duck typing with some type hints but no type checks or validations.

- Trade off of repo model
>> You know they say economists know the price of everything and the value of nothing? Well, programmers know the benefits of everything and the trade-offs of nothing.

-- Ryan Hickey 

- **Port and Adapter in Python**

    - Port: port is the interface between our application and whatever we want to abstract away

    - Adapter: Is the implementation of the port behind that interface or abstraction


## Summary and Takeaways

1. **Apply Dependency Inversion to your ORM**

2. **The repo pattern is simple abstraction around persistent storage.**

3. **Local complexity and coupling good. Global one is a nuissance**

### Take aways

1. I suppose we mean "no stateful dependencies." Depending on a helper library is fine; depending on an ORM or a web framework is not.

2. Mark Seemann has an excellent blog post on the topic.

3. In this sense, using an ORM is already an example of the DIP. Instead of depending on hardcoded SQL, we depend on an abstraction, the ORM. But that’s not enough for us—not in this book!

4. Even in projects where we don’t use an ORM, we often use SQLAlchemy alongside Alembic to declaratively create schemas in Python and to manage migrations, connections, and sessions.

5. Shout-out to the amazingly helpful SQLAlchemy maintainers, and to Mike Bayer in particular.
6. You may be thinking, "What about list or delete or update?" However, in an ideal world, we modify our model objects one at a time, and delete is usually handled as a soft-delete—i.e., batch.cancel(). Finally, update is taken care of by the Unit of Work pattern, as you’ll see in.

7. To really reap the benefits of ABCs (such as they may be), be running helpers like pylint and mypy.


## Abstraction and clean code

- Abstraction is a process of hiding away the messy details or just giving names to stuff.

- Almost every term we use irl is an abstraction over something inherently complex and messy

- for example, lets take a term `human`. It hides away all the complexity that makes up human in both physical and psychological way, and presents a clear representation of the object.

- abstraction in programming is giving reference to objects, to hide the details of implementation so that we can reuse them more easily, or test with better coverage.

>>  vocabulary of Gerard Meszaros's book

- **Test Double** - Any pretend object that is just used in testing as a replacement to the real object for various reasons. Mesazaros's doubles are: - 
    - **Dummy** - Dummy's are objects that are created and just around, but not actually used. They are just used to fill the parameter lists and stuff.
    - **Fake** - These are striped down versions of real objects and have working implementations of the real objects. But using shortcuts in implementation for the tests makes them unsuitable for production. (for instance: In memory database)
    - **Mocks** - Mocks are the objects that are preprogrammed with the expectations of the calls they are to receive and answers the formulate.
    -  **Stubs** - Stubs provide canned answers to calls made during the test, and don't respond to anything outside of their prorgamming bound
    - **Spies** - Spies are the stubs that record some information on how they are called. (For instance: an email service that records how many emails were sent)

- **"Tell Don't Ask"** principle, which encourages you to tell an object to do something rather than rip data out of an object to do it in client code.

- work at the highest level of abstraction possible rather than doing checks on the behavior of intermediary collaborators

### Relationship between TDD and DDD**

TDD comes from the tradition of xP out of Detroit School and focuse on behavior and state design through iteration of tests. (Think of RGR cycle). The TDD community follows the mockists and classicist ideologies in testing, where you test for behavior with mocks and with/without doubles respectively. The idea of TDD is to have a better coverage for the SUT and iterate.

But in DDD, we use TDD as a design inspiration and testing practice/inspiration as second. Object testing with fakes is at the heart of TDD because we want to test for both the state and behavior of the SUT, rather than writing small coverage tests for intermediary collaborators.



## Further reading:
    - `https://refactoring.com/` - Guide to refactoring and design by Martin Fowler

    - `https://martinfowler.com/architecture/` - Guide about the architecture of 
    the enterprise apps.

    - Mocks aren't stubs- `https://martinfowler.com/articles/mocksArentStubs.`htmlGuide on testing with mocks and stubs.

    - Behavior Driven Development (BDD) : `https://dannorth.net/introducing-bdd/`


