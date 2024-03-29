import io
import os
from typing import Dict, List

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_requirements(filename: str) -> List[str]:
    with io.open(
        os.path.join(HERE, "requirements", filename), "rt", encoding="utf-8"
    ) as f:
        return [line.strip() for line in f if is_requirement(line)]


def load_readme() -> str:
    with io.open(os.path.join(HERE, "README.md"), "rt", encoding="utf8") as f:
        readme = f.read()
    # Replace img src for publication on pypi
    return readme.replace(
        "./docs/img/",
        "https://github.com/codewithemad/django-num2fa/raw/master/docs/img/",
    )


def is_requirement(line: str) -> bool:
    return not (line.strip() == "" or line.startswith("#"))


def load_about() -> Dict[str, str]:
    about: Dict[str, str] = {}
    with io.open(
        os.path.join(HERE, "django_num2fa", "__about__.py"), "rt", encoding="utf-8"
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()

setup(
    name="django-num2fa",
    version=ABOUT["__version__"],
    project_urls={
        "Code": "https://github.com/codewithemad/django-num2fa",
        "Issue tracker": "https://github.com/codewithemad/django-num2fa/issues",
    },
    license="AGPLv3",
    author="Emad Rad",
    author_email="codewithemad@gmail.com",
    description="A Django app with filters to convert numbers"
    "into Persian numbers or words.",
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests*"]),
    test_suite="tests",
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=load_requirements("base.txt"),
    extras_require={
        "dev": load_requirements("dev.txt"),
    },
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
