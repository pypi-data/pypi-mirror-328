from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='PyrpcSchedule',
    version='1.0.1',
    description="PyrpcSchedule Description",
    long_description=long_description,
    # long_description_content_type="text/x-rst",
    include_package_data=True,
    author='YanPing',
    author_email='zyphhxx@foxmail.com',
    maintainer='YanPing',
    maintainer_email='zyphhxx@foxmail.com',
    license='MIT License',
    url='https://gitee.com/ZYPH/pyrpc-schedule',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires=">=3.8",
    install_requires=[
        'kombu~=5.2.2',
        'pytz~=2024.1',
        'pika~=1.3.2',
        'psutil~=5.9.0',
        'eventlet~=0.39.0',
        'nameko~=2.14.1',
        'pymongo~=4.8.0',
        'kombu~=5.2.2',
        'amqp~=5.0.6',
        'psutil~=5.9.0',
        'pycryptodomex~=3.21.0',
    ]
)
