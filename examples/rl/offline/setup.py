from os import path

from setuptools import find_packages, setup

# this_dir = path.abspath(path.dirname(__file__))
# with open(path.join(this_dir, "README.md"), encoding="utf-8") as f:
#     long_description = f.read()

setup(
    name="OfflineRL",
    description="Offline RL with d3rlpy",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    python_requires=">=3.7",
    install_requires=[
        "setuptools>=41.0.0,!=50.0",
        "ruamel.yaml==0.17.17",
        "smarts[camera-obs] @ git+https://github.com/huawei-noah/SMARTS.git@sb3-1",
        "tensorflow==2.4.0",
        "torchinfo==1.6.4",
        "torchvision==0.12.0",
        "d3rlpy>=1.0.0",
        "d4rl-atari @ git+https://github.com/takuseno/d4rl-atari",
        "d4rl-pybullet @ git+https://github.com/takuseno/d4rl-pybullet",
    ],
)