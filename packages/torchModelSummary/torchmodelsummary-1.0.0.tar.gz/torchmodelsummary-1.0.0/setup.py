from setuptools import setup, find_packages

setup(
    name='torchModelSummary',
    version='1.0.0',
    description='A custom-renovated version of torchsummary module',
    long_description=open('README.md', 'r', encoding='UTF8').read(),
    long_description_content_type='text/markdown',
    author='Daun Kim',
    author_email='daunkim430@yonsei.ac.kr',
    url='https://github.com/DaunKimY/torchModelSummary',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'torch'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

## https://beeny-ds.tistory.com/entry/Package-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%EB%93%9C-%ED%8C%A8%ED%82%A4%EC%A7%80%ED%99%94-%E2%86%92-setuppy
## Ref for uploading to pypi: https://velog.io/@zo_meong/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8C%A8%ED%82%A4%EC%A7%80
## Ref for uploading to pypi: https://yoonminlee.com/python-package-deployment-pypi-github-actions#22-pypi