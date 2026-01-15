from setuptools import find_packages, setup

package_name = 'iqmattso_py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ian Q. Mattson',
    maintainer_email='iqmattso@mtu.edu',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = iqmattso_py_pubsub.publisher_member_function:main',
        ],
    },
)
