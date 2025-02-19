from taproot.pretrained import (
    CLIPViTLTextEncoderWithProjection,
    OpenCLIPViTGTextEncoder
)

__all__ = [
    "SDXLNightVisionV9TextEncoderPrimary",
    "SDXLNightVisionV9TextEncoderSecondary"
]

class SDXLNightVisionV9TextEncoderPrimary(CLIPViTLTextEncoderWithProjection):
    """
    SDXL NightVision V9 Primary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-nightvision-v9-text-encoder.fp16.safetensors"

class SDXLNightVisionV9TextEncoderSecondary(OpenCLIPViTGTextEncoder):
    """
    SDXL NightVision V9 Secondary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-nightvision-v9-text-encoder-2.fp16.safetensors"
