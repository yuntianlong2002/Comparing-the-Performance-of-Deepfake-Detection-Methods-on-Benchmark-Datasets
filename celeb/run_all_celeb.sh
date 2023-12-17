#!/bin/bash

# List of files
files=(
# efficientnetb1_lstm_celebdf.pth
# efficientnetb1_lstm_dfdc.pth
# efficientnetb1_lstm_dftimit_hq.pth
# efficientnetb1_lstm_dftimit_lq.pth
# efficientnetb1_lstm_uadfv.pth
# efficientnetb7_celebdf.pth
# efficientnetb7_dfdc.pth
# efficientnetb7_dftimit_hq.pth
# efficientnetb7_dftimit_lq.pth
# efficientnetb7_uadfv.pth
mesonet_celebdf.pth
mesonet_dfdc.pth
mesonet_dftimit_hq.pth
mesonet_dftimit_lq.pth
mesonet_pretrain.pth
mesonet_uadfv.pth
resnet_lstm_celebdf.pth
resnet_lstm_dfdc.pth
resnet_lstm_dftimit_hq.pth
resnet_lstm_dftimit_lq.pth
resnet_lstm_uadfv.pth
# xception-b5690688.pth # no
xception_celebdf.pth
# xception_celebdf_seed25.pth
xception_dfdc.pth
# xception_dfdc_seed25.pth
xception_dftimit_hq.pth
# xception_dftimit_hq_seed25.pth
xception_dftimit_lq.pth
# xception_dftimit_lq_seed25.pth
xception_uadfv.pth
# xception_uadfv_seed25.pth
)

# Iterate over each file in the list
for file in "${files[@]}"; do
    # Remove the .pth extension to get the filename
    name="${file%.pth}"
    
    # Run the command and pipe the output to a text file with the same name as the file
    python deepfake_detector/dfdetector.py --benchmark True --data_path ~/Downloads/celebdf --detection_method "$name" --dataset celebdf > "celebdf_${name}.txt"
done
