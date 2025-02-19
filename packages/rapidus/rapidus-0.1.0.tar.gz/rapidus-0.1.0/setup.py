from setuptools import setup, find_packages
import pathlib

# Путь к текущей директории
here = pathlib.Path(__file__).parent.resolve()

# Читаем README.md для long_description
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='rapidus',  # Имя вашего пакета
    version='0.1.0',    # Версия пакета
    description='A short description of your package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Evgenii Gerasin',
    author_email='e.d.gerasin@yandex.ru',
    url='https://github.com/EvgeniiGerasin/rapidus-api-test-framework',  # URL репозитория (если есть)
    packages=find_packages(),  # Автоматически находит все пакеты
    install_requires=[         # Зависимости вашего пакета
        'allure-pytest>=2.13.5',
        'requests>=2.32.3',
        'pytest>=8.3.4'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Тип лицензии
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',  # Минимальная версия Python
    project_urls={  # Дополнительные ссылки
        "Bug Reports": "https://github.com/EvgeniiGerasin/rapidus-api-test-framework/issues",
        "Source": "https://github.com/EvgeniiGerasin/rapidus-api-test-framework",
    },
)
