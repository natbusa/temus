Temus
==============================

Author: Natalino Busa

Assignment:
We would like you to identify and demonstrate an opportunity to deploy machine learning to take
a small but practical step towards increasing sustainability and reducing environmental impact.
You should focus on both on the development of a model and the way in which it will be deployed to deliver
measurable environmental or sustainable outcomes. You should adopt a balanced approach considering any factors
which you believe to be important in supporting real-world deployments of machine learning.
You may develop your model using the data sets listed below, or any other data sets which are publicly accessible,
and may provide you the opportunity to demonstrate your skills to deliver against the environmental and sustainability
goals.

- Global Energy Forecasting Competition 2012  
https://www.kaggle.com/competitions/GEF2012-wind-forecasting
https://www.kaggle.com/competitions/global-energy-forecasting-competition-2012-load-forecasting
  

- AMS 2013-2014 Solar Energy Prediction Contest  
https://www.kaggle.com/competitions/ams-2014-solar-energy-prediction-contest
  

- World Sustainability Dataset  
https://www.kaggle.com/datasets/truecue/worldsustainabilitydataset

## Deliverables
 
 - presentation: https://github.com/natbusa/temus/blob/main/reports/Temus%20case%20study.pdf
 - notebook: https://github.com/natbusa/temus/blob/main/notebooks/temus.ipynb
 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │  └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

```
>$ make
Available rules:

clean               Delete all compiled Python files 
create_environment  Set up python interpreter environment 
data                Make Dataset 
lint                Lint using flake8 
requirements        Install Python Dependencies 
sync_data_from_s3   Download Data from S3 
sync_data_to_s3     Upload Data to S3 
test_environment    Test python environment is setup correctly 
```

--------
Install procedure and requirements:

 1. make sure that conda is installed on the system
 2. run `make create_environment` to create the conda env for this project 
 3. download the raw data in `data/raw`
    
--------
Data:

either manual download from:  
https://www.kaggle.com/c/santander-customer-transaction-prediction/data

or using the kaggle API:   
`cd data/raw && kaggle competitions download -c santander-customer-transaction-prediction`

--------
Quick start for inspect/work on notebooks:
```
make data && jupyter lab
```

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
# temus
