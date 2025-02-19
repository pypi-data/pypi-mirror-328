from __future__ import annotations

from dataclasses import dataclass, field

from typing import Any, Union, Dict, Optional, List, Tuple, Literal, TYPE_CHECKING
from typing_extensions import Self

if TYPE_CHECKING:
    import torch

__all__ = [
    "mask_from_seq_lengths",
    "mask_from_start_end_indices",
    "mask_from_frac_lengths",
    "MaskWeightBuilder",
]

def mask_from_seq_lengths(
    t: torch.Tensor,
    length: Optional[int]=None
) -> torch.Tensor:
    """
    Convert a seq_lengths tensor to a mask tensor

    :param t: A tensor of seq_lengths
    :param length: The length of the mask
    """
    import torch

    if length is None:
        length = t.max().item() # type: ignore[assignment]

    mask = torch.arange(length, device=t.device, dtype=t.dtype) # type: ignore[arg-type]
    return mask[None, :] < t[:, None]

def mask_from_start_end_indices(
    seq_length: torch.Tensor,
    start: torch.Tensor,
    end: torch.Tensor,
) -> torch.Tensor:
    """
    Convert start and end indices to a mask

    :param seq_length: The length of the sequence
    :param start: The start indices
    :param end: The end indices
    """
    import torch
    seq = torch.arange(seq_length.max().item(), device=seq_length.device).long()
    start_mask = seq[None, :] >= start[:, None]
    end_mask = seq[None, :] < end[:, None]
    return start_mask & end_mask

def mask_from_frac_lengths(
    seq_length: torch.Tensor,
    frac_lengths: torch.Tensor,
    generator: Optional[torch.Generator]=None
) -> torch.Tensor:
    """
    Convert fractional lengths to a mask

    :param seq_length: The length of the sequence
    :param frac_lengths: The fractional lengths
    :param generator: The random number generator, optional
    """
    import torch
    lengths = (frac_lengths * seq_length).long()
    max_start = seq_length - lengths

    rand = torch.randn(
        *frac_lengths.shape,
        device=frac_lengths.device,
        dtype=frac_lengths.dtype,
        generator=generator
    )
    start = (max_start * rand).long().clamp(min=0)
    end = start + lengths
    
    return mask_from_start_end_indices(seq_length, start, end)

@dataclass(frozen=True)
class DiffusionMask:
    """
    Holds all the variables needed to compute a mask.
    """
    width: int
    height: Optional[int]

    def calculate(self) -> torch.Tensor:
        """
        These weights are always 1.
        """
        import torch
        if self.height is None:
            return torch.ones(self.width)
        return torch.ones(self.height, self.width)

@dataclass(frozen=True)
class DiffusionUnmask(DiffusionMask):
    """
    Holds all variables need to compute an unmask.
    Unmasks are used to ensure no area of a diffusion is completely ommitted by chunks.
    There is probably a much more efficient way to calculate this. Help is welcomed!
    """
    left: bool
    right: bool
    top: Optional[bool]
    bottom: Optional[bool]

    def unmask_left(
        self,
        x: int,
        m_x: int,
        y: Optional[int]=None,
        m_y: Optional[int]=None
    ) -> bool:
        """
        Determines if the left should be unmasked.
        """
        if not self.left:
            return False
        if x > m_x:
            return False
        if y is None or m_y is None or self.height is None:
            return True
        if y > m_y:
            return x <= self.height - y
        return x <= y

    def unmask_top(self, x: int, y: int, m_x: int, m_y: int) -> bool:
        """
        Determines if the top should be unmasked.
        """
        if not self.top:
            return False
        if y > m_y:
            return False
        if x > m_x:
            return y <= self.width - x
        return y <= x

    def unmask_right(
        self,
        x: int,
        m_x: int,
        y: Optional[int]=None,
        m_y: Optional[int]=None
    ) -> bool:
        """
        Determines if the right should be unmasked.
        """
        if not self.right:
            return False
        if x < m_x:
            return False
        if y is None or m_y is None or self.height is None:
            return True
        if y > m_y:
            return x >= y
        return x >= self.height - y

    def unmask_bottom(self, x: int, y: int, m_x: int, m_y: int) -> bool:
        """
        Determines if the bottom should be unmasked.
        """
        if not self.bottom:
            return False
        if y < m_y:
            return False
        if x > m_x:
            return y >= x
        return y >= self.width - x

    def calculate(self) -> torch.Tensor:
        """
        Calculates the unmask.
        """
        import torch

        if self.height is None:
            unfeather_mask = torch.zeros(self.width)
            m_x = self.width // 2

            for x in range(self.width):
                if (
                    self.unmask_left(x=x, m_x=m_x) or
                    self.unmask_right(x=x, m_x=m_x)
                ):
                    x_deviation = abs(m_x - x) / self.width
                    unfeather_mask[x] = min(1.0, 1.0 * x_deviation / 0.29)
        else:
            unfeather_mask = torch.zeros(self.height, self.width)
            m_x = self.width // 2
            m_y = self.height // 2

            for y in range(self.height):
                for x in range(self.width):
                    if (
                        self.unmask_left(x=x, y=y, m_x=m_x, m_y=m_y) or
                        self.unmask_top(x=x, y=y, m_x=m_x, m_y=m_y) or
                        self.unmask_right(x=x, y=y, m_x=m_x, m_y=m_y) or
                        self.unmask_bottom(x=x, y=y, m_x=m_x, m_y=m_y)
                    ):
                        x_deviation = abs(m_x - x) / self.width
                        y_deviation = abs(m_y - y) / self.height
                        unfeather_mask[y, x] = min(1.0, 1.0 * max(x_deviation, y_deviation) / 0.29)

        return unfeather_mask

@dataclass(frozen=True)
class BilinearDiffusionMask(DiffusionMask):
    """
    Feathers the edges of a mask.
    """
    ratio: float

    def calculate(self) -> torch.Tensor:
        """
        Calculates weights in linear gradients.
        """
        import torch
        tensor = super(BilinearDiffusionMask, self).calculate()
        latent_length = int(self.ratio * self.width)

        for i in range(latent_length):
            feathered = torch.tensor(i / latent_length)

            if self.height is None:
                tensor[i] = torch.minimum(tensor[i], feathered)
                tensor[self.width - i - 1] = torch.minimum(
                    tensor[self.width - i - 1],
                    feathered
                )
            else:
                tensor[:, i] = torch.minimum(tensor[:, i], feathered)
                tensor[i, :] = torch.minimum(tensor[i, :], feathered)
                tensor[:, self.width - i - 1] = torch.minimum(
                    tensor[:, self.width - i - 1],
                    feathered
                )
                tensor[self.height - i - 1, :] = torch.minimum(
                    tensor[self.height - i - 1, :],
                    feathered
                )
        return tensor

@dataclass(frozen=True)
class GaussianDiffusionMask(DiffusionMask):
    """
    Feathers the edges and corners using gaussian probability.
    """
    deviation: float
    growth: float

    def calculate(self) -> torch.Tensor:
        """
        Calculates weights with a gaussian distribution
        """
        import torch
        import numpy as np
        midpoint = (self.width - 1) / 2
        x_probabilities = [
            np.exp(-(x - midpoint) * (x - midpoint) / (self.width ** (2 + self.growth)) / (2 * self.deviation)) / np.sqrt(2 * np.pi * self.deviation)
            for x in range(self.width)
        ]

        if self.height is None:
            weights = torch.tensor(x_probabilities)
        else:
            midpoint = (self.height - 1) / 2
            y_probabilities = [
                np.exp(-(y - midpoint) * (y - midpoint) / (self.height ** (2 + self.growth)) / (2 * self.deviation)) / np.sqrt(2 * np.pi * self.deviation)
                for y in range(self.height)
            ]

            weights_np = np.outer(y_probabilities, x_probabilities)
            weights = torch.tile(torch.tensor(weights_np), (1, 1))

        weights = weights / weights.max()
        return weights

@dataclass
class MaskWeightBuilder:
    """
    A class for computing blending masks given dimensions and some optional parameters

    Stores masks on the device for speed. Be sure to free memory when no longer needed.
    """
    device: Union[str, torch.device]
    dtype: torch.dtype

    constant_weights: Dict[DiffusionMask, torch.Tensor] = field(default_factory=dict)
    unmasked_weights: Dict[DiffusionUnmask, torch.Tensor] = field(default_factory=dict)
    bilinear_weights: Dict[BilinearDiffusionMask, torch.Tensor] = field(default_factory=dict)
    gaussian_weights: Dict[GaussianDiffusionMask, torch.Tensor] = field(default_factory=dict)

    def clear(self) -> None:
        """
        Clears all stored tensors
        """
        for key in list(self.constant_weights.keys()):
            del self.constant_weights[key]
        for key in list(self.bilinear_weights.keys()):
            del self.bilinear_weights[key]
        for key in list(self.gaussian_weights.keys()):
            del self.gaussian_weights[key]
        for key in list(self.unmasked_weights.keys()):
            del self.unmasked_weights[key]

    def __enter__(self) -> Self:
        """
        Implement base enter.
        """
        return self

    def __exit__(self, *args: Any) -> None:
        """
        On exit, clear tensors.
        """
        self.clear()

    def frames(
        self,
        frames: List[int],
        start: Optional[int]=None,
        end: Optional[int]=None
    ) -> torch.Tensor:
        """
        Calculates a 1D frame mask
        """
        import torch
        mask = torch.tensor(frames)
        if start is not None:
            mask = torch.where(mask >= start, mask, -1)
        if end is not None:
            mask = torch.where(mask < end, mask, -1)
        return torch.where(mask >= 0, 1, 0).to(
            dtype=self.dtype,
            device=self.device
        )

    def audio(
        self,
        frames: List[int],
        frequencies: torch.Tensor,
        amplitudes: torch.Tensor,
        frequency: Optional[Union[int, Tuple[int, int]]]=None,
        channel: Optional[Union[int, Tuple[int, ...]]]=None
    ) -> torch.Tensor:
        """
        Calculates a 1D audio mask
        """
        import torch
        from einops import repeat

        num_frames = len(frames)

        if frequency is None:
            return torch.ones((num_frames)).to(device=self.device, dtype=self.dtype)

        num_channels = amplitudes.shape[-1]

        if isinstance(frequency, tuple):
            lo, hi = frequency
        else:
            lo, hi = frequency * 0.9, frequency * 1.1 # type: ignore[assignment]

        frequency_mask = torch.where((lo <= frequencies) & (frequencies < hi), 1, 0)
        frequency_mask = repeat(frequency_mask, "h -> f h c", f=num_frames, c=num_channels)
        masked_amplitude = amplitudes[frames, :, :] * frequency_mask

        if channel is not None:
            if isinstance(channel, tuple):
                masked_amplitude = masked_amplitude[:, :, channel]
            else:
                masked_amplitude = masked_amplitude[:, :, [channel]]

        masked_amplitude = torch.mean(masked_amplitude, dim=2)
        masked_amplitude = torch.sum(masked_amplitude, dim=1) / torch.sum(torch.where(masked_amplitude > 0, 1, 0), dim=1)
        return masked_amplitude

    def constant(
        self,
        width: int,
        height: Optional[int]=None,
        **kwargs: Any
    ) -> torch.Tensor:
        """
        Calculates the constant mask. No feathering.
        """
        mask = DiffusionMask(
            width=width,
            height=height
        )
        if mask not in self.constant_weights:
            self.constant_weights[mask] = mask.calculate().to(
                dtype=self.dtype,
                device=self.device
            )
        return self.constant_weights[mask]

    def bilinear(
        self,
        width: int,
        height: Optional[int]=None,
        unfeather_left: bool=False,
        unfeather_right: bool=False,
        unfeather_top: bool=False,
        unfeather_bottom: bool=False,
        ratio: float=0.25,
        **kwargs: Any
    ) -> torch.Tensor:
        """
        Calculates the bilinear mask.
        """
        import torch
        mask = BilinearDiffusionMask(
            width=width,
            height=height,
            ratio=ratio
        )
        unmask = DiffusionUnmask(
            width=width,
            height=height,
            left=unfeather_left,
            top=unfeather_top,
            right=unfeather_right,
            bottom=unfeather_bottom
        )
        if mask not in self.bilinear_weights:
            self.bilinear_weights[mask] = mask.calculate().to(
                dtype=self.dtype,
                device=self.device
            )
        if unmask not in self.unmasked_weights:
            self.unmasked_weights[unmask] = unmask.calculate().to(
                dtype=self.dtype,
                device=self.device
            )
        return torch.maximum(
            self.bilinear_weights[mask],
            self.unmasked_weights[unmask]
        )

    def gaussian(
        self,
        width: int,
        height: Optional[int]=None,
        unfeather_left: bool=False,
        unfeather_top: bool=False,
        unfeather_right: bool=False,
        unfeather_bottom: bool=False,
        deviation: float=0.01,
        growth: float=0.15,
        **kwargs: Any
    ) -> torch.Tensor:
        """
        Calculates the gaussian mask, optionally unfeathered.
        """
        import torch
        mask = GaussianDiffusionMask(
            width=width,
            height=height,
            deviation=deviation,
            growth=growth
        )
        unmask = DiffusionUnmask(
            width=width,
            height=height,
            left=unfeather_left,
            top=unfeather_top,
            right=unfeather_right,
            bottom=unfeather_bottom
        )
        if mask not in self.gaussian_weights:
            self.gaussian_weights[mask] = mask.calculate().to(
                dtype=self.dtype,
                device=self.device
            )
        if unmask not in self.unmasked_weights:
            self.unmasked_weights[unmask] = unmask.calculate().to(
                dtype=self.dtype,
                device=self.device
            )
        return torch.maximum(
            self.gaussian_weights[mask],
            self.unmasked_weights[unmask]
        )

    def temporal(
        self,
        tensor: torch.Tensor,
        frames: Optional[int]=None,
        unfeather_start: bool=False,
        unfeather_end: bool=False
    ) -> torch.Tensor:
        """
        Potentially expands a tensor temporally
        """
        import torch
        if frames is None:
            return tensor
        tensor = tensor.unsqueeze(2).repeat(1, 1, frames, 1, 1)
        if not unfeather_start or not unfeather_end:
            frame_length = frames // 3
            for i in range(frame_length):
                feathered = torch.tensor(i / frame_length)
                if not unfeather_start:
                    tensor[:, :, i, :, :] = torch.minimum(
                        tensor[:, :, i, :, :],
                        feathered
                    )
                if not unfeather_end:
                    tensor[:, :, frames - i - 1, :, :] = torch.minimum(
                        tensor[:, :, frames - i - 1, :, :],
                        feathered
                    )
        return tensor

    def __call__(
        self,
        mask_type: Literal["constant", "bilinear", "gaussian"],
        batch: int,
        dim: int,
        width: int,
        height: Optional[int]=None,
        frames: Optional[int]=None,
        unfeather_left: bool=False,
        unfeather_top: bool=False,
        unfeather_right: bool=False,
        unfeather_bottom: bool=False,
        unfeather_start: bool=False,
        unfeather_end: bool=False,
        **kwargs: Any
    ) -> torch.Tensor:
        """
        Calculates a mask depending on the method requested.
        """
        if mask_type == "constant":
            get_mask = self.constant
        elif mask_type == "bilinear":
            get_mask = self.bilinear
        elif mask_type == "gaussian":
            get_mask = self.gaussian
        else:
            raise AttributeError(f"Unknown mask type {mask_type}")

        mask = get_mask(
            width=width,
            height=height,
            unfeather_left=unfeather_left,
            unfeather_top=unfeather_top,
            unfeather_right=unfeather_right,
            unfeather_bottom=unfeather_bottom,
            **kwargs
        )

        if height is None:
            return mask.unsqueeze(0).unsqueeze(-1).repeat(batch, 1, dim)

        return self.temporal(
            mask.unsqueeze(0).unsqueeze(0).repeat(batch, dim, 1, 1),
            frames=frames,
            unfeather_start=unfeather_start,
            unfeather_end=unfeather_end,
        )
