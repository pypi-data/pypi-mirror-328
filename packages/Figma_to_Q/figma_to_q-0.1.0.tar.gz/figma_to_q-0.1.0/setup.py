from setuptools import setup, find_packages

setup(
    name='Figma_to_Q',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fig2q=fig2q.cli:main',
        ],
    },
    author='Jonas Oesch',
    author_email='jonas.oesch@nzz.ch',
    description='A CLI-Tool to publish Figma designs to Q',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
