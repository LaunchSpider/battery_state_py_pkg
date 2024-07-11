from setuptools import find_packages, setup

package_name = 'battery_state_py_pkg'

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
    maintainer='launchspider',
    maintainer_email='danylo.bezruchenko@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "LED_panel = battery_state_py_pkg.LED_panel:main",
            "battery = battery_state_py_pkg.battery:main"
        ],
    },
)
