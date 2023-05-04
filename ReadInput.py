import yaml

def read_yaml(filename:str) -> dict:
    
    '''Reads a yaml file and returns a dictionary
    ----------    
    Parameters
    * filename: str; the path to the yaml file


    Returns
    * dict; the dictionary containing the yaml entries
    '''

    with open(filename, 'r') as f:
        return yaml.safe_load(f)



class basic_input(object):
    def __init__(self, input_file:str):
        '''
        Load a yaml file and store the entries as attributes of the class
        
        Parameters
        ----------
        * input_file: str; the path to the yaml file
        '''
        self.yamlpath = input_file

        yaml_dict = read_yaml(input_file)
        
        for key in yaml_dict:
            setattr(self, key, yaml_dict[key])


    def __use_default_warning(self, key:str, default_value):
        if hasattr(self, key):
            pass
        else:
            setattr(self, key, default_value)
            print(f'Using default value for {key}: {default_value}')

            
class TrainParamReader(basic_input):
    def __init__(self, input_file:str):
        '''
        Load a yaml file and store the entries as attributes of the class
        
        Parameters
        ----------
        * input_file: str; the path to the yaml file
        '''
        super().__init__(input_file)

        default_values = {
            'lr': 1e-3,
            'epochs': 1000,
            'randomSeed': 42,
            'batchSize': 32,
            'savepath': 'results',
            'optimizer': 'adam',
            'schedulerParams':{
                'factor':0.5, 
                'patience':20, 
                'cooldown':20, 
                'minLr':1e-5
            }
        }
        
        self.lr:float
        self.epochs:int
        self.randomSeed:int
        self.savePath:str
        self.schedulerParams:dict
        self.optimizer:str
        self.batchSize:int
        self.dataPath:str
        

        for key in default_values:
            self.__use_default_warning(key, default_values[key])
