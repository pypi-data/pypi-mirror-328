from taproot.pretrained import (
    CLIPViTLTextEncoderWithProjection,
    OpenCLIPViTGTextEncoder
)

__all__ = [
    "SDXLRealVisV50TextEncoderPrimary",
    "SDXLRealVisV50TextEncoderSecondary"
]

class SDXLRealVisV50TextEncoderPrimary(CLIPViTLTextEncoderWithProjection):
    """
    SDXL RealVis XL 5.0 Primary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-realvis-v5-0-text-encoder.fp16.safetensors"

class SDXLRealVisV50TextEncoderSecondary(OpenCLIPViTGTextEncoder):
    """
    SDXL RealVis XL 5.0 Secondary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-realvis-v5-0-text-encoder-2.fp16.safetensors"
