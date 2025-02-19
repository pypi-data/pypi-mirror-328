from ..base import (
    StableDiffusion35Large,
    StableDiffusion35LargeInt8,
    StableDiffusion35LargeNF4,
    StableDiffusion35Medium,
)

from .transformer import (
    StableDiffusion35LargeAbsynthV19Transformer,
    StableDiffusion35LargeAbsynthV19TransformerInt8,
    StableDiffusion35LargeAbsynthV19TransformerNF4,
    StableDiffusion35LargeAbsynthV20Transformer,
    StableDiffusion35LargeAbsynthV20TransformerInt8,
    StableDiffusion35LargeAbsynthV20TransformerNF4,
    StableDiffusion35MediumAbsynthV20Transformer,
)

__all__ = [
    "StableDiffusion35LargeAbsynthV19",
    "StableDiffusion35LargeAbsynthV19Int8",
    "StableDiffusion35LargeAbsynthV19NF4",
    "StableDiffusion35LargeAbsynthV20",
    "StableDiffusion35LargeAbsynthV20Int8",
    "StableDiffusion35LargeAbsynthV20NF4",
    "StableDiffusion35MediumAbsynthV20",
]

class StableDiffusion35LargeAbsynthV19(StableDiffusion35Large):
    model = "stable-diffusion-v3-5-large-absynth-v1-9"
    pretrained_models = {
        **StableDiffusion35Large.pretrained_models,
        **{"transformer": StableDiffusion35LargeAbsynthV19Transformer},
    }

class StableDiffusion35LargeAbsynthV19Int8(StableDiffusion35LargeInt8):
    model = "stable-diffusion-v3-5-large-absynth-v1-9-int8"
    pretrained_models = {
        **StableDiffusion35LargeInt8.pretrained_models,
        **{"transformer": StableDiffusion35LargeAbsynthV19TransformerInt8},
    }

class StableDiffusion35LargeAbsynthV19NF4(StableDiffusion35LargeNF4):
    model = "stable-diffusion-v3-5-large-absynth-v1-9-nf4"
    pretrained_models = {
        **StableDiffusion35LargeNF4.pretrained_models,
        **{"transformer": StableDiffusion35LargeAbsynthV19TransformerNF4},
    }

class StableDiffusion35LargeAbsynthV20(StableDiffusion35Large):
    model = "stable-diffusion-v3-5-large-absynth-v2-0"
    pretrained_models = {
        **StableDiffusion35Large.pretrained_models,
        **{"transformer": StableDiffusion35LargeAbsynthV20Transformer},
    }

class StableDiffusion35LargeAbsynthV20Int8(StableDiffusion35LargeInt8):
    model = "stable-diffusion-v3-5-large-absynth-v2-0-int8"
    pretrained_models = {
        **StableDiffusion35LargeInt8.pretrained_models,
        **{"transformer": StableDiffusion35LargeAbsynthV20TransformerInt8},
    }

class StableDiffusion35LargeAbsynthV20NF4(StableDiffusion35LargeNF4):
    model = "stable-diffusion-v3-5-large-absynth-v2-0-nf4"
    pretrained_models = {
        **StableDiffusion35LargeNF4.pretrained_models,
        **{"transformer": StableDiffusion35LargeAbsynthV20TransformerNF4},
    }

class StableDiffusion35MediumAbsynthV20(StableDiffusion35Medium):
    model = "stable-diffusion-v3-5-medium-absynth-v2-0"
    pretrained_models = {
        **StableDiffusion35Medium.pretrained_models,
        **{"transformer": StableDiffusion35MediumAbsynthV20Transformer},
    }
