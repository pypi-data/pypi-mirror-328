"""
DynamicAxisControl Librery.

Linear trajectory generator for robotic axes, with the ability to synchronize up to two speed profiles, 
to maximize performance. Also perfect for calculating the trajectories of the CoreXY Axes....
"""

__version__ = "1.0.2"
__author__ = 'Davide Zuanon'
__credits__ = 'Private'
__doc__ = "https://github.com/daddi1987/DynamicAxisControl"


from .DynamicAxisControl import ProfileGenerator
import logging
import sys
import argparse

EnableLog = False
__all__ = ["ProfileGenerator"]

try:
    import numpy as np
except ImportError:
    raise ImportError("DynamicAxisControl requires NumPy. Install it with: pip install numpy")

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("DynamicAxisControl requires matplotlib. Install it with: pip install matplotlib")

try:
    import scipy
except ImportError:
    raise ImportError("DynamicAxisControl requires scipy. Install it with: pip install scipy")

try:
    import time
except ImportError:
    raise ImportError("DynamicAxisControl requires time. Install it with: pip install time")


if EnableLog == True:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("DynamicAxisControl module loaded successfully")


if sys.version_info < (3, 7):
    raise RuntimeError("DynamicAxisControl requires Python 3.7 or higher")


def main():
    parser = argparse.ArgumentParser(description="DynamicAxisControl CLI")
    parser.add_argument("--version", action="store_true", help="Mostra la versione della libreria")
    
    args = parser.parse_args()
    
    if args.version:
        print("DynamicAxisControl Version:", __version__)

if __name__ == "__main__":
    main()

