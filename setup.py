import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Get the required packages
with open('requirements.txt', encoding='utf-8') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="dice_ml",
    version="2.0.1",
    author="ramaravind",
    author_email="raam.arvind93@gmail.com",
    description="Generates Diverse Counterfactual Explanations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/DiCE",
    packages=setuptools.find_packages(), #setuptools.find_packages(), ['dice_ml', 'dice_ml.data_interfaces', 'dice_ml.dice_interfaces', 'dice_ml.model_interfaces', 'dice_ml.utils']
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=install_requires
)