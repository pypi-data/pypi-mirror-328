from setuptools import setup, find_packages
from setuptools import  find_namespace_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='raipred',
    version='1.1',
    description='A tool to predict rheumatoid arthritis inducing peptides',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_files = ('LICENSE.txt',),
    url='https://github.com/raghavagps/raipred', 
    packages=find_namespace_packages(where="src"),
    package_dir={'':'src'},
    package_data={
        "raipred.Model": ["*"],  # Include everything in Model/
        "raipred.Data": ["*.csv", "*.txt"],  # Include specific file types in Data/
        "raipred.motifs": ["*.txt"],  # Include JSON and TXT files in Resources/
    },
    entry_points={ 'console_scripts' : ['raipred = raipred.Python_scripts.raipred:main']},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'pandas', 'xgboost == 1.3.3', 'scikit-learn == 1.0.1'# Add any Python dependencies here
    ]
)
