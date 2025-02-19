from setuptools import setup, find_packages

setup(
    name='pytoke',
    version='0.1.1',
    author='Ada Zhang, Nihal Karim, Hamza Louzan, Victor Wei',
    author_email='abz200026@gmail.com, karimnihal@gmail.com, hamzalouzan5@gmail.com, victorwei0916@gmail.com',
    description='A library for calculating fertility and parity scores with visualizations using tokenizers.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/karimnihal/pytoke',
    packages=find_packages(),  # Automatically finds the package in the pytoke folder
    license='MIT',
    license_files=['LICENSE'],
    install_requires=[
        'transformers',
        'pandas',
        'matplotlib',
        'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.9',
)
