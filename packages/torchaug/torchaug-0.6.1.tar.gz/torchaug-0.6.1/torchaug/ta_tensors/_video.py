# ==================================
# Copyright: CEA-LIST/DIASI/SIALV/
# Author : Torchaug Developers
# License: CECILL-C
# ==================================

# Code partially based on Torchvision (BSD 3-Clause License), available at:
#   https://github.com/pytorch/vision

from __future__ import annotations

from typing import Any, Optional, Union

import torch

from ._ta_tensor import TATensor


class Video(TATensor):
    """:class:`torch.Tensor` subclass for videos.

    Args:
        data: Any data that can be turned into a tensor with :func:`torch.as_tensor`.
        dtype: Desired data type. If omitted, will be inferred from
            ``data``.
        device: Desired device. If omitted and ``data`` is a
            :class:`torch.Tensor`, the device is taken from it. Otherwise, the video is constructed on the CPU.
        requires_grad: Whether autograd should record operations. If omitted and
            ``data`` is a :class:`torch.Tensor`, the value is taken from it. Otherwise, defaults to ``False``.
    """

    def __new__(
        cls,
        data: Any,
        *,
        dtype: Optional[torch.dtype] = None,
        device: Optional[Union[torch.device, str, int]] = None,
        requires_grad: Optional[bool] = None,
    ) -> Video:
        tensor = cls._to_tensor(data, dtype=dtype, device=device, requires_grad=requires_grad)
        if data.ndim < 4:
            raise ValueError
        return tensor.as_subclass(cls)

    def __repr__(self, *, tensor_contents: Any = None) -> str:  # type: ignore[override]
        return self._make_repr()
