from setuptools import setup, find_packages

setup(
    name="EZ_Manage_Tool",
    version="1.0",
    packages=find_packages(),   # make sure init.py present inside package
    include_package_data=True,
    package_data={
        "ez_manage_tool": ["sources/*"],  # ✅ Include specific file types
    },
    install_requires=[
        "PySide6==6.7.1",
        "PySide6_Addons==6.7.1",
        "PySide6_Essentials==6.7.1",
        "shiboken6==6.7.1"
    ],
    entry_points={
        "console_scripts": [
            "ez_manage_ui = ez_manage_tool:initUI"
        ],
    }
)