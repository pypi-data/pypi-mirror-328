from ..pretrained.unet import StableDiffusionUNet

__all__ = ["StableDiffusionLyrielV16UNet"]

class StableDiffusionLyrielV16UNet(StableDiffusionUNet):
    """
    Lyriel V1.6 UNet model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v1-5-lyriel-v1-6-unet.fp16.safetensors"
