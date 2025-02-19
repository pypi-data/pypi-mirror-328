from ..pretrained.unet import StableDiffusionUNet

__all__ = ["StableDiffusionPhotonV1UNet"]

class StableDiffusionPhotonV1UNet(StableDiffusionUNet):
    """
    Photon V1 UNet Model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v1-5-photon-v1-unet.fp16.safetensors"
