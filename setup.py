from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk~=0.11",
    "cached_property==1.5.2",
    "facebook_business==16.0.0",
    "pendulum>=2,<3",
]

TEST_REQUIREMENTS = [
    "pytest~=6.1",
    "pytest-mock~=3.6",
    "requests_mock~=1.8",
]

setup(
    name="source_waba_analytics",
    description="Source implementation for WhatsApp Business Analytics API.",
    author="Lucas Zanotelli",
    author_email="lucas@zanotelli.dev",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
