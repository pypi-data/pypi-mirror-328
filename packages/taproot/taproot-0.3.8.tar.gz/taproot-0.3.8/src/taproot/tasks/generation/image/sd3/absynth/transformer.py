from ..pretrained import (
    StableDiffusion35LargeTransformer,
    StableDiffusion35LargeTransformerInt8,
    StableDiffusion35LargeTransformerNF4,
    StableDiffusion35MediumTransformer,
)

__all__ = [
    "StableDiffusion35LargeAbsynthV19Transformer",
    "StableDiffusion35LargeAbsynthV19TransformerInt8",
    "StableDiffusion35LargeAbsynthV19TransformerNF4",
    "StableDiffusion35LargeAbsynthV20Transformer",
    "StableDiffusion35LargeAbsynthV20TransformerInt8",
    "StableDiffusion35LargeAbsynthV20TransformerNF4",
    "StableDiffusion35MediumAbsynthV20Transformer",
]

class StableDiffusion35LargeAbsynthV19Transformer(StableDiffusion35LargeTransformer):
    """
    Absynth V1.9 Transformer Model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v3-5-large-absynth-v1-9-transformer.fp16.safetensors"

class StableDiffusion35LargeAbsynthV19TransformerInt8(StableDiffusion35LargeTransformerInt8):
    """
    Absynth V1.9 Transformer Model (Int8 Quantization)
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v3-5-large-absynth-v1-9-transformer.int8.fp16.safetensors"

class StableDiffusion35LargeAbsynthV19TransformerNF4(StableDiffusion35LargeTransformerNF4):
    """
    Absynth V1.9 Transformer Model (NF4 Quantization)
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v3-5-large-absynth-v1-9-transformer.nf4.fp16.safetensors"

class StableDiffusion35LargeAbsynthV20Transformer(StableDiffusion35LargeTransformer):
    """
    Absynth V2.0 Transformer Model
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v3-5-large-absynth-v2-0-transformer.fp16.safetensors"

class StableDiffusion35LargeAbsynthV20TransformerInt8(StableDiffusion35LargeTransformerInt8):
    """
    Absynth V2.0 Transformer Model (Int8 Quantization)
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v3-5-large-absynth-v2-0-transformer.int8.fp16.safetensors"

class StableDiffusion35LargeAbsynthV20TransformerNF4(StableDiffusion35LargeTransformerNF4):
    """
    Absynth V2.0 Transformer Model (NF4 Quantization)
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v3-5-large-absynth-v2-0-transformer.nf4.fp16.safetensors"

class StableDiffusion35MediumAbsynthV20Transformer(StableDiffusion35MediumTransformer):
    """
    Absynth V2.0 Transformer Model (Medium)
    """
    model_url = "https://huggingface.co/benjamin-paine/taproot-common/resolve/main/image-generation-stable-diffusion-v3-5-medium-absynth-v2-0-transformer.fp16.safetensors"
