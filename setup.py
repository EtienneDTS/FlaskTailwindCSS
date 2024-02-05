from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='flask-tailwindcss',
    version='0.4',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'flask-tailwindcss=flask_tailwindcss.main:start',
        ],
    },
    author='Etienne DTS',
    description='Integrate TailwindCSS in one command.',
    license='MIT',
    long_description=description,
    long_description_content_type="text/markdown"
)