from setuptools import setup, find_packages

install_requires = [
    "click>=8.1.7",
    "colorama>=0.4.6"
]

setup(
    name="DailyTasks",
    version="0.1.0",
    description="A tasks manager for those who like work from shell.",
    author="LuisanaMT",
    author_email="luisanamartineztorres25@gmail.com",
    license="Apache-2.0",
    classifiers=["CLI"],
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.11",
    entry_points={
        'console_scripts': [
            'dailytasks = daily_tasks.commands.main:daily_tasks',
        ],
    },
)
