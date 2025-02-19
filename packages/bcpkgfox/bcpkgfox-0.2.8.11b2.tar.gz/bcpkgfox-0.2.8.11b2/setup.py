from setuptools import setup, find_packages

setup(
    name="bcpkgfox",
    version="0.2.8.11b2",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'bcpkgfox': ['bin/IEDriverServer.exe'],
    },
    author="Guilherme Neri",
    author_email="guilherme.neri@bcfox.com.br",
    description="Biblioteca BCFOX",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/robotsbcfox/PacotePythonBCFOX",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'selenium',
        'undetected-chromedriver',
        'selenium-stealth',
        'requests',
        'pyautogui',
        'setuptools',
        'opencv-python',
        'pyscreeze',
        'Pillow'
    ],
)