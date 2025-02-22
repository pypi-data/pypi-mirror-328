from setuptools import setup 

setup(
    name='chatbotai-gui',
    version='1.0.1b1',
    packages=['chatai'],
    license='AGPL-3.0-or-later',
    description='A chatbot GUI that uses OpenAI, MetaAI, and Google Generative AI.',
    # Metadata
    author='ProgMEM-CC',

    # Required dependencies
    install_requires=[
        'openai',
        'google.generativeai',
        'meta_ai_api'
    ],

    # Optional dependencies
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'coverage',
            'flake8',
            'black',
            'isort'
        ]
    },
    include_package_data=True,  # Ensures extra files like LICENSE are included
    license_files=[]
)