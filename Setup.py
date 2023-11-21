##Need of Setup.py file -->building our application as package itself, so it will be used in any enviroment
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirement(file_path:str)-> List[str]:
    '''
    this will return the function the list of requirement
    '''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", " ") for req  in requirements]  
        ##while reading 'Requirement.txt' it will take \n while reading next line for replacing \n we have to take blank space
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Tejas_Patil',
    author_email='tejaspatil0807@gmail.com',
    packages= find_packages(),
    install_requires = get_requirement('Requirement.txt')

    ##create folder src--source 
    ##if you want to found source(src) as package --> we will create one more file in src folder
    # __init__.py --> whenever the setup.py the find_packages is running in how many folder you have '__init__.py'
    # it will consider 'src ' as package itself.
    
)


#Notes ---> In 'get_requirement' while we are reading ''-e.y'' also come and probably in 'get_requirement' while installing packages in the form of list ''-e.''
#   also come , it need to be eliminated if we get that value it will connect to setup.py file (it should not come whille runing the code)