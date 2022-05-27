# -*- coding: utf-8 -*-
"""commands.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zLVOqN6EvsG2z06LCFllw9R38U6vz0NC
"""

!python3 /content/drive/MyDrive/BIA2022/train.py --model Unet -c 1 -e 150 -m sampled -n _unet_sampled_image -i image

!cd

try:
    import google.colab
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

from pathlib import Path
if IN_COLAB:
    google.colab.drive.mount("/content/drive")
    
    # Change this if you created the shortcut in a different location
    AUX_DATA_ROOT = Path("/content/drive/MyDrive/BIA2022/")
    
    assert AUX_DATA_ROOT.is_dir(), "Have you forgot to 'Add a shortcut to Drive'?"
    
    import sys
    sys.path.append(str(AUX_DATA_ROOT))
else:
    AUX_DATA_ROOT = Path(".")

!ls

!python /content/drive/MyDrive/BIA2022/predict.py --model Unet -c 1 -m sampled -n _unet_sampled_mask -i mask
# python predict.py --model ConvLSTM -i image -mode sampled -n convlstm_from_mask_sampled_5channels -c 5