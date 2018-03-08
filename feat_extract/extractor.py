import caffe 
import pickle
import numpy as np



# required only if working in gpu mode
gpu_id = 0

extract_from_layer = “pool5/drop_7x7_s1” 
input_images_file = “./cat.jpeg”
model_def= “/path/to/deploy.prototxt”
pretrained_model=”/path/to/pretrained-model.caffemodel”

# output file to write extracted features to disk
output_pkl_file_name = “path/to/output-file.pkl”

# change based on your deploy.prototxt file
batch_size = 1
