# -*- coding: utf-8 -*-
"""gpt2-simple.ipynb

Automatically generated by Colaboratory.
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
# !pip3 install gpt-2-simple

import tensorflow
print(tensorflow.__version__)

import gpt_2_simple as gpt2
import os
import requests

model_name = "124M"
base_dir = "/content/drive/My Drive/Colab Notebooks/gpt2_learning"
model_dir = os.path.join(base_dir,"models")
if not os.path.isdir(os.path.join(model_dir, model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_dir=model_dir,model_name=model_name)   # model is saved into current directory under /models/124M/


file_name = os.path.join(base_dir,"shakespeare.txt")
if not os.path.isfile(file_name):
	url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
	data = requests.get(url)
	
	with open(file_name, 'w') as f:
		f.write(data.text)
    

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              file_name,
							model_dir=model_dir,
              model_name=model_name,
							checkpoint_dir=os.path.join(base_dir,"checkpoint"),
              steps=1000)   # steps is max number of training steps

gpt2.generate(sess)

gpt2.generate(sess, prefix="2015 年")

