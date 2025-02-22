from setuptools import setup, find_packages

# README.md içeriğini güvenli bir şekilde oku
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="DHdlk",
    version="0.1.10",
    packages=find_packages(),  # Proje kök dizinindeki modülleri bulur
    package_data={
        "": ["pyarmor_runtime/*.so", "pyarmor_runtime/*.dll", "pyarmor_runtime/*.dylib"],  # PyArmor runtime dosyaları
    },
    author="sahin",
    description="Algebra library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
