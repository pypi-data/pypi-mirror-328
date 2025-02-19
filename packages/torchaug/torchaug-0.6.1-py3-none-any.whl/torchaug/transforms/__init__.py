# ==================================
# Copyright: CEA-LIST/DIASI/SIALV/
# Author : Torchaug Developers
# License: CECILL-C
# ==================================

# ruff: noqa: F401
# ruff: noqa: D104

from torchvision.transforms import AutoAugmentPolicy, InterpolationMode

from . import functional
from ._augment import JPEG, CutMix, MixUp, RandomErasing
from ._auto_augment import AugMix, AutoAugment, RandAugment, TrivialAugmentWide
from ._color import (
    RGB,
    ColorJitter,
    Grayscale,
    RandomAdjustSharpness,
    RandomAutocontrast,
    RandomChannelPermutation,
    RandomColorJitter,
    RandomEqualize,
    RandomGrayscale,
    RandomInvert,
    RandomPhotometricDistort,
    RandomPosterize,
    RandomSolarize,
)
from ._container import (
    Compose,
    RandomApply,
    RandomChoice,
    RandomOrder,
    SequentialTransform,
)
from ._geometry import (
    CenterCrop,
    ElasticTransform,
    FiveCrop,
    Pad,
    RandomAffine,
    RandomCrop,
    RandomHorizontalFlip,
    RandomIoUCrop,
    RandomPerspective,
    RandomResize,
    RandomResizedCrop,
    RandomRotation,
    RandomShortestSize,
    RandomVerticalFlip,
    RandomZoomOut,
    Resize,
    ScaleJitter,
    TenCrop,
)
from ._meta import ClampBoundingBoxes, ConvertBoundingBoxFormat
from ._misc import (
    GaussianBlur,
    Identity,
    Lambda,
    LinearTransformation,
    Normalize,
    RandomGaussianBlur,
    SanitizeBoundingBoxes,
    ToDtype,
)
from ._temporal import UniformTemporalSubsample
from ._transform import RandomApplyTransform, Transform
from ._type_conversion import NestedToBatch, NestedToList, ToBatchImages, ToImage, ToPureTensor
