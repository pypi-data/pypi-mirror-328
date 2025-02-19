from taproot.pretrained import (
    CLIPViTLTextEncoderWithProjection,
    OpenCLIPViTGTextEncoder
)

__all__ = [
    "SDXLStoiqoNewRealityProTextEncoderPrimary",
    "SDXLStoiqoNewRealityProTextEncoderSecondary"
]

class SDXLStoiqoNewRealityProTextEncoderPrimary(CLIPViTLTextEncoderWithProjection):
    """
    SDXL Stoiqo NewReality Pro Primary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-stoiqo-newreality-pro-text-encoder.fp16.safetensors"

class SDXLStoiqoNewRealityProTextEncoderSecondary(OpenCLIPViTGTextEncoder):
    """
    SDXL Stoiqo NewReality Pro Secondary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-stoiqo-newreality-pro-text-encoder-2.fp16.safetensors"
