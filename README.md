# PyPass Password Manager
----------------------------------

<img width="481" alt="Screenshot 2019-08-16 at 14 35 31" src="https://user-images.githubusercontent.com/23168398/63168108-83496080-c033-11e9-8111-2fc94b34e52e.png">

<img width="801" alt="Screenshot 2019-08-16 at 14 37 53" src="https://user-images.githubusercontent.com/23168398/63168186-bf7cc100-c033-11e9-97be-766b3c8bb41a.png">



This application has been written in Python3 with tkinter GUI library for educational purposes

Inital Password for opening main windows is "bob"


To run Pypass you need Python3 to be installed and 3 libraries

1. [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)
2. [sys](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys)
3. [getpass](https://docs.python.org/3/library/getpass.html?highlight=getpass#module-getpass)



There are 3 main components:

1. PyPass.py - application itself with all functionality
2. backend_functions.py - Functions for interacting with backend (bakend uses SQLLite3)
3. storage.db - SQLLite3 database where all the values are stored



Usage:

Clone the repo and run PyPass.py

```
git clone https://github.com/asukiasyan/PyPass.git
cd pypass
[python|python3] Pypass.py

```




TODO:

1. Fix destroy of mainwindow when master password hits limit of 5 attempts
2. Implement show/hide fuctionality for password fiels
