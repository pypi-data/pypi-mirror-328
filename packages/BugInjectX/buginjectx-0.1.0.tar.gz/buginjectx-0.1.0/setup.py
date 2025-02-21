from setuptools import setup, find_packages

# Read the contents of your README file to use as the long description
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='BugInjectX',  # Name of the package
    version='0.1.0',  # Version of the package
    author='Your Name',  # Your name
    author_email='youremail@example.com',  # Your email address
    description='A tool for discovering SQLi, SSRF, and XSS vulnerabilities using dictionary-based attacks.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/BugInjectX',  # Your GitHub repo URL
    packages=find_packages(),  # Automatically finds all packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests',  # Any dependencies your tool needs (e.g., requests, aiohttp, etc.)
        'aiohttp',  # if you are using asyncio
        'colorama',  # for colored output
    ],
    entry_points={
        'console_scripts': [
            'buginjectx=main:run',  # 'buginjectx' will call the run method from main.py
        ],
    },
    python_requires='>=3.6',  # The minimum Python version required
)
