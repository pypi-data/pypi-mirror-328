from setuptools import setup, find_packages

setup(
    name="flask_ignite",
    version="0.1.4",
    description="A simple Flask app creator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nahom D",
    author_email="nahom@nahom.eu.org",
    url="https://github.com/nahom-d54/flask_admin",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask", "flask-sqlalchemy", "flask-migrate", "python-dotenv"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "flask-ignite=flask_admin.setup_flask_project:main",
        ],
    },
)
