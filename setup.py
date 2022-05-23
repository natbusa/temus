from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='identify and demonstrate an opportunity to deploy machine learning to take '
                'a small but practical step towards increasing sustainability and reducing environmental impact.',
    author='Natalino Busa',
    license='MIT',
    install_requires=[
        'numpy==1.21',
        'pandas',
        'patsy',
        'scipy',
        'scikit-learn',
        'lightgbm',
        'catboost',
        'kaggle',
        'shap',
        'statsmodels',
        'pystan==2.19.1.1',
        'prophet',
        'tensorflow',
        'flaml',
        'cloudpickle',
        'pyarrow'
    ]
)
