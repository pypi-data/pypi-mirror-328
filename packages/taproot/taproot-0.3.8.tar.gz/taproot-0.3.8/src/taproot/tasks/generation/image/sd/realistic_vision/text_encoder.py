from taproot.pretrained import CLIPViTLTextEncoder

__all__ = [
    "StableDiffusionRealisticVisionV51TextEncoder",
    "StableDiffusionRealisticVisionV60TextEncoder"
]

class StableDiffusionRealisticVisionV51TextEncoder(CLIPViTLTextEncoder):
    """
    RealisticVision v5.1 Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v1-5-realistic-vision-v5-1-text-encoder.fp16.safetensors"

class StableDiffusionRealisticVisionV60TextEncoder(CLIPViTLTextEncoder):
    """
    RealisticVision v6.0 Text Encoder model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v1-5-realistic-vision-v6-0-text-encoder.fp16.safetensors"
