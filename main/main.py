import models
import argparse
import tensorflow as tf

parser = argparse.ArgumentParser(description="Up-Scales an image using Image Super Resolution Model")
parser.add_argument("imgpath", type=str, nargs="+", help="Path to input image")
parser.add_argument("--model", type=str, default="dsr", help="Use either image super resolution (sr) or denoising auto encoder sr (dsr)")
parser.add_argument("--scale", default=2, help='Scaling factor. Default = 2x')
parser.add_argument("--mode", default="patch", type=str, help='Mode of operation. Choices are "fast" or "patch"')
parser.add_argument("--save_intermediate", dest='save', default='True', type=str,
                        help="Whether to save bilinear upscaled image")
parser.add_argument("--suffix", default="scaled", type=str, help='Suffix of saved image')
parser.add_argument("--patch_size", type=int, default=8, help='Patch Size')

def strToBool(v):
    return v.lower() in ("true", "yes", "t", "1")

args = parser.parse_args()


suffix = args.suffix

model_type = str(args.model).lower()
if not model_type in ["sr", "esr"]:
    raise ValueError('Model type must be either "sr", "esr"')

mode = str(args.mode).lower()
assert mode in ['fast', 'patch'], 'Mode of operation must be either "fast" or "patch"'

scale_factor = int(args.scale)
save = strToBool(args.save)

patch_size = int(args.patch_size)
assert patch_size > 0, "Patch size must be a positive integer"

with tf.device('/CPU:0'):
    path = args.imgpath
    for p in path:
        if model_type == "sr":
            model = models.ImageSuperResolutionModel(scale_factor)
        elif model_type == "dsr":
            model = models.DenoisingAutoEncoderSR(scale_factor)
        else:
            model = models.DenoisingAutoEncoderSR(scale_factor)

        model.upscale(p, save_intermediate=save, mode=mode, patch_size=patch_size, suffix=suffix)
