from setuptools import find_packages, setup

setup(
    name='chatapp',  # Package name
    version='0.1.2',  # Initial version
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # License type
    description='A Django app for chat functionality',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/chatapp',  # Replace with your repo URL
    author='Your Name',
    author_email='youremail@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',  # Adjust based on Django version
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'Django>=3.0',  # Add your dependencies here
        "dateparser",
        "twilio",
        "elevenlabs",
        "docx2txt"
    ],
    python_requires='>=3.6',
)
