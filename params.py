import os
from collections import OrderedDict

import numpy as np
import tensorflow as tf

#### CONST
## Initialize Constant
flags = tf.app.flags
FLAGS = flags.FLAGS

batch_size=128
img_height=66
img_width=200
img_channels=3

## Nvida's camera format
flags.DEFINE_integer('img_h', img_height, 'The image height.')
flags.DEFINE_integer('img_w', img_width, 'The image width.')
flags.DEFINE_integer('img_c', img_channels, 'The number of channels.')

## Fix random seed for reproducibility
np.random.seed(42)

## Path
data_dir = os.path.abspath('./epochs')
out_dir = os.path.abspath('./output')
model_dir = os.path.abspath('./models')