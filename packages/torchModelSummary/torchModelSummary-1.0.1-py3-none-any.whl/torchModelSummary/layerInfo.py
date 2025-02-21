'''
The MIT License (MIT)

Copyright (c) <2024> <Daun Kim, Yonsei University, Seoul, Republic of Korea>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

"""layerInfo.py"""

from typing import (
    Any,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)
import torch
import torch.nn as nn

DETECTED_INPUT_OUTPUT_TYPES = Union[
    torch.Tensor,
    Dict[Any, torch.Tensor],
    Sequence[Any],
]

'''Functions'''
def tree_notation(depth: int) -> str:
  string = "├─" if depth == 1 else "│    " * (depth - 1) + "└─"
  return string

class LayerInfo:
    """ Class that holds information about a layer module. """

    def __init__(
        self,
        module: nn.Module,
        depth: int,
        depth_index: Optional[int] = None,
        parent_info: Optional["LayerInfo"] = None,
    ):
        # Identifying information
        self.layer_id = id(module)
        self.module = module
        self.class_name = str(module.__class__).split(".")[-1].split("'")[0]
        self.inner_layers: Dict[str, List[int]] = {}
        self.depth = depth
        self.depth_index = depth_index
        self.executed = False
        self.parent_info = parent_info

        # Statistics
        self.trainable = True
        self.is_recursive = False
        self.input_size: List[int] = []
        self.output_size: List[int] = []
        self.kernel_size: List[int] = []
        self.num_params = 0
        self.macs = 0

        self.input_bytes: float = 0  # Input size (MB)
        self.output_bytes: float = 0  # Forward/backward pass size (MB)
        self.params_bytes: float = 0  # Params size (MB)
        self.size_bytes: float = 0  # Estimated Total Size (MB)

        self.calculate_num_params()

    def __repr__(self) -> str:
        if self.depth_index is None:
            return f"{self.class_name}: {self.depth}"
        return f"{self.class_name}: {self.depth}-{self.depth_index}"

    def __str__(self) -> str:
        summary = tree_notation(self.depth)
        summary += f"{self.class_name:<{30 - len(tree_notation(self.depth))}}"

        str_out_bytes = str(self.output_bytes) if not self.is_recursive else "(recursive)"
        str_params_bytes = str(self.params_bytes) if not self.is_recursive else "(recursive)"
        str_size_bytes = str(self.size_bytes) if not self.is_recursive else "(recursive)"

        summary += (
            f"{str(self.input_size):>30}"
            f"{str(self.output_size):>30}"
            f"{str(self.num_params):>30}"
            f"{str(self.input_bytes):>30}"
            f"{str_out_bytes:>35}"
            f"{str_params_bytes:>30}"
            f"{str_size_bytes:>30}"
            )

        return summary

    @staticmethod
    def calculate_size(
        inputs: DETECTED_INPUT_OUTPUT_TYPES, batch_dim: Optional[int], #batch_size: int = -1
    ) -> List[int]:
        """ Set input_size or output_size using the model's inputs. """

        def nested_list_size(inputs: Sequence[Any]) -> List[int]:
            """ Flattens nested list size. """
            ## For list or tuple that contains input tensors as elements
            if hasattr(inputs[0], "size") and callable(inputs[0].size):
                return list(inputs[0].size())
            ## For list or tuple that contains lists or tuples containing input tensors as elements
            if isinstance(inputs, (list, tuple)):
                return nested_list_size(inputs[0])
            ## Case eventually there is no any tensor
            return []

        # pack_padded_seq and pad_packed_seq store feature into data attribute
        ## For custom dataset or variable dataset given as list or tuple that contains input tensors
        # dataset len==0이면 a tensor나 an image가 없으니, []로 "an" input tensor의 size를 return
        if isinstance(inputs, (list, tuple)) and len(inputs) == 0:
            size = []
        # dataset에 input tensor가 있을 때, input tensor의 data를 받아 tensor의 size를 구해 return
        elif isinstance(inputs, (list, tuple)) and hasattr(inputs[0], "data"):
            size = list(inputs[0].data.size())
            # single tensor의 size를 받아 왔으니, batch size가 들어갈 공간을 남겨 주는 코드
            if batch_dim is not None:
                size = size[:batch_dim] + [-1] + size[batch_dim + 1 :]

        ## For custom dataset given as dict that contains input tensors
        elif isinstance(inputs, dict):
            # TODO avoid overwriting the previous size every time?
            # key에 따라 들어있는 input tensor의 값이 다를 수 있으니, for 문으로 전체를 스캔해 size를 받아와 본다.
            for _, output in inputs.items():
                size = list(output.size())
                # single tensor의 size를 받아 왔으니, batch size가 들어갈 공간을 남겨 주는 코드
                if batch_dim is not None:
                    size = [size[:batch_dim] + [-1] + size[batch_dim + 1 :]]

        ## For dataset that is given as a single or multiple tensor(s)
        elif isinstance(inputs, torch.Tensor):
            size = list(inputs.size())
            # tensor의 size를 받아 왔으니, batch size가 들어갈 공간을 공란으로 남겨 주는 코드
            if batch_dim is not None:
                size[batch_dim] = -1

        ## For any dataset given as list or tuple that eventually contains input tensors
        elif isinstance(inputs, (list, tuple)):
            size = nested_list_size(inputs)

        ## 더이상 dataset의 size를 계산 할 수 없으니, 예외 처리.
        else:
            raise TypeError(
                "Model contains a layer with an unsupported "
                "input or output type: {}".format(inputs)
            )

        return size

    def calculate_num_params(self) -> None:
        """
        Set num_params, trainable, inner_layers, and kernel_size
        using the module's parameters.
        """
        ## self.num_params, self.trainable, self.kernel_size에 parameter 수를 저장하는 함수
        for name, param in self.module.named_parameters(): # named_parameters(): Tuple containing the name(->"weight"or"bias") and parameter(->torch.Tensor)
            self.num_params += param.nelement() # torch.Tensor.nelement() -> int: return a number of tensor elements
            self.trainable &= param.requires_grad # torch.Tensor.requires_grad: attribute of a tensor whether it has a gradient which allows training.

            ## RNN의 경우 어떤지는 모르나, CNN의 경우 name이 weight or bias로 return,
            if name == "weight": # CNN의 weight이므로, kernel size는 weight에서 구하기.
                ksize = list(param.size()) # -> [output_channels, input_channels, kernel_size_h, kernel_size_w]
                # to make [in_shape, out_shape, ksize, ksize]
                if len(ksize) > 1:
                    ksize[0], ksize[1] = ksize[1], ksize[0] # ksize -> [input_channels, output_channels, kernel_size_h, kernel_size_w]
                self.kernel_size = ksize # ksize -> [input_channels, output_channels, kernel_size_h, kernel_size_w]

            # RNN modules have inner weights such as weight_ih_l0
            elif "weight" in name:
                self.inner_layers[name] = list(param.size())

    def calculate_macs(self) -> None:
        """
        Set MACs using the module's parameters and layer's output size, which is
        used for computing number of operations for Conv layers.
        """
        ## MAC 계산을 몇 회하는 지 계산하는 함수
        for name, param in self.module.named_parameters(): # named_parameters(): Tuple containing the name(->"weight"or"bias") and parameter(->torch.Tensor)
            if name == "weight": # CNN에서 kernel size는 weight이므로, kernel size는 weight에서 구하기.
                # ignore N, C when calculate Mult-Adds in ConvNd
                if "Conv" in self.class_name: # CNN에서 kernel size는 weight이므로, kernel size는 Conv에서만 구하기.
                    self.macs += int(param.nelement() * prod(self.output_size[2:])) # MAC 횟수 == kernel_size * (각 layer별 output size_h * 각 layer별 output size_w)
                else: # Conv가 아니면 parameter 1 to 1 multiplication이므로, just 합산.
                    self.macs += param.nelement()
            # RNN modules have inner weights such as weight_ih_l0
            elif "weight" in name:
                self.macs += param.nelement()

    def check_recursive(self, summary_list: List["LayerInfo"]) -> None:
        """
        If the current module is already-used, mark as (recursive).
        Must check before adding line to the summary.
        """
        if list(self.module.named_parameters()): # -> List[Tuple(name: str, param: torch.Tensor)]
            for other_layer in summary_list: # 이미 분석한 layer는 summary_list에 추가 됨
                if self.layer_id == other_layer.layer_id: # 이미 분석한 layer의 id와 같으면 이미 분석했다는 뜻.
                    self.is_recursive = True # set recursive-check flag signal high.


## iterable elements' product
def prod(num_list: Union[Iterable[Any], torch.Size]) -> int:
    result = 1
    for num in num_list:
        result *= num
    return abs(result)