from taproot.pretrained import CLIPViTLTextEncoder

__all__ = [
    "StableDiffusionDreamShaperV8TextEncoder"
]

class StableDiffusionDreamShaperV8TextEncoder(CLIPViTLTextEncoder):
    """
    DreamShaper V8 Text Encoder
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v1-5-dreamshaper-v8-text-encoder.fp16.safetensors"
