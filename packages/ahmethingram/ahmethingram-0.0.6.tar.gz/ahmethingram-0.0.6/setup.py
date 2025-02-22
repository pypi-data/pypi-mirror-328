from setuptools import setup, find_packages

setup(
    name="ahmethingram",  # اسم المكتبة
    version="0.0.6", 
    packages=find_packages(),
    install_requires=[],  # ضع المتطلبات هنا إن وجدت
    author="Ahmed Asaad",
    author_email="ahmadasaadmajed1@gmail.com",
    description='😁🤩🤗🤗🤗🙂😚😁',
    long_description=open('README.md').read(),  # إذا كنت تستخدم ملف README.md للوصف
    long_description_content_type='text/markdown',  # استخدم هذا إذا كنت تستخدم Markdown
    url="https://github.com/aamya2003/ahmethingram",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",

    ],
    python_requires=">=3.6",
)
