from taproot.pretrained import (
    CLIPViTLTextEncoderWithProjection,
    OpenCLIPViTGTextEncoder
)

__all__ = [
    "SDXLHelloWorldV7TextEncoderPrimary",
    "SDXLHelloWorldV7TextEncoderSecondary"
]

class SDXLHelloWorldV7TextEncoderPrimary(CLIPViTLTextEncoderWithProjection):
    """
    SDXL HelloWorld V7 Primary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-hello-world-v7-text-encoder.fp16.safetensors"

class SDXLHelloWorldV7TextEncoderSecondary(OpenCLIPViTGTextEncoder):
    """
    SDXL HelloWorld V7 Secondary Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-xl-hello-world-v7-text-encoder-2.fp16.safetensors"
