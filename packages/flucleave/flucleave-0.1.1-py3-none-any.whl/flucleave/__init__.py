"""
FluCleave: Predict influenza HA cleavage site pathogenicity

A deep learning tool for analyzing influenza virus hemagglutinin (HA) 
cleavage sites and predicting their pathogenicity (HPAI vs LPAI).

Key Features:
    - Sequence analysis of HA cleavage sites
    - Deep learning based pathogenicity prediction
    - Command-line interface for easy use
    - Support for both DNA and protein sequences
"""

import os
from pathlib import Path
import pkg_resources

# Package metadata
__version__ = '0.1.1'
__author__ = 'Cameron Norris'
__description__ = 'Deep learning prediction of HA cleavage site pathogenicity'

def get_data_dir() -> Path:
    """Get the data directory, handling both development and installed cases."""
    try:
        # When installed via pip
        return Path(pkg_resources.resource_filename('flucleave', 'data'))
    except Exception:
        # During development
        return Path(__file__).parent / 'data'

def get_model_dir() -> Path:
    """Get the model directory, handling both development and installed cases."""
    try:
        return Path(pkg_resources.resource_filename('flucleave', 'model'))
    except Exception:
        return Path(__file__).parent / 'model'

# Setup paths
DATA_DIR = get_data_dir()
MODEL_DIR = get_model_dir()

# Create required directories if they don't exist
# exist_ok=True prevents errors if directories already exist
MODEL_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

# Configure TensorFlow logging
# 0 = all messages are logged (default)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'