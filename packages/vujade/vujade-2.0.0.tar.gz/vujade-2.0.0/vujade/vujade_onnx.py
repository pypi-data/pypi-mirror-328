"""
Developer: vujadeyoon
Email: vujadeyoon@gmail.com
Github: https://github.com/vujadeyoon/vujade

Title: vujade_onnx.py
Description: A module for ONNX
"""


import torch
import onnx
import onnxruntime
import numpy as np
from typing import Optional, Tuple, Union
from onnxsim import simplify
from vujade import vujade_path as path_
from vujade.vujade_debug import printd


class ONNX(object):
    def __init__(self, _spath_onnx: str) -> None:
        super(ONNX, self).__init__()
        self.spath_onnx = _spath_onnx
        self.ort_session = onnxruntime.InferenceSession(self.spath_onnx)

    def run(self, _ndarr_input: np.ndarray) -> list:
        ort_inputs = {self.ort_session.get_inputs()[0].name: _ndarr_input}
        ort_outputs = self.ort_session.run(None, ort_inputs)
        return ort_outputs

    @classmethod
    def save(cls, _model_onnx: onnx.onnx_ml_pb2.ModelProto, _spath_onnx: str, _kwargs_simplify: Optional[dict] = None) -> None:
        if (_kwargs_simplify is not None) and (isinstance(_kwargs_simplify, (dict, )) is True):
            _model_onnx = cls.simplify(_model_onnx=_model_onnx, _kwargs_simplify=_kwargs_simplify)
        onnx.save(_model_onnx, _spath_onnx)

    @staticmethod
    def load(_spath_onnx: str) -> onnx.onnx_ml_pb2.ModelProto:
        model_onnx = onnx.load(_spath_onnx)
        onnx.checker.check_model(model_onnx)
        return model_onnx

    @classmethod
    def print_node_name(cls, _spath_onnx: str) -> None:
        model_onnx = cls.load(_spath_onnx=_spath_onnx)
        printd('Input nodes: {}'.format([_node.name for _node in model_onnx.graph.input]), _is_pause=False)
        printd('Output nodes: {}'.format([_node.name for _node in model_onnx.graph.output]), _is_pause=False)


    @staticmethod
    def simplify(_model_onnx: onnx.onnx_ml_pb2.ModelProto, _kwargs_simplify: dict) -> onnx.onnx_ml_pb2.ModelProto:
        model_onnx_simp, is_success = simplify(
            _model_onnx,
            **_kwargs_simplify
        )
        if is_success is False:
            raise BufferError('The conversion for simplifying ONNX is failed.')
        return model_onnx_simp

    @classmethod
    def pytorch2onnx(
            cls,
            _model,                                           # model being run
            _tensor_inputs: Tuple[torch.Tensor],              # model input (or a tuple for multiple inputs)
            _spath_onnx: str,                                 # where to save the model (can be a file or file-like object)
            _is_export_params: bool = True,                   # store the trained parameter weights inside the model file
            _opset_version: int = 10,                         # the ONNX version to export the model to
            _is_do_constant_folding: bool = True,             # whether to execute constant folding for optimization
            _input_names: Union[list, tuple] = ('input', ),   # the model's input names
            _output_names: Union[list, tuple] = ('output', ), # the model's output names
            _dynamic_axes: Optional[dict] = None,             # variable length axes
            _kwargs_simplify: Optional[dict] = None
    ) -> None:
        path_onnx = path_.Path(_spath_onnx)

        if isinstance(_input_names, tuple):
            _input_names = list(_input_names)
        if isinstance(_output_names, tuple):
            _output_names = list(_output_names)

        torch.onnx.export(
            _model,
            _tensor_inputs,
            _spath_onnx,
            export_params=_is_export_params,
            opset_version=_opset_version,
            do_constant_folding=_is_do_constant_folding,
            input_names=_input_names,
            output_names=_output_names,
            dynamic_axes=_dynamic_axes
        )

        if (_kwargs_simplify is not None) and (isinstance(_kwargs_simplify, (dict, )) is True) and (path_onnx.path.is_file()):
            cls.save(_model_onnx=cls.load(_spath_onnx=_spath_onnx), _spath_onnx=_spath_onnx, _kwargs_simplify=_kwargs_simplify)

    @classmethod
    def get_skipped_optimizers(cls) -> tuple:
        return (
            'adjust_add'
            'adjust_slice_and_matmul',
            'eliminate_consecutive_idempotent_ops',
            'eliminate_deadend',
            'eliminate_duplicate_initializer',
            'eliminate_identity',
            'eliminate_if_with_const_cond',
            'eliminate_nop_cast',
            'eliminate_nop_concat',
            'eliminate_nop_dropout',
            'eliminate_nop_expand',
            'eliminate_nop_flatten',
            'eliminate_nop_monotone_argmax',
            'eliminate_nop_pad',
            'eliminate_nop_reshape',
            'eliminate_nop_split',
            'eliminate_nop_transpose',
            'eliminate_shape_gather',
            'eliminate_shape_op',
            'eliminate_slice_after_shape',
            'eliminate_unused_initializer',
            'extract_constant_to_initializer',
            'fuse_add_bias_into_conv',
            'fuse_bn_into_conv',
            'fuse_concat_into_reshape',
            'fuse_consecutive_concats',
            'fuse_consecutive_log_softmax',
            'fuse_consecutive_reduce_unsqueeze',
            'fuse_consecutive_squeezes',
            'fuse_consecutive_transposes',
            'fuse_matmul_add_bias_into_gemm',
            'fuse_pad_into_conv',
            'fuse_pad_into_pool',
            'fuse_transpose_into_gemm',
            'lift_lexical_references',
            'nop',
            'rename_input_output',
            'replace_einsum_with_matmul',
            'set_unique_name_for_nodes',
            'split',
            'fuse_consecutive_slices',
            'eliminate_common_subexpression',
            'fuse_qkv',
            'fuse_consecutive_unsqueezes',
            'eliminate_nop_with_unit',
            'rewrite_input_dtype',
        )
