from setuptools import setup, Extension, find_packages

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="bharatpe",
    version="0.0.2",
    description="Hmm, Payments API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://t.me/North_Yankton",
    author="Alpha",
    author_email="imr@outlook.in",
    license="MIT",
    keywords="payments api bharatpe",
    project_urls={
        "Tracker": "https://github.com/Alpha-Like/bharatpe/issues",
        "Community": "https://t.me/SpLBots",
        "Source": "https://github.com/Alpha-Like/bharatpe",
        "Documentation": "https://t.me/SpLBots",
    },
    python_requires="~=3.7",
    packages=find_packages(),
    test_suite="tests",
    zip_safe=False,
    install_requires = [
        'requests',
        'pymongo'
    ]
)