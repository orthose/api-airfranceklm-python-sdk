from setuptools import setup, find_packages

setup(
    name='api-airfranceklm',
    version='0.0.1',
    description='SDK to request Airfrance KLM REST API',
    url='https://github.com/orthose/api-airfranceklm-python-sdk',
    author='Maxime Vincent',
    author_email='maxime.vincent1@universite-paris-saclay.fr',
    keywords='api, airfrance, klm, flights, booking, offers, fare',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=['requests', 'pandas']
)