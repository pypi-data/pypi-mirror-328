from taproot.pretrained import (
    CLIPViTLTextEncoderWithProjection,
    OpenCLIPViTGTextEncoder
)

__all__ = [
    "SDXLAnimagineV31TextEncoderPrimary",
    "SDXLAnimagineV31TextEncoderSecondary"
]

class SDXLAnimagineV31TextEncoderPrimary(CLIPViTLTextEncoderWithProjection):
    """
    SDXL Animagine V3.1 Primary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-animagine-v3-1-text-encoder.fp16.safetensors"

class SDXLAnimagineV31TextEncoderSecondary(OpenCLIPViTGTextEncoder):
    """
    SDXL Animagine V3.1 Secondary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-animagine-v3-1-text-encoder-2.fp16.safetensors"
