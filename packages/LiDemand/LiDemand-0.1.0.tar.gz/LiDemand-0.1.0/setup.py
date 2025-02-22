

from setuptools import setup, find_packages

setup(
    name='LiDemand',  # 包名称
    version='0.1.0',    # 版本号
    author='mayanjie1',
    author_email='mayanjie1@lixiang.com',
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.chehejia.com/cpd_myj/lilib/demandlib',  # 更新为你的项目地址
    packages=find_packages(),  # 自动找到所有包
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Python版本要求
)