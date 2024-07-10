from setuptools import setup, find_packages

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Harisankar K',
    author_email = 'harisankarkaramchand@gmail.com',
    install_requires = ["JAMBA", "langchain", "streamlit", "python-dotenv","PyPDF2"],
    packages = find_packages()
)