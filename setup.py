from setuptools import setup, find_packages

setup(
    name="dns-ip-updater",
    version="0.1.0",
    description="A script to update IONOS DNS records to match the current public IP address.",
    author="Nathan Spelts",
    author_email="nate@nathanspelts.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.25",
    ],
    entry_points={
        "console_scripts": [
            "dns-ip-updater = dns_ip_updater.main:main",
        ],
    },
)

