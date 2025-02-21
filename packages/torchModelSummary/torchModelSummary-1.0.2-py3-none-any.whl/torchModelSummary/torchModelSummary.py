'''
The MIT License (MIT)

Copyright (c) <2024> <Daun Kim, Yonsei University, Seoul, Republic of Korea>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

"""torchModelStatistics.py"""

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
from torch.utils.hooks import RemovableHandle

from .layerInfo import LayerInfo, prod

'''Data Type Notation'''
LAYER_MODULES = (torch.nn.MultiheadAttention,)
INPUT_SIZE_TYPE = Sequence[Union[int, Sequence[Any], torch.Size]]
INPUT_DATA_TYPE = Optional[
    Union[torch.Tensor, torch.Size, Sequence[torch.Tensor], INPUT_SIZE_TYPE]
]
CORRECTED_INPUT_SIZE_TYPE = List[Union[Iterable[Any], torch.Size]]


'''Simple Calculating Functions'''
def to_bytes(num: int) -> float:
    """ Converts a number (assume floats, 4 bytes each) to megabytes. """
    return num * 4 / (1024 ** 2)


def to_readable(num: int) -> float:
    """ Converts a number to millions or billions. """
    if num >= 1e9:
        return num / 1e9
    return num / 1e6


'''Functions Used for Building Module Statistics Class'''
def apply_hooks(
    module: nn.Module,
    orig_model: nn.Module,
    batch_dim: Optional[int],
    depth: int,
    summary_list: List[LayerInfo],
    idx: Dict[int, int],
    hooks: Optional[List[RemovableHandle]],
    # batch_size: int = -1,
    curr_depth: int = 0,
    parent_info: Optional[LayerInfo] = None,
) -> None:
    """
    If input_data is provided, recursively adds hooks to all layers of the model.
    Else, fills summary_list with layer info without computing a
    forward pass through the network.
    """
    # Fallback is used if the layer's hook is never called, in ModuleLists, for example.
    info = LayerInfo(module, curr_depth, None, parent_info) # 전체모델(또는 a layer)을 받아 첫 layer info를 작성.

    def pre_hook(module: nn.Module, inputs: Any) -> None:
        """ Create a LayerInfo object to aggregate information about that layer. """
        del inputs # in*output을 제외한 layer에 대한 정보만을 보기 위한 forward pre hook이므로, input은 메모리 확보를 위해 삭제.
        nonlocal info # 전역 변수 info를 prehook에서도 편집할 수 있는 선언 -> pre_hook 밖에서  info(layerinfo) 변수를 사용 가능하다!
        idx[curr_depth] = idx.get(curr_depth, 0) + 1 # depth_index 작성.
        info = LayerInfo(module, curr_depth, idx[curr_depth], parent_info) # layer id tree에서 layer_info class에 들어갈 depth_index 정보가 잘못됐으니, nonlocal info 변수의 데이터를 수정해 저장.
        info.check_recursive(summary_list)
        summary_list.append(info)

    def hook(module: nn.Module, inputs: Any, outputs: Any) -> None:
        """ Update LayerInfo after forward pass. """
        del module
        info.input_size = info.calculate_size(inputs, batch_dim, )#batch_size) # hook 입장에선 info는 전역 변수이니 데이터를 가져와서 사용 가능하다.
        info.output_size = info.calculate_size(outputs, batch_dim,) #batch_size)
        info.calculate_macs()
        info.executed = True

    submodules = [m for m in module.modules() if m is not orig_model] #
    if module != orig_model or isinstance(module, LAYER_MODULES) or not submodules:
        if hooks is None: # layer info들을 작성한 적이 없을 때 == 전체 모듈이 input으로 처음 주어졌을 때,
            pre_hook(module, None)
        else: # layer info를 이미 작성한 적이 있을 때
            hooks.append(module.register_forward_pre_hook(pre_hook))
            hooks.append(module.register_forward_hook(hook))

    ## 하위 layer가 남아 있을 경우, layer_info를 recursive하게 계속해서 작성.
    if curr_depth <= depth:
        for child in module.children():
            apply_hooks(
                child,
                orig_model,
                batch_dim,
                depth,
                summary_list,
                idx,
                hooks,
                curr_depth + 1,
                info,
            )


def process_input_data(
    input_data: INPUT_DATA_TYPE,
    batch_dim: Optional[int],
    device: torch.device,
    dtypes: Optional[List[torch.dtype]],
) -> Tuple[INPUT_DATA_TYPE, CORRECTED_INPUT_SIZE_TYPE]:
    """ Create sample input data and the corrected input size. """
    if isinstance(input_data, torch.Tensor):
        input_size = get_correct_input_sizes(input_data.size())
        x = [input_data.to(device)]

    elif isinstance(input_data, (list, tuple)):
        if all(isinstance(data, torch.Tensor) for data in input_data):
            input_sizes = [
                data.size() for data in input_data  # type: ignore[union-attr]
            ]
            input_size = get_correct_input_sizes(input_sizes)
            x = set_device(input_data, device)
        else:
            if dtypes is None:
                dtypes = [torch.float] * len(input_data)
            input_size = get_correct_input_sizes(input_data)
            x = get_input_tensor(input_size, batch_dim, dtypes, device)

    else:
        raise TypeError(
            "Input type is not recognized. Please ensure input_data is valid.\n"
            "For multiple inputs to the network, ensure input_data passed in is "
            "a sequence of tensors or a list of tuple sizes. If you are having "
            "trouble here, please submit a GitHub issue."
        )

    return x, input_size


def get_input_tensor(
    input_size: CORRECTED_INPUT_SIZE_TYPE,
    batch_dim: Optional[int],
    dtypes: List[torch.dtype],
    device: torch.device,
) -> List[torch.Tensor]:
    """ Get input_tensor with batch size 2 for use in model.forward() """
    x = []
    for size, dtype in zip(input_size, dtypes):
        # add batch_size of 2 for BatchNorm
        input_tensor = torch.rand(*size)
        if batch_dim is not None:
            input_tensor = input_tensor.unsqueeze(dim=batch_dim)
            input_tensor = torch.cat([input_tensor] * 2, dim=batch_dim)
        x.append(input_tensor.to(device).type(dtype))
    return x


def get_correct_input_sizes(input_size: INPUT_SIZE_TYPE) -> CORRECTED_INPUT_SIZE_TYPE:
    """
    Convert input_size to the correct form, which is a list of tuples.
    Also handles multiple inputs to the network.
    """
    def flatten(nested_array: INPUT_SIZE_TYPE) -> Iterator[Any]:
        """ Flattens a nested array. """
        for item in nested_array:
            if isinstance(item, (list, tuple)):
                yield from flatten(item)
            else:
                yield item

    if not input_size or any(size <= 0 for size in flatten(input_size)):
        raise ValueError("Input_data is invalid, or negative size found in input_data.")

    if isinstance(input_size, list) and isinstance(input_size[0], int):
        return [tuple(input_size)]
    if isinstance(input_size, list):
        return input_size
    if isinstance(input_size, tuple) and isinstance(input_size[0], tuple):
        return list(input_size)
    return [input_size]


def set_device(data: Any, device: torch.device) -> Any:
    """ Sets device for all input types and collections of input types. """
    if torch.is_tensor(data):
        return data.to(device, non_blocking=True)

    # Recursively apply to collection items
    elem_type = type(data)
    if isinstance(data, Mapping):
        return elem_type({k: set_device(v, device) for k, v in data.items()})
    if isinstance(data, tuple) and hasattr(data, "_fields"):  # Named tuple
        return elem_type(*(set_device(d, device) for d in data))
    if isinstance(data, Iterable) and not isinstance(data, str):
        return elem_type([set_device(d, device) for d in data])
    # Data is neither a tensor nor a collection
    return data

def get_depth(model: nn.Module, depth: int = 1, current_depth: int = 1) -> int:
  '''Calculate the depth of a model'''
  for layer in model.children():
    if any(layer.children()):
      depth = get_depth(layer, depth, current_depth + 1)

  if current_depth > depth:
    return current_depth

  return depth

'''Module Statistics Class'''
class Statistics:
  def __init__(
    self,
    model: nn.Module,
    input_data: INPUT_DATA_TYPE = None,
    *args: Any,
    batch_dim: Optional[int] = 0,
    # batch_size: Optional[int] = -1,
    branching: bool = True,
    depth: Optional[int] = None,
    device: Optional[torch.device] = None,
    dtypes: Optional[List[torch.dtype]] = None,
    **kwargs: Any,
  ):
    """
    Summarize the given PyTorch model. Summarized information includes:
        1) Layer names,
        2) input/output shapes,
        3) kernel shape,
        4) # of parameters,
        5) # of operations (Mult-Adds)

    Args:
        model (nn.Module):
                PyTorch model to summarize. The model should be fully in either train()
                or eval() mode. If layers are not all in the same mode, running summary
                may have side effects on batchnorm or dropout statistics. If you
                encounter an issue with this, please open a GitHub issue.

        input_data (Sequence of Sizes or Tensors):
                Example input tensor of the model (dtypes inferred from model input).
                - OR -
                Shape of input data as a List/Tuple/torch.Size
                (dtypes must match model input, default is FloatTensors).
                You should NOT include batch size in the tuple.
                - OR -
                If input_data is not provided, no forward pass through the network is
                performed, and the provided model information is limited to layer names.
                Default: None

        batch_dim (int):
                Batch_dimension of input data. If batch_dim is None, the input data
                is assumed to contain the batch dimension.
                WARNING: in a future version, the default will change to None.
                Default: 0

        # batch_size (int):
        #         Batch_size of input data. If batch_dim is None, the input data
        #         is filled as Null sign.
        #         Default: -1

        branching (bool):
                Whether to use the branching layout for the printed output.
                Default: True

        device (torch.Device):
                Uses this torch device for model and input_data.
                If not specified, uses result of torch.cuda.is_available().
                Default: None

        dtypes (List[torch.dtype]):
                For multiple inputs, specify the size of both inputs, and
                also specify the types of each parameter here.
                Default: None

        *args, **kwargs:
                Other arguments used in `model.forward` function.

    Return:
        ModelStatistics object
                See torchsummary/model_statistics.py for more information.
    """

    """
    Attributes:
        summary_list:
                A list containing LayerInfo classes which describe an information about a layer module.
                LayerInfo = List[class(
                             # Identifying Information
                             layer_id: int, id of a layer.
                             module:nn.Module, a layer of a model.
                             class_name: class name of a layer, Conv2d, MaxPool2d ... etc.
                             inner_layers:,
                             depth: int, .
                             depth_index:,
                             executetd:,
                             parent_info:,

                             # Statistics
                             trainable: bool, check whether a layer requires a gradient so it is trainable.
                             is_recursive: bool, == is_already_on_summary_list, used when printing a number of parameters of a layer not to print it again.
                             input_size: List[int] = List(input_tensor.size()), ex. [-1, num_of_channels, height, width].
                             output_size: List[int] = List(input_tensor.size()), ex. [-1, num_of_channels, height, width].
                             kernel_size:,
                             num_params: int, number of parameters of a layer.
                             macs: int, number of MAC operations.)]

        input_size:
                A variable of CORRECTED_INPUT_SIZE_TYPE (List[Union[Iterable[Any], torch.Size]]) containing an input's size.

        total_input:
                The number of floating point in a input data

        depth (int):
                Number of nested layers to traverse (e.g. Sequentials).
                Default: 1
    """
    self.summary_list: List[LayerInfo] = [] # summary list를 저장할 list 형의 변수 생성
    self.input_size: CORRECTED_INPUT_SIZE_TYPE = [] # input size를 저장할 CORRECTED_INPUT_SIZE_TYPE 형의 변수 생성
    self.total_input: int = 0 # input_size list에 데이터가 있을 때, input data에 들어있는 fp가 몇 개인지 합산한 int 값.
    self.total_params: int = 0 # model의 total parameter 수
    self.trainable_params: int = 0 # total trainable param 수 저장 변수.
    self.total_output: float = 0
    self.total_mult_adds: int = 0 # model의 total parameter 수, total trainable param 수 저장 변수.
    self.depth: int = 1 # nested layer를 총 고려한 모델의 깊이.

    self.total_input_bytes: float = 0
    self.total_output_bytes: float = 0
    self.total_params_bytes: float = 0
    self.total_size_bytes: float = 0

    '''Initializing ModuleStatistics Class'''
    saved_model_mode = model.training # model의 train(True) or eval(False) 상태를 저장
    model.eval() # model을 eval로 변형
    hooks: Optional[List[RemovableHandle]] = None if input_data is None else [] # hook를 저장하는 변수
    idx: Dict[int, int] = {} # RemovableHandle object는 depth와 depth_index를 갖는다.

    # 모델의 깊이 계산
    self.depth = get_depth(model)

    apply_hooks(model, model, batch_dim, self.depth, self.summary_list, idx, hooks) # 아래 참조. model과 hook들을 참고 하여 model 정리.

    ## input (size)에 대한 정보가 주어지면 model의 정보를 계산해낼 수 있다.
    if input_data is not None:
        if device is None:
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        x, self.input_size = process_input_data(input_data, batch_dim, device, dtypes)
        args, kwargs = set_device(args, device), set_device(kwargs, device)

        self.total_input: int = sum(prod(sz) for sz in self.input_size) if self.input_size else 0 # input_size list에 데이터가 있을 때, input data에 들어있는 fp가 몇 개인지 합산한 int 값.

        ## forward pre hook과 forward hook으로 layer에 대한 정보(input(activation) size, output (gradient) size ... etc)
        ## 를 받아오라 등록을 했으니, 모델을 1회 돌려 해당 정보들을 뽑아낸다.
        try:
            with torch.no_grad():
                _ = model.to(device)(*x, *args, **kwargs)  # type: ignore[misc]
        ## 만약 model을 돌릴 수 없는 상황이라면, exception을 올리고, 그동안 실행한 layer들만 보여준다.
        except Exception as e:
            executed_layers = [layer for layer in self.summary_list if layer.executed]
            raise RuntimeError(
                "Failed to run modelstatistics. See above stack traces for more details. "
                "Executed layers up to: {}".format(executed_layers)
            ) from e
        ## try가 exception 발생 없이 성공했으면, model은 1회 연산 수행을 마친 것이므로, 더 이상 hook은 필요 없다.
        ## model을 원래 초기 상태로 만들기 위해 model에서 hook 제거.
        finally:
            if hooks is not None:
                for hook in hooks:
                    hook.remove()
            model.train(saved_model_mode)

    for layer_info in self.summary_list: # LayerInfo를 통해 정리한 summary_list를 받아 layerinfo class 하나씩 정보를 불러오기.
            self.total_mult_adds += layer_info.macs # calc of total num of MAC

            ## 처리하지 않은 layer일 경우,
            if not layer_info.is_recursive:
                # model의 가장 하위 구성 layer일 경우,
                if layer_info.depth == self.depth or ( # Why layer_info.depth == formatting.max_depth condition exists?
                    not any(layer_info.module.children())
                    and layer_info.depth < self.depth
                ):
                    # parameter 수를 계산해준다.
                    self.total_params += layer_info.num_params
                    if layer_info.trainable:
                        self.trainable_params += layer_info.num_params

                # parameter가 있고, 가장 하위 layer일 경우,
                # model 사용중 저장되는 activation과 gradient를 저장할 필요가 있다.
                # 따라서 각 layer의 input & output size를 저장해야 한다.
                if layer_info.num_params > 0 and not any(layer_info.module.children()):
                    # x2 for calculating activations and gradients
                    if saved_model_mode:
                      self.total_output += 2 * prod(layer_info.output_size)
                      self.total_output += layer_info.num_params
                    else:
                      self.total_output += prod(layer_info.output_size)
                    # self.total_output += 2 * prod(layer_info.output_size)

    '''layer 별 메모리 차지하는 크기 계산하기 위한 part: recursive한 놈도 일단 memory size를 계산'''
    for idx in range(self.depth, 0, -1):
      for jdx, layer_info in enumerate(self.summary_list):
        if layer_info.depth == idx:
          layer_info.input_bytes = to_bytes(sum(prod(sz) for sz in self.input_size) if layer_info.input_size else 0)

          if not any(layer_info.module.children()):
            if saved_model_mode:
              layer_info.output_bytes = to_bytes(2 * prod(layer_info.output_size))
              layer_info.output_bytes += to_bytes(layer_info.num_params)
            else:
              layer_info.output_bytes = to_bytes(prod(layer_info.output_size))
            # layer_info.output_bytes = to_bytes(2 * prod(layer_info.output_size))

            layer_info.params_bytes = to_bytes(layer_info.num_params)
            layer_info.size_bytes = layer_info.input_bytes + layer_info.output_bytes + layer_info.params_bytes

          else:
            margin = 1
            while jdx+margin < len(self.summary_list) and self.summary_list[jdx+margin].depth > idx:
              if self.summary_list[jdx+margin].depth == (idx + 1):
                layer_info.num_params += self.summary_list[jdx+margin].num_params
                layer_info.macs += self.summary_list[jdx+margin].macs

                layer_info.output_bytes += self.summary_list[jdx+margin].output_bytes
                layer_info.params_bytes += self.summary_list[jdx+margin].params_bytes
                layer_info.size_bytes += self.summary_list[jdx+margin].size_bytes
              margin += 1

        else:
          pass

    """memory size, byte로 계산"""
    self.total_input_bytes = to_bytes(self.total_input)
    self.total_output_bytes = to_bytes(self.total_output)
    self.total_params_bytes = to_bytes(self.total_params)
    self.total_size_bytes = to_bytes(self.total_input + self.total_output + self.total_params)


  def __repr__(self) -> str:
    '''Print Total Statistics of a Model'''
    col_length = max(len(str(layer_info)) for layer_info in self.summary_list)
    bold_divider = "=" * col_length
    slim_divider = "-" * col_length
    summary_str = (
        "{0}\n"
        "Total # of Params: {1:}\n"
        "Trainable Params #: {2:}\n"
        "Non Trainable Params #: {3:}\n".format(
            bold_divider,
            self.total_params,
            self.trainable_params,
            self.total_params - self.trainable_params,
        )
    )

    if self.input_size:
      summary_str += (
          "{}\n"
          "Total mult-adds ({}): {:0.2f}\n"
          "Input size (MB): {:0.2f}\n"
          "Forward/backward pass size (MB): {:0.2f}\n"
          "Params size (MB): {:0.2f}\n"
          "Estimated Total Size (MB): {:0.2f}\n".format(
              slim_divider,
              "G" if self.total_mult_adds >= 1e9 else "M",
              to_readable(self.total_mult_adds),
              self.total_input_bytes,
              self.total_output_bytes,
              self.total_params_bytes,
              self.total_size_bytes
          )
      )

    if self.summary_list:
      summary_str += bold_divider + "\n"
      index = "Layer Name (type)"
      summary_str += f"{index:>{col_length-215}}"
      summary_str += (
          "{0:>30}{1:>30}{2:>30}{3:>30}{4:>35}{5:>30}{6:>30}\n".format(
              "Input Shape",
              "Output Shape",
              "Param #",
              "Input Size (MB)",
              "Forward & Backward Size (MB)",
              "Params Size (MB)",
              "Estimated Total Size (MB)"
          )
      )

      for layer_info in self.summary_list:
        summary_str += str(layer_info)
        summary_str += "\n"

    summary_str += bold_divider
    return summary_str