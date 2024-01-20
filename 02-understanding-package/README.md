# \_\_init__.py
- The \_\_init__.py is a special file in every package.
- It helps interpreter recognize this folder as package.
- It also specifies the resources to be imported from this module.
- An empty \_\_init__.py allows to import all the functions of the module.


# Restricting function to be imported
- Here we're allowing only gfg and sum to be imported from module1 and module2
````
from .module1 import gfg
from .module2 import sum
````