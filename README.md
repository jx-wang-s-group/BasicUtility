# BasicUtility
Common utilities (e.g. input parameter reading) for Sci-ML jobs

## Installation
Replase the RELEASE_VERSION with desired version number (e.g. v0.0.1)
```bash
pip install git+https://github.com/jx-wang-s-group/BasicUtility@RELEASE_VERSION
```

## Usage
* `basic_input`: read in the yaml file and returns an object contains all the yaml file entries.
    
    Example: 

    `input.yaml` looks like:

        ```yaml
        data_path: /a/b/c
        params:
          nu: 1.e-3
          mesh_size: [10, 10,]
        ```

    ```python
    >>> hyper_params = basic_input("input.yaml")
    >>> hyper_params.data_path
    >>> '/a/b/c'
    >>> hyper_params.params
    >>> {'nu': 0.001, 'mesh_size': [10, 10]}
    ```
    
    basic_input.update_defaults(): takes in a dictionary to update the default values. Then default values can be omitted in the yaml file.

* `TrainParamReader`: subclass of basic_input, with predefines attributes related to DL training.

* `createFn`:
 Create nested function/class from a dictionary. Work well with `TrainParamReader`/`basic_input`

    Example:
    
    Say, we have a yaml file like this
    ```yaml
    fo:
        name: foo
        kwargs:
            x:
                name: fx
                kwargs:
                    a:
                        name: fa
                        kwargs:
                            alpha: 1
                    b: 2
            y: 3
            z: 4
    ```
    Read in the yaml file and pass to `createFn`
    ```python
    import abc
    dictionary = basic_input("PATH_TO_YAML")
    fo = createFn(dictionary, abc)
    ```
    which is equivalent to 
    ```python
    >>> fo = abc.foo(
    >>>     x = fx( a = fa(alpha = 1), b = 2 ),
    >>>     y = 3,
    >>>     z = 4,
    >>> )
    ```
        


