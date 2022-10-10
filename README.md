# 0x00. AirBnB clone - The console

This is the first step towards building our first full web application: the AirBnB clone.

We put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
We created a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
We created all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
We created the first abstracted storage engine of the project: File storage using JSON.
We created unittests to validate our classes and storage enginedescription of the command interpreter.

To start and use:
```
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
Non-interactive mode:
```
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
