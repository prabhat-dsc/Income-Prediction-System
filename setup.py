from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requriments(filepath: str)->List:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ i.replace("\n", "") for i in requirements]
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

setup(name='Income-Prediction-System',
     version='1.0.0',
     description= " ML Income Prdiction System",
     author="Prabhat Kumar",
     author_email="prabhat.dsc48@gmail.com",
     url= "https://github.com/prabhat-dsc/Income-Prediction-System.git",
     packages= find_packages(),
     install_requires=get_requriments("requirements.txt")
     )
     
