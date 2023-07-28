##### Difference between module and package
Both modules and package organize the structure of the code.
Both of them have different functions and class that can be used by the user.
It is made mainly to support code reusability and modularity of the python code.

The main difference between the module and package is that a module is a single file,
whereas a package is a collection of modules organized in a directory hierarchy

The module is a single Python file that can be imported into another module. In contrast, a package is a collection of modules organized into a directory hierarchy.
A package can have multiple sub-packages and modules, and each module and sub-package has its own namespace, whereas when modules are imported, their content is placed inside a namespace.
The module is initialized when first imported into a program, whereas the package is initialized when one of its modules is imported.
A package is installed using the import keyword followed by the package name, and you can access the module and sub-packages within the package name using dot notation. In contrast, the module can be directly installed using the import keyword followed by the module name

##### Example
This is how a sample module directorly looks like.
    package  
        
        
        sub_package_1
            
            
            --->__init__.py
            
            
            --->module_one.py
            
            
            --->module_two.py
            
            
            --->module_three.py
        
        
        sub_package_2
            
            
            --->__init__.py
            
            --->module_a.py
            
            --->module_b.py
            
            --->module_c.py

