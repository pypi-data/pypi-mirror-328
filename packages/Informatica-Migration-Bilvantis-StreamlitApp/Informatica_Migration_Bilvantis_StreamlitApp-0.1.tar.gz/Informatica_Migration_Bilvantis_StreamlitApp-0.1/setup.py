from setuptools import setup, find_packages

setup(
    name="Informatica_Migration_Bilvantis_StreamlitApp",
    version="0.1",
    author="Rajesh Patil",
    author_email="rajesh@bilvantis.io",
    description="A Streamlit app to convert Informatica mapping XML to SQL queries.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/RajeshPatilBilvantis/setup_git_package_demo.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyvis==0.3.2',
        'PyYAML==6.0.2',
        'streamlit==1.41.1',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'informatica_migration_app = streamlit_app.launcher:run_streamlit',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
