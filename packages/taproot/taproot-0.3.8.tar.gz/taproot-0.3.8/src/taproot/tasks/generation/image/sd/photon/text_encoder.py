from taproot.pretrained import CLIPViTLTextEncoder

__all__ = [
    "StableDiffusionPhotonV1TextEncoder"
]

class StableDiffusionPhotonV1TextEncoder(CLIPViTLTextEncoder):
    """
    Photon V1 Text Encoder
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v1-5-photon-v1-text-encoder.fp16.safetensors"
