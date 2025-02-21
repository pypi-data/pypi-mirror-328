from setuptools import setup, find_packages

setup(
    name='Fnai_deepseek',  # 替换为你的库名
    version='0.4',  # 替换为你的版本号
    packages=find_packages(),  # 查找所有的包
    install_requires=[  # 如果你的库有依赖，可以在这里列出
        # 'requests',
    ],
    classifiers=[  # 可选的分类
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',  # 设置支持的Python版本
)
