from setuptools import find_packages, setup

PACKAGE_NAME = "export-easy-package"

setup(
    name=PACKAGE_NAME,
    version="0.0.13",
    description="This is Export Easy Tools package",
    packages=find_packages(),
    entry_points={
        "package_tools": ["my_tools = export_easy_package.tools.utils:list_package_tools"],
    },
    include_package_data=True,   # This line tells setuptools to include files from MANIFEST.in
    extras_require={
        "azure": [
            "azure-ai-ml>=1.11.0,<2.0.0"
        ]
    },
)
