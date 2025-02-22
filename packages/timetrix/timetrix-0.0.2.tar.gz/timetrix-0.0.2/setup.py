from setuptools import setup,find_packages

setup(
    name="timetrix",
    version="0.0.2",
    author="Maglovski Nenad",
    description="Lightweight and intuitive Python library designed to help developers,track, measure, and visualize time with ease.",
    description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["datetime"],
    keywords=['python','time','measure','track'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)