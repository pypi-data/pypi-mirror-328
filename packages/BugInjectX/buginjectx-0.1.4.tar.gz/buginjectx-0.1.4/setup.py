from setuptools import setup, find_packages

# Read README.md as the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="BugInjectX",
    version="0.1.4",  # Increment version to reflect changes
    author="Z3r0 S3c",
    author_email="z3r0s3c@greynodesecurity.com",
    description="Automated vulnerability scanner for SQL Injection (SQLi), SSRF, and XSS.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Make sure this is markdown!
    url="https://github.com/greynodesecurity/BugInjectX",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',  # Change to '5 - Production/Stable' when ready
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    
    install_requires=[
        'requests>=2.28.0',  # Ensures a stable version
        'aiohttp>=3.8.0',  # Async HTTP client for faster requests
        'colorama>=0.4.4',  # Adds color-coded terminal output
        'beautifulsoup4>=4.11.1',  # For parsing and extracting HTML elements
        'tqdm>=4.64.0',  # Progress bar for better UX
        'asyncio',  # Required for asynchronous operations
        'argparse',  # Command-line argument parsing
    ],

    extras_require={
        'dev': ['pytest', 'black', 'flake8'],  # Development tools
    },

    entry_points={
        'console_scripts': [
            'buginjectx=buginjectx.main:run',  # Entry point for command-line execution
        ],
    },

    python_requires='>=3',  # Minimum Python version required
    
    keywords=[
        'security', 'bug bounty', 'pentesting', 'SQLi', 'SSRF', 'XSS', 'infosec',
        'hacking', 'penetration testing', 'web security', 'vulnerability scanning',
        'ethical hacking', 'bug bounty automation', 'cybersecurity',
    ],

    project_urls={
        'Source Code': 'https://github.com/greynodesecurity/BugInjectX',
        'Bug Tracker': 'https://github.com/greynodesecurity/BugInjectX/issues',
        'Documentation': 'https://github.com/greynodesecurity/BugInjectX/wiki',
    },
)
