# 0x00. AirBnB clone - The console 
:books:  Foundations - Higher-level programming ― AirBnB clone

:couple:Project to be done in teams of 2 people:
###### Abderrahmen Hidoussi, Oumayma Bougossa.

## Welcome to the AirBnB clone project! (The Holberton B&B) :loudspeaker:

### First step: :eyes:  Write a command interpreter to manage your AirBnB objects.

**This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…**
**Each task is linked and will help you to:**
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine.

### What’s a command interpreter :question:

**Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:**
- Create a new object (ex: a new User or a new Place).
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…).
- Update attributes of an object.
- Destroy an object.


## :dart: Learning Objectives 


### General

1. How to create a Python package
2. How to create a command interpreter in Python using the cmd module
3. What is Unit testing and how to implement it in a large project
4. How to serialize and deserialize a Class
5. How to write and read a JSON file
6. How to manage datetime
7. What is an UUID
8. What is *args and how to use it
9. What is **kwargs and how to use it
10. How to handle named arguments in a function


## Requirements


### :snake:  Python Scripts
1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. The first line of all your files should be exactly #!/usr/bin/python3
5. A README.md file, at the root of the folder of the project, is mandatory
6. Your code should use the PEP 8 style (version 1.7 or more)
7. All your files must be executable
8. The length of your files will be tested using wc
9. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
10. All your classes should have a documentation (python3 -c 'print(__import__("my_module").11. MyClass.__doc__)')
12. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
13. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).


## :page_facing_up:      Python Unit Tests

'''
1. Allowed editors: vi, vim, emacs
2. All your files should end with a new line
3. All your test files should be inside a folder tests
4. You have to use the unittest module
5. All your test files should be python files (extension: .py)
6. All your test files and folders should start by test_
5. Your file organization in the tests folder should be the same as your project
6. e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
7. e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
8. All your tests should be executed by using this command: python3 -m unittest discover tests
9. You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
10. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
11. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
12. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
13. We strongly encourage you to work together on test cases, so that you don’t miss any edge case.


## :white_check_mark:     Execution 

***Your shell should work like this in interactive mode:***

```ruby

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

***But also in non-interactive mode: (like the Shell project in C)***

```ruby
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


# :computer:   Tasks

### :large_blue_circle:  0. README, AUTHORS

1. Write a `README.md:`
 - description of the project
    - description of the command interpreter:
    * how to start it
    * how to use it
    * examples
2. You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
3. You should use branches and pull requests on Github - it will help you as team to organize your work.

### Repo:
* GitHub repository: `AirBnB_clone`
* File: `README.md`, `AUTHORS`

### :large_blue_circle: 1. Be PEP8 compliant! 

***Write beautiful code that passes the PEP8 checks.***

### Repo:
* GitHub repository: `AirBnB_clone`

### :large_blue_circle:  2. Unittests  

***All your files, classes, functions must be tested with unit tests***

```ruby
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```
### Repo:

* GitHub repository: `AirBnB_clone`
* File: `tests/`


### :large_blue_circle:  3. BaseModel

1.***Write a class BaseModel that defines all common `attributes/methods` for other classes:***

 - `models/base_model.py`
 - Public instance attributes: 
    * `id`:string - assign with an `uuid` when an instance is created:
        * you can use `uuid.uuid4()` to generate unique `id` but don’t forget to convert to a string
        * the goal is to have unique `id` for each `BaseModel`
    * `created_at`: datetime - assign with the current datetime when an instance is created
    * updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
 - `__str__`: should print:` [<class name>] (<self.id>) <self.__dict__>`
 - Public instance methods:
    * `save(self)`: updates the public instance attribute updated_at with the current datetime
    * `to_dict(self)`: returns a dictionary containing all keys/values of `__dict__ `of the instance:
        * by using `self.__dict__`, only instance attributes set will be returned
        * a key `__class__` must be added to this dictionary with the class name of the object
        * `created_at` and `updated_at` must be converted to string object in `ISO format`:
            * format:` %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)`
            * you can use `isoformat()` of `datetime` object
        * This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our `BaseModel`

```ruby
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'Holberton', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - Holberton
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
```
### Repo :
* GitHub repository: `AirBnB_clone`
* File: `models/base_model.py`, `models/__init__.py`, `tests/`

### :large_blue_circle: 4. Create BaseModel from dictionary
***Previously we created a method to generate a dictionary representation of an instance (method to_dict()).***

***Now it’s time to re-create an instance with this dictionary representation.***
```ruby
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
* Update `models/base_model.py`:

    * __init__(self, *args, **kwargs):
    * you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
    * *args won’t be used
    * if kwargs is not empty:
        * each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
        * each value of this dictionary is the value of this attribute name
        * Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
    * otherwise:
        * create id and created_at as you did previously (new instance).

```ruby
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'Holberton'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'Holberton'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - Holberton
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'Holberton'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$ 
```
### Repo :
* GitHub repository: `AirBnB_clone`
* File: `models/base_model.py`, `tests/`

### :large_blue_circle:  5. Store first object 

***Now we can recreate a BaseModel from another one by using a dictionary representation:***
```ruby
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

**It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.**

*Writing the dictionary representation to a file won’t be relevant:*

    * Python doesn’t know how to convert a string to a dictionary (easily).
    * It’s not human readable.
    * Using this file with another program in Python or other language will be hard.

**So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.**

*Now the flow of serialization-deserialization will be:*

```ruby
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
- Magic right?

- Terms:

* **simple Python data structure**: Dictionaries, arrays, number and string. ```ex: { '12': { 'numbers': [1, 2, 3], 'name': "John" } }```
* **JSON string representation**: String representing a simple data structure in JSON format.``` ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'```

***Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:***

* ``models/engine/file_storage.py``
    * Private class attributes:
        * ``__file_path: string`` - path to the JSON file (ex: file.json)
        * ``__objects: dictionary``- empty but will store all objects by `<class name>.id` (ex: to store a BaseModel object with ``id=12121212``, the key will be ``BaseModel.12121212``)
    * Public instance methods:
        * `all(self)`: returns the dictionary `__objects`
        * `new(self, obj)`: sets in `__objects` the obj with key `<obj class name>.id`
        * `save(self)`: serializes `__objects` to the JSON file `(path: __file_path)`
        * `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
* Update `models/__init__.py`: to create a unique FileStorage instance for your application
    * import file_storage.py
    * create the variable storage, an instance of FileStorage
    * call reload() method on this variable
* Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage
    * import the variable storage
    * in the method save(self):
        * call save(self) method of storage
    * __init__(self, *args, **kwargs):
        * if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage.


````ruby
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'Holberton', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "Holberton", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'Holberton', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'Holberton', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'Holberton', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'Holberton', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'Holberton', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "Holberton", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "Holberton", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "Holberton", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$ 
```


























### :large_blue_circle: 6. Console 0.0.1 

### :large_blue_circle: 7. Console 0.1 
### :large_blue_circle: 8. First User 
### :large_blue_circle: 9. More classes!
### :large_blue_circle: 10. Console 1.0 