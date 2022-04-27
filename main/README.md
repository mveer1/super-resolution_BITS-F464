# Image Super Resolution

Implementation of Image Super Resolution CNN in Keras from the paper 
<i><a href="https://arxiv.org/pdf/1501.00092v3.pdf">Image Super-Resolution Using Deep Convolutional Networks</a></i>.

Also contains models that outperforms the above mentioned model, termed Expanded Super Resolution, Denoiseing Auto Encoder SRCNN which outperforms both of the above models and Deep Denoise SR, which with certain limitations, outperforms all of the above.

## Requirements
```
pillow
imageio
sklearn
scipy
tensorflow
keras
kapre
tensorflow-probability
scipy
h5py
```

## Usage

`python main.py "imgpath"`

The default model is DDSRCNN, To switch models :<br>
`python main.py "imgpath" --model="type"`, where type = `sr`, `dsr`

To change scaling factor :<br>
`python main.py "imgpath" --scale=s`, where s can be any number. Default `s = 2`

## Model Architecture
### Super Resolution CNN (SRCNN)
<img src="https://raw.githubusercontent.com/titu1994/ImageSuperResolution/master/architectures/SRCNN.png" height=100% width=25%>

Optimizer Used: Adam

### Super Resolution CNN with Denoiseing
<img src="https://raw.githubusercontent.com/titu1994/ImageSuperResolution/master/architectures/Denoise.png" height=100% width=40%>

The above is the "Denoiseing Auto Encoder SRCNN", which performs even better than SRCNN.

This model uses bridge connections between the convolutional layers of the same level in order to speed up convergence and improve output results. The bridge connections are averaged to be more robust. 

Since the training images are passed through a gausian filter (sigma = 0.5), then downscaled to 1/3rd the size, then upscaled to the original 33x33 size images, the images can be considered "noisy". Thus, this auto encoder quickly improves on the earlier results, and reduces the noisy output image problem faced by the simpler SRCNN model.
