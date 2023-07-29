from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n",'') for i in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements



setup(
    name = 'Wafer_fault_dectection',
    version = '0.0.1',
    author = 'Zaib',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)