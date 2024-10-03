from setuptools import find_packages, setup

package_name = 'node_pkg'

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
    maintainer='ahmad',
    maintainer_email='ahmad@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "lidar = node_pkg.node:main",
            "draw_circle = node_pkg.draw_node:main",
            "pos_sub = node_pkg.sub_node:main",
            "pos_sub = node_pkg.sub_pub:main"
        ],
    },
)
