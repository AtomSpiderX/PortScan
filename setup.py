from setuptools import setup

setup(
    name="port-scanner-vuln-checker",
    version="1.0.0",
    py_modules=["scanner", "utils"],
    install_requires=[
        "requests",
        "colorama"
    ],
    entry_points={
        'console_scripts': [
            'port-scanner=scanner:main'
        ]
    }
)
