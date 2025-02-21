from setuptools import setup, find_packages

setup(
    name="cleanflo",  # Package name
    version="0.1.0",  # Initial version
    author="MYNAMPATI SRI RANGANADHA AVIANSH",  # Replace with your name
    author_email="aviinashhreddyy77@gmail.com",  # Replace with your actual email
    description="A beginner-friendly Python package for easy data cleaning and preprocessing.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cleanflo",  # Replace with your actual GitHub repo link
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "nltk"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="data cleaning, preprocessing, data science, machine learning",
    python_requires=">=3.7",
    include_package_data=True,
)
