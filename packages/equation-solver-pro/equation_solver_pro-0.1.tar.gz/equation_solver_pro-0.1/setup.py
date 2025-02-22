from setuptools import setup, find_packages

setup(
    name="equation_solver_pro",  
    version="0.1",           
    packages=find_packages(),
    install_requires=[         
    ],
    description="This Python script is designed to solve simple linear equations with one unknown variable (denoted as `x`). The equation can involve addition, subtraction, multiplication, or division. The script handles equations in various formats, such as `x + a = b`, `a - x = b`, `x * a = b`, and others, and calculates the value of `x` accordingly.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Tabib",
    author_email="pytabib@gmail.com",
    url="https://github.com/pyTabib/Equation_Solver_pro",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
