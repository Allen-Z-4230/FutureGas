# FutureGas
COGS 108 Final Project - Group 40.<br/>
Predicting gas prices from the state of the economy.


## Setup

Make sure you have conda installed by running the following:
```
conda -V
```

Run the following command to setup a new conda environment. Enter [y] where applicable. This may take a while.

```
conda create -n future_gas python=3.6 anaconda
```

Activate your environment with the following:

```
source activate future_gas 
```

Install the required packages once in the conda environment.
```
pip install -r requirements.txt
```

When finished working in the environment, run the following to exit:
```
source deactivate
```

## New Packages
When incorporating new packages into the project using `pip`, first test that the package works as expected in your own local environment. Then, add the package name only to `requirements.txt`.

For example, if I were to run `pip install pytrends` and write code that uses this package, I would need to add `pytrends` to the end of `requirements.txt`.

Skip this step if you are just experimenting with packages and if the main code we are using won't incorporate these packages.


## Run notebooks
Make sure you are running in your conda environments with all of the required packages. Then, run the following command to open up jupyter in your browser.
```
jupyter notebook
```