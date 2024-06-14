from setuptools import find_packages, setup

package_name = 'mpu6050'

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
    maintainer='ubuntu',
    maintainer_email='tjpink@gmail.com',
    description='Publish MPU6050 raw data.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mpu6050_node = mpu6050.mpu6050_node:main'
        ],
    },
)
