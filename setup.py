from setuptools import setup, find_packages

setup(
    name="coneventional",
    version='1.0.0',
    description='Parse conventional event summaries into objects.',

    long_description=open('README.rst', encoding='utf-8').read(),
    keywords=['python', 'events'],

    author='David Newman',
    url='https://github.com/davidnewman/coneventional',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    include_package_data=True,

    install_requires=open('requirements.txt').readlines(),
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
