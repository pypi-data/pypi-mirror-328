from taproot.pretrained import (
    CLIPViTLTextEncoderWithProjection,
    OpenCLIPViTGTextEncoder
)

__all__ = [
    "SDXLZavyChromaV10TextEncoderPrimary",
    "SDXLZavyChromaV10TextEncoderSecondary"
]

class SDXLZavyChromaV10TextEncoderPrimary(CLIPViTLTextEncoderWithProjection):
    """
    SDXL ZavyChroma V10 Primary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-zavychroma-v10-text-encoder.fp16.safetensors"

class SDXLZavyChromaV10TextEncoderSecondary(OpenCLIPViTGTextEncoder):
    """
    SDXL ZavyChroma V10 Secondary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-zavychroma-v10-text-encoder-2.fp16.safetensors"
