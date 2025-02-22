# -*- coding: utf-8 -*-
"""Tensor Quantizer module."""

import typing as tp
from dataclasses import dataclass, field

import torch
import torch.nn as nn

from deepcompressor.calib.config import SkipBasedQuantLowRankCalibConfig
from deepcompressor.calib.lowrank import LowRankBranch, QuantLowRankCalibrator
from deepcompressor.calib.range import calibrate_dynamic_range
from deepcompressor.data.cache import TensorsCache
from deepcompressor.data.common import TensorType
from deepcompressor.data.range import DynamicRange
from deepcompressor.quantizer.processor import Quantizer

from .config import (
    DiffusionActivationQuantizerConfig,
    DiffusionGPTQConfig,
    DiffusionQuantizerConfig,
    DiffusionWeightQuantizerConfig,
)

__all__ = ["DiffusionQuantizer", "DiffusionWeightQuantizer", "DiffusionActivationQuantizer"]


@dataclass
class DiffusionQuantizer(Quantizer):
    """Denoising model quantizer class.

    Args:
        config (`DiffusionQuantizerConfig` or `None`):
            The quantizer configuration.
        key (`str`, *optional*, defaults to `""`):
            The key of the quantizer.
        tensor_type (`TensorType`, *optional*, defaults to `TensorType.Weights`):
            The type of the tensor to quantize.
        channels_dim (`int` or `None`, *optional*, defaults to `None`):
            The dimension of channels.
        scale (`torch.Tensor` or `Sequence[torch.Tensor]` or `None`, *optional*, defaults to `None`):
            The scale tensor.
        zero (`torch.Tensor` or `None`, *optional*, defaults to `None`):
            The zero point tensor.
        dynamic_range (`DynamicRange` or `Sequence[DynamicRange]` or `None`, *optional*, defaults to `None`):
            The dynamic range.
        range_bound (`RangeBound` or `None`, *optional*, defaults to `None`):
            The dynamic range bound.
        quant_range (`QuantRange` or `None`, *optional*, defaults to `None`):
            The quantization range.
        default_dtype (`torch.dtype` or `None`, *optional*, defaults to `None`):
            The default scale dtype
        develop_dtype (`torch.dtype`, *optional*, defaults to `torch.float32`):
            The quantization development dtype.

        kernel (`DiffusionGPTQConfig` or `None`, *optional*, defaults to `MISSING`):
            The GPTQ kernel configuration.
            If not provided (i.e., `MISSING`), the GPTQ configuration from the `config` will be used.
        low_rank (`QuantLowRankConfig` or `None`, *optional*, defaults to `MISSING`):
            The quantization low-rank branch configuration.
            If not provided (i.e., `MISSING`), the low-rank branch configuration from the `config` will be used.
        input_packager (`BaseInputPackager` or `None`, *optional*, defaults to `None`):
            The input packager, used for unpacking and repacking the input tensor(s).
        output_packager (`BaseOutputPackager` or `None`, *optional*, defaults to `None`):
            The output packager, used for unpacking and repacking the output tensor(s).
    """

    config: DiffusionQuantizerConfig
    kernel: DiffusionGPTQConfig | None = field(init=False)
    low_rank: SkipBasedQuantLowRankCalibConfig | None = field(init=False)
    tensor_type: TensorType = TensorType.Weights

    def __post_init__(self) -> None:
        self.kernel = self.config.kernel_gptq
        self.low_rank = self.config.low_rank

    def calibrate_dynamic_range(
        self,
        modules: tp.Sequence[nn.Module],
        activations: TensorsCache,
        weights: tp.Sequence[nn.Parameter] = None,
        eval_inputs: TensorsCache | None = None,
        eval_module: nn.Module | None = None,
        eval_kwargs: dict[str, tp.Any] | None = None,
        orig_weights: tp.Sequence[tuple[nn.Parameter, torch.Tensor]] | None = None,
        orig_activations: TensorsCache | None = None,
        orig_eval_inputs: TensorsCache | None = None,
    ) -> tp.Sequence[DynamicRange] | None:
        """Calibrate the dynamic range.

        Args:
            modules (`Sequence[nn.Module]`):
                The modules to calibrate.
            activations (`TensorsCache`):
                The inputs cache if the tensor type is not outputs, or the outputs cache if the tensor type is outputs.
            weights (`Sequence[nn.Parameter]` or `None`, *optional*, defaults to `None`):
                The weights to calibrate.
                If not provided, the weights of the modules will be used.
            eval_inputs (`TensorsCache` or `None`, *optional*, defaults to `None`):
                The cache of the inputs for evaluation.
                If not provided, the `activations` cache will be used.
            eval_module (`nn.Module` or `None`, *optional*, defaults to `None`):
                The module to evaluate the quantization error.
                If not provided, the module to calibrate will be used.
            eval_kwargs (`dict[str, tp.Any]` or `None`, *optional*, defaults to `None`):
                The keyword arguments for evaluation.
            orig_weights (`Sequence[tuple[nn.Parameter, torch.Tensor]]` or `None`, *optional*, defaults to `None`):
                The original weights.
            orig_activations (`TensorsCache` or `None`, *optional*, defaults to `None`):
                The original activations.
            orig_eval_inputs (`TensorsCache` or `None`, *optional*, defaults to `None`):
                The original evaluation inputs.

        Returns:
            `Sequence[DynamicRange]` or `None`:
                The dynamic ranges of each quantization step.
        """
        if (
            not self.is_enabled()
            or self.config.calib_range is None
            or not self.config.calib_range.is_enabled_for(self.key)
        ):
            self.dynamic_range = None
        else:
            self.dynamic_range = calibrate_dynamic_range(
                tensor_type=self.tensor_type,
                config=self.config.calib_range,
                static=self.config.static,
                quantizer=self,
                modules=modules,
                activations=activations,
                weights=weights,
                eval_inputs=eval_inputs,
                eval_module=eval_module,
                eval_kwargs=eval_kwargs,
                orig_weights=orig_weights,
                orig_activations=orig_activations,
                orig_eval_inputs=orig_eval_inputs,
            )
        return self.dynamic_range


@dataclass
class DiffusionWeightQuantizer(DiffusionQuantizer):
    """Diffusion model weight quantizer class.

    Args:

    Args:
        config (`DiffusionWeightQuantizerConfig` or `None`):
            The quantizer configuration.
        key (`str`, *optional*, defaults to `""`):
            The key of the quantizer.
        scale (`torch.Tensor` or `Sequence[torch.Tensor]` or `None`, *optional*, defaults to `None`):
            The scale tensor.
        zero (`torch.Tensor` or `None`, *optional*, defaults to `None`):
            The zero point tensor.
        dynamic_range (`DynamicRange` or `Sequence[DynamicRange]` or `None`, *optional*, defaults to `None`):
            The dynamic range.
        range_bound (`RangeBound` or `None`, *optional*, defaults to `None`):
            The dynamic range bound.
        quant_range (`QuantRange` or `None`, *optional*, defaults to `None`):
            The quantization range.
        default_dtype (`torch.dtype` or `None`, *optional*, defaults to `None`):
            The default scale dtype
        develop_dtype (`torch.dtype`, *optional*, defaults to `torch.float32`):
            The quantization development dtype.

        kernel (`DiffusionGPTQConfig` or `None`, *optional*, defaults to `MISSING`):
            The GPTQ kernel configuration.
            If not provided (i.e., `MISSING`), the GPTQ configuration from the `config` will be used.
        low_rank (`QuantLowRankConfig` or `None`, *optional*, defaults to `MISSING`):
            The quantization low-rank branch configuration.
            If not provided (i.e., `MISSING`), the low-rank branch configuration from the `config` will be used.
        input_packager (`BaseInputPackager` or `None`, *optional*, defaults to `None`):
            The input packager, used for unpacking and repacking the input tensor(s).
        output_packager (`BaseOutputPackager` or `None`, *optional*, defaults to `None`):
            The output packager, used for unpacking and repacking the output tensor(s).
    """

    config: DiffusionWeightQuantizerConfig
    channels_dim: None = field(init=False, default=None)
    tensor_type: TensorType = field(init=False, default=TensorType.Weights)

    def calibrate_dynamic_range(
        self,
        module: nn.Module,
        inputs: TensorsCache,
        weight: nn.Parameter | None = None,
        eval_inputs: TensorsCache | None = None,
        eval_module: nn.Module | None = None,
        eval_kwargs: dict[str, tp.Any] | None = None,
        orig_inputs: TensorsCache | None = None,
        orig_eval_inputs: TensorsCache | None = None,
    ) -> tp.Sequence[DynamicRange] | None:
        """Calibrate the dynamic range.

        Args:
            module (`nn.Module`):
                The module to calibrate.
            inputs (`TensorsCache`):
                The inputs cache.
            weight (`nn.Parameter` or `None`, *optional*, defaults to `None`):
                The weight parameter to calibrate.
                If not provided, the weight of the `module` will be used.
            eval_inputs (`TensorsCache` or `None`, *optional*, defaults to `None`):
                The cache of the inputs for evaluation.
                If not provided, the `activations` cache will be used.
            eval_module (`nn.Module` or `None`, *optional*, defaults to `None`):
                The module to evaluate the quantization error.
                If not provided, the module to calibrate will be used.
            eval_kwargs (`dict[str, tp.Any]` or `None`, *optional*, defaults to `None`):
                The keyword arguments for evaluation.
            orig_inputs (`TensorsCache` or `None`, *optional*, defaults to `None`):
                The original inputs.
            orig_eval_inputs (`TensorsCache` or `None`, *optional*, defaults to `None`):
                The original evaluation inputs.

        Returns:
            `Sequence[DynamicRange]` or `None`:
                The dynamic ranges of each quantization step.
        """
        return super().calibrate_dynamic_range(
            modules=[module],
            weights=[weight] if weight is not None else [module.weight],
            activations=inputs,
            eval_inputs=eval_inputs,
            eval_module=eval_module,
            eval_kwargs=eval_kwargs,
            orig_activations=orig_inputs,
            orig_eval_inputs=orig_eval_inputs,
        )

    def calibrate_low_rank(
        self,
        input_quantizer: "DiffusionActivationQuantizer",
        modules: tp.Sequence[nn.Module],
        inputs: TensorsCache,
        weights: tp.Sequence[nn.Parameter] = None,
        eval_inputs: TensorsCache | None = None,
        eval_module: nn.Module | None = None,
        eval_kwargs: dict[str, tp.Any] | None = None,
        orig_inputs: TensorsCache | None = None,
        orig_eval_inputs: TensorsCache | None = None,
    ) -> LowRankBranch:
        """Calibrate the quantization low-rank branch."""
        if weights is None:
            weights = [module.weight for module in modules]
        return QuantLowRankCalibrator(
            config=self.low_rank,
            w_quantizer=self,
            x_quantizer=input_quantizer,
            develop_dtype=self.develop_dtype,
        ).calibrate(
            x_wgts=weights,
            x_acts=inputs,
            x_mods=modules,
            eval_inputs=eval_inputs,
            eval_module=eval_module,
            eval_kwargs=eval_kwargs,
            orig_x_acts=orig_inputs,
            orig_eval_inputs=orig_eval_inputs,
        )


@dataclass
class DiffusionActivationQuantizer(DiffusionQuantizer):
    """Diffusion model activation quantizer class.

    Args:
        config (`DiffusionActivationQuantizerConfig` or `None`):
            The quantizer configuration.
        key (`str`, *optional*, defaults to `""`):
            The key of the quantizer.
        tensor_type (`TensorType`, *optional*, defaults to `TensorType.Inputs`):
            The type of the tensor to quantize.
        channels_dim (`int` or `None`, *optional*, defaults to `None`):
            The dimension of channels.
        scale (`torch.Tensor` or `Sequence[torch.Tensor]` or `None`, *optional*, defaults to `None`):
            The scale tensor.
        zero (`torch.Tensor` or `None`, *optional*, defaults to `None`):
            The zero point tensor.
        dynamic_range (`DynamicRange` or `Sequence[DynamicRange]` or `None`, *optional*, defaults to `None`):
            The dynamic range.
        range_bound (`RangeBound` or `None`, *optional*, defaults to `None`):
            The dynamic range bound.
        quant_range (`QuantRange` or `None`, *optional*, defaults to `None`):
            The quantization range.
        default_dtype (`torch.dtype` or `None`, *optional*, defaults to `None`):
            The default scale dtype
        develop_dtype (`torch.dtype`, *optional*, defaults to `torch.float32`):
            The quantization development dtype.

        input_packager (`BaseInputPackager` or `None`, *optional*, defaults to `None`):
            The input packager, used for unpacking and repacking the input tensor(s).
        output_packager (`BaseOutputPackager` or `None`, *optional*, defaults to `None`):
            The output packager, used for unpacking and repacking the output tensor(s).
        develop_dtype (torch.dtype, optional): The develop dtype. Defaults to ``torch.float32``.
    """

    config: DiffusionActivationQuantizerConfig
    tensor_type: TensorType = TensorType.Inputs

    def __post_init__(self) -> None:
        super().__post_init__()
        assert self.tensor_type != TensorType.Weights, "The tensor type cannot be weights."
        assert isinstance(self.channels_dim, int), "The channels dimension must be provided."
