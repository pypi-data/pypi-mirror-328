from setuptools import setup, find_packages

setup(
    name='metamodels',
    version='0.1.0',
    description='Библиотека для запуска мета модели на основе предсказаний других моделей.',
    author='Ваше Имя',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    python_requires='>=3.6',
    url='https://github.com/QaqanBagan/metamodels',  # если есть репозиторий
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # или другая лицензия
        'Operating System :: OS Independent',
    ],
)
