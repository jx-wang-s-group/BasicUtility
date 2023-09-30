import yaml


def read_yaml(filename: str) -> dict:
    """Reads a yaml file and returns a dictionary
    ----------
    Parameters
    * filename: str; the path to the yaml file


    Returns
    * dict; the dictionary containing the yaml entries
    """

    with open(filename, "r") as f:
        return yaml.safe_load(f)


class basic_input(object):
    def __init__(self, input_file: str):
        """
        Load a yaml file and store the entries as attributes of the class

        Parameters
        ----------
        * input_file: str; the path to the yaml file
        """
        self.yamlpath = input_file

        yaml_dict = read_yaml(input_file)

        for key in yaml_dict:
            setattr(self, key, yaml_dict[key])

    def _use_default_warning(self, key: str, default_value):
        if hasattr(self, key):
            pass
        else:
            setattr(self, key, default_value)
            print(f"Using default value for {key}: {default_value}")


class TrainParamReader(basic_input):
    def __init__(self, input_file: str):
        """
        Load a yaml file and store the entries as attributes of the class

        Parameters
        ----------
        * input_file: str; the path to the yaml file
        """
        super().__init__(input_file)

        default_values = {
            "lr": 1e-3,
            "epochs": 1000,
            "randomSeed": 42,
            "batchSize": 32,
            "savePath": "results",
            "optimizer": "adam",
            "schedulerParams": {
                "factor": 0.5,
                "patience": 20,
                "cooldown": 20,
                "minLr": 1e-5,
            },
        }

        self.lr: float
        self.epochs: int
        self.randomSeed: int
        self.savePath: str
        self.schedulerParams: dict
        self.optimizer: str
        self.batchSize: int
        self.dataPath: str

        for key in default_values:
            self._use_default_warning(key, default_values[key])
        print("")


def createFn(fnName, pkgName: str):
    """
    Create nested function/class from a dictionary
    example:
        to create function/class `foo` from package which has the API: `foo(x, y, z)`
        where `x` is a function/class, which has the API: `fx(a, b)`,
            where `a` is a function/class, which has the API: `fa(alpha)`,
                where `alpha` is a regular parameter
        `y` and `z` are regular parameters (the parameters which don't have input)

        the yaml file should be like this:

        foo:
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

        assume all the functions are from same package/module
    """

    if isinstance(fnName, dict):
        if "kwargs" in fnName:
            for k in fnName["kwargs"]:
                if isinstance(fnName["kwargs"][k], dict):
                    fnName["kwargs"][k] = createFn(fnName["kwargs"][k])
            v = getattr(pkgName, fnName["name"])(**fnName["kwargs"])
        else:
            v = getattr(pkgName, fnName["name"])
    else:
        v = getattr(pkgName, fnName)
    return v
