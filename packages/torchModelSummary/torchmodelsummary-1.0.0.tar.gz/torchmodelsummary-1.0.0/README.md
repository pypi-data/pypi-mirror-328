# Model-Summary-Module-for-Pytorch
A custom-renovated version of torchsummary module

## Abstract
- A pytorch model splitter, layer by layer for implementing model parallelism/pipelining
- A summarizer of pytorch model's statistics

## Introduction
### Limitation of GPU's DRAM for a huge model
![Fig 1. VGG 16’s GPU memory usage for five batches on Tesla 4](./torchModelSummary/Fig1.png)

###### Fig 1. VGG 16’s GPU memory usage for five batches on Tesla 4
###### (You could see codes of Fig 1 in appendix A. [Reference web site](https://pytorch.org/blog/understanding-gpu-memory-1/))

There are four major GPU memory usage causes when training a model - model parameters, optimizer, activation, and gradient. Model parameters and optimizer are mainly derived from layers of the model, and activation and gradient are derived from given train dataset.

When it comes to use train dataset, the memory could be saved by dividing a single train batch into multiple mini batches and giving those a number of available CUDA cores, called [Data Parallelism](https://tutorials.pytorch.kr/beginner/blitz/data_parallel_tutorial.html) or [Distributed Data Parallel](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html). Or training it with mini batches by a single CUDA hardware could be possible.

In the same way, if we are trying to train a single huge model, Model parallelism method or model pipelining is coming up with regard to commercial GPGPU and insufficient cores, unlike having a A100 or H100. From this context, a code (or module) for separating a model into several sets of layers is needed.

## Insufficient functions of torchsummary module
![Fig 2. Torchsummary module’s summary of ResNet50](./torchModelSummary/Fig2.png)

###### Fig 2. Torchsummary module’s summary of ResNet50
###### (You could see codes of Fig 2 in appendix B.)

There is a module named torchsummary, which gives information of a given model, layer by layer. But the only thing you could do by the module is printing the summary. For the purpose of model parallelism, a function to get layers as variables is necessary. Further more, the torchsummary only supports informing layer type, output shape and number of parameters. We need more, especially memory sizes for each steps.

## License
```python
'''
The MIT License (MIT)

Copyright (c) <2024> <Daun Kim, Yonsei University, Seoul, Republic of Korea>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
```

The source codes of torchModelSummary module is originally based on the torchsummary. As torchsummary follows the MIT license, torchModelSummary also follows the MIT license. You could see source codes in attached files.

## How to use
- Import the module

```python
import torch
import torch.nn as nn
import torchvision.models as models

import torchModelSummary
```

- Extract statistics of a pytorch machine learning model (ResNet152)

```python
model = models.resnet152()
statistics = torchModelSummary.Statistics(model=model, input_data=torch.rand(1, 3, 224, 224))
```

- Explanation of the class “torchModelSummary.Statistics”

```python
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
```

- print summary list of a given model

```python
print(statistics.summary_list)
```

```powershell
>>>
[Conv2d: 1-1, BatchNorm2d: 1-2, ReLU: 1-3, MaxPool2d: 1-4, Sequential: 1-5, Bottleneck: 2-1, Conv2d: 3-1, BatchNorm2d: 3-2, ReLU: 3-3, Conv2d: 3-4, BatchNorm2d: 3-5, ReLU: 3-6, Conv2d: 3-7, BatchNorm2d: 3-8, Sequential: 3-9, Conv2d: 4-1, BatchNorm2d: 4-2, ReLU: 3-10, Bottleneck: 2-2, Conv2d: 3-11, BatchNorm2d: 3-12, ReLU: 3-13, Conv2d: 3-14, BatchNorm2d: 3-15, ReLU: 3-16, Conv2d: 3-17, BatchNorm2d: 3-18, ReLU: 3-19, Bottleneck: 2-3, Conv2d: 3-20, BatchNorm2d: 3-21, ReLU: 3-22, Conv2d: 3-23, BatchNorm2d: 3-24, ReLU: 3-25, Conv2d: 3-26, BatchNorm2d: 3-27, ReLU: 3-28, Sequential: 1-6, Bottleneck: 2-4, Conv2d: 3-29, BatchNorm2d: 3-30, ReLU: 3-31, Conv2d: 3-32, BatchNorm2d: 3-33, ReLU: 3-34, Conv2d: 3-35, BatchNorm2d: 3-36, Sequential: 3-37, Conv2d: 4-3, BatchNorm2d: 4-4, ReLU: 3-38, Bottleneck: 2-5, Conv2d: 3-39, BatchNorm2d: 3-40, ReLU: 3-41, Conv2d: 3-42, BatchNorm2d: 3-43, ReLU: 3-44, Conv2d: 3-45, BatchNorm2d: 3-46, ReLU: 3-47, Bottleneck: 2-6, Conv2d: 3-48, BatchNorm2d: 3-49, ReLU: 3-50, Conv2d: 3-51, BatchNorm2d: 3-52, ReLU: 3-53, Conv2d: 3-54, BatchNorm2d: 3-55, ReLU: 3-56, Bottleneck: 2-7, Conv2d: 3-57, BatchNorm2d: 3-58, ReLU: 3-59, Conv2d: 3-60, BatchNorm2d: 3-61, ReLU: 3-62, Conv2d: 3-63, BatchNorm2d: 3-64, ReLU: 3-65, Bottleneck: 2-8, Conv2d: 3-66, BatchNorm2d: 3-67, ReLU: 3-68, Conv2d: 3-69, BatchNorm2d: 3-70, ReLU: 3-71, Conv2d: 3-72, BatchNorm2d: 3-73, ReLU: 3-74, Bottleneck: 2-9, Conv2d: 3-75, BatchNorm2d: 3-76, ReLU: 3-77, Conv2d: 3-78, BatchNorm2d: 3-79, ReLU: 3-80, Conv2d: 3-81, BatchNorm2d: 3-82, ReLU: 3-83, Bottleneck: 2-10, Conv2d: 3-84, BatchNorm2d: 3-85, ReLU: 3-86, Conv2d: 3-87, BatchNorm2d: 3-88, ReLU: 3-89, Conv2d: 3-90, BatchNorm2d: 3-91, ReLU: 3-92, Bottleneck: 2-11, Conv2d: 3-93, BatchNorm2d: 3-94, ReLU: 3-95, Conv2d: 3-96, BatchNorm2d: 3-97, ReLU: 3-98, Conv2d: 3-99, BatchNorm2d: 3-100, ReLU: 3-101, Sequential: 1-7, Bottleneck: 2-12, Conv2d: 3-102, BatchNorm2d: 3-103, ReLU: 3-104, Conv2d: 3-105, BatchNorm2d: 3-106, ReLU: 3-107, Conv2d: 3-108, BatchNorm2d: 3-109, Sequential: 3-110, Conv2d: 4-5, BatchNorm2d: 4-6, ReLU: 3-111, Bottleneck: 2-13, Conv2d: 3-112, BatchNorm2d: 3-113, ReLU: 3-114, Conv2d: 3-115, BatchNorm2d: 3-116, ReLU: 3-117, Conv2d: 3-118, BatchNorm2d: 3-119, ReLU: 3-120, Bottleneck: 2-14, Conv2d: 3-121, BatchNorm2d: 3-122, ReLU: 3-123, Conv2d: 3-124, BatchNorm2d: 3-125, ReLU: 3-126, Conv2d: 3-127, BatchNorm2d: 3-128, ReLU: 3-129, Bottleneck: 2-15, Conv2d: 3-130, BatchNorm2d: 3-131, ReLU: 3-132, Conv2d: 3-133, BatchNorm2d: 3-134, ReLU: 3-135, Conv2d: 3-136, BatchNorm2d: 3-137, ReLU: 3-138, Bottleneck: 2-16, Conv2d: 3-139, BatchNorm2d: 3-140, ReLU: 3-141, Conv2d: 3-142, BatchNorm2d: 3-143, ReLU: 3-144, Conv2d: 3-145, BatchNorm2d: 3-146, ReLU: 3-147, Bottleneck: 2-17, Conv2d: 3-148, BatchNorm2d: 3-149, ReLU: 3-150, Conv2d: 3-151, BatchNorm2d: 3-152, ReLU: 3-153, Conv2d: 3-154, BatchNorm2d: 3-155, ReLU: 3-156, Bottleneck: 2-18, Conv2d: 3-157, BatchNorm2d: 3-158, ReLU: 3-159, Conv2d: 3-160, BatchNorm2d: 3-161, ReLU: 3-162, Conv2d: 3-163, BatchNorm2d: 3-164, ReLU: 3-165, Bottleneck: 2-19, Conv2d: 3-166, BatchNorm2d: 3-167, ReLU: 3-168, Conv2d: 3-169, BatchNorm2d: 3-170, ReLU: 3-171, Conv2d: 3-172, BatchNorm2d: 3-173, ReLU: 3-174, Bottleneck: 2-20, Conv2d: 3-175, BatchNorm2d: 3-176, ReLU: 3-177, Conv2d: 3-178, BatchNorm2d: 3-179, ReLU: 3-180, Conv2d: 3-181, BatchNorm2d: 3-182, ReLU: 3-183, Bottleneck: 2-21, Conv2d: 3-184, BatchNorm2d: 3-185, ReLU: 3-186, Conv2d: 3-187, BatchNorm2d: 3-188, ReLU: 3-189, Conv2d: 3-190, BatchNorm2d: 3-191, ReLU: 3-192, Bottleneck: 2-22, Conv2d: 3-193, BatchNorm2d: 3-194, ReLU: 3-195, Conv2d: 3-196, BatchNorm2d: 3-197, ReLU: 3-198, Conv2d: 3-199, BatchNorm2d: 3-200, ReLU: 3-201, Bottleneck: 2-23, Conv2d: 3-202, BatchNorm2d: 3-203, ReLU: 3-204, Conv2d: 3-205, BatchNorm2d: 3-206, ReLU: 3-207, Conv2d: 3-208, BatchNorm2d: 3-209, ReLU: 3-210, Bottleneck: 2-24, Conv2d: 3-211, BatchNorm2d: 3-212, ReLU: 3-213, Conv2d: 3-214, BatchNorm2d: 3-215, ReLU: 3-216, Conv2d: 3-217, BatchNorm2d: 3-218, ReLU: 3-219, Bottleneck: 2-25, Conv2d: 3-220, BatchNorm2d: 3-221, ReLU: 3-222, Conv2d: 3-223, BatchNorm2d: 3-224, ReLU: 3-225, Conv2d: 3-226, BatchNorm2d: 3-227, ReLU: 3-228, Bottleneck: 2-26, Conv2d: 3-229, BatchNorm2d: 3-230, ReLU: 3-231, Conv2d: 3-232, BatchNorm2d: 3-233, ReLU: 3-234, Conv2d: 3-235, BatchNorm2d: 3-236, ReLU: 3-237, Bottleneck: 2-27, Conv2d: 3-238, BatchNorm2d: 3-239, ReLU: 3-240, Conv2d: 3-241, BatchNorm2d: 3-242, ReLU: 3-243, Conv2d: 3-244, BatchNorm2d: 3-245, ReLU: 3-246, Bottleneck: 2-28, Conv2d: 3-247, BatchNorm2d: 3-248, ReLU: 3-249, Conv2d: 3-250, BatchNorm2d: 3-251, ReLU: 3-252, Conv2d: 3-253, BatchNorm2d: 3-254, ReLU: 3-255, Bottleneck: 2-29, Conv2d: 3-256, BatchNorm2d: 3-257, ReLU: 3-258, Conv2d: 3-259, BatchNorm2d: 3-260, ReLU: 3-261, Conv2d: 3-262, BatchNorm2d: 3-263, ReLU: 3-264, Bottleneck: 2-30, Conv2d: 3-265, BatchNorm2d: 3-266, ReLU: 3-267, Conv2d: 3-268, BatchNorm2d: 3-269, ReLU: 3-270, Conv2d: 3-271, BatchNorm2d: 3-272, ReLU: 3-273, Bottleneck: 2-31, Conv2d: 3-274, BatchNorm2d: 3-275, ReLU: 3-276, Conv2d: 3-277, BatchNorm2d: 3-278, ReLU: 3-279, Conv2d: 3-280, BatchNorm2d: 3-281, ReLU: 3-282, Bottleneck: 2-32, Conv2d: 3-283, BatchNorm2d: 3-284, ReLU: 3-285, Conv2d: 3-286, BatchNorm2d: 3-287, ReLU: 3-288, Conv2d: 3-289, BatchNorm2d: 3-290, ReLU: 3-291, Bottleneck: 2-33, Conv2d: 3-292, BatchNorm2d: 3-293, ReLU: 3-294, Conv2d: 3-295, BatchNorm2d: 3-296, ReLU: 3-297, Conv2d: 3-298, BatchNorm2d: 3-299, ReLU: 3-300, Bottleneck: 2-34, Conv2d: 3-301, BatchNorm2d: 3-302, ReLU: 3-303, Conv2d: 3-304, BatchNorm2d: 3-305, ReLU: 3-306, Conv2d: 3-307, BatchNorm2d: 3-308, ReLU: 3-309, Bottleneck: 2-35, Conv2d: 3-310, BatchNorm2d: 3-311, ReLU: 3-312, Conv2d: 3-313, BatchNorm2d: 3-314, ReLU: 3-315, Conv2d: 3-316, BatchNorm2d: 3-317, ReLU: 3-318, Bottleneck: 2-36, Conv2d: 3-319, BatchNorm2d: 3-320, ReLU: 3-321, Conv2d: 3-322, BatchNorm2d: 3-323, ReLU: 3-324, Conv2d: 3-325, BatchNorm2d: 3-326, ReLU: 3-327, Bottleneck: 2-37, Conv2d: 3-328, BatchNorm2d: 3-329, ReLU: 3-330, Conv2d: 3-331, BatchNorm2d: 3-332, ReLU: 3-333, Conv2d: 3-334, BatchNorm2d: 3-335, ReLU: 3-336, Bottleneck: 2-38, Conv2d: 3-337, BatchNorm2d: 3-338, ReLU: 3-339, Conv2d: 3-340, BatchNorm2d: 3-341, ReLU: 3-342, Conv2d: 3-343, BatchNorm2d: 3-344, ReLU: 3-345, Bottleneck: 2-39, Conv2d: 3-346, BatchNorm2d: 3-347, ReLU: 3-348, Conv2d: 3-349, BatchNorm2d: 3-350, ReLU: 3-351, Conv2d: 3-352, BatchNorm2d: 3-353, ReLU: 3-354, Bottleneck: 2-40, Conv2d: 3-355, BatchNorm2d: 3-356, ReLU: 3-357, Conv2d: 3-358, BatchNorm2d: 3-359, ReLU: 3-360, Conv2d: 3-361, BatchNorm2d: 3-362, ReLU: 3-363, Bottleneck: 2-41, Conv2d: 3-364, BatchNorm2d: 3-365, ReLU: 3-366, Conv2d: 3-367, BatchNorm2d: 3-368, ReLU: 3-369, Conv2d: 3-370, BatchNorm2d: 3-371, ReLU: 3-372, Bottleneck: 2-42, Conv2d: 3-373, BatchNorm2d: 3-374, ReLU: 3-375, Conv2d: 3-376, BatchNorm2d: 3-377, ReLU: 3-378, Conv2d: 3-379, BatchNorm2d: 3-380, ReLU: 3-381, Bottleneck: 2-43, Conv2d: 3-382, BatchNorm2d: 3-383, ReLU: 3-384, Conv2d: 3-385, BatchNorm2d: 3-386, ReLU: 3-387, Conv2d: 3-388, BatchNorm2d: 3-389, ReLU: 3-390, Bottleneck: 2-44, Conv2d: 3-391, BatchNorm2d: 3-392, ReLU: 3-393, Conv2d: 3-394, BatchNorm2d: 3-395, ReLU: 3-396, Conv2d: 3-397, BatchNorm2d: 3-398, ReLU: 3-399, Bottleneck: 2-45, Conv2d: 3-400, BatchNorm2d: 3-401, ReLU: 3-402, Conv2d: 3-403, BatchNorm2d: 3-404, ReLU: 3-405, Conv2d: 3-406, BatchNorm2d: 3-407, ReLU: 3-408, Bottleneck: 2-46, Conv2d: 3-409, BatchNorm2d: 3-410, ReLU: 3-411, Conv2d: 3-412, BatchNorm2d: 3-413, ReLU: 3-414, Conv2d: 3-415, BatchNorm2d: 3-416, ReLU: 3-417, Bottleneck: 2-47, Conv2d: 3-418, BatchNorm2d: 3-419, ReLU: 3-420, Conv2d: 3-421, BatchNorm2d: 3-422, ReLU: 3-423, Conv2d: 3-424, BatchNorm2d: 3-425, ReLU: 3-426, Sequential: 1-8, Bottleneck: 2-48, Conv2d: 3-427, BatchNorm2d: 3-428, ReLU: 3-429, Conv2d: 3-430, BatchNorm2d: 3-431, ReLU: 3-432, Conv2d: 3-433, BatchNorm2d: 3-434, Sequential: 3-435, Conv2d: 4-7, BatchNorm2d: 4-8, ReLU: 3-436, Bottleneck: 2-49, Conv2d: 3-437, BatchNorm2d: 3-438, ReLU: 3-439, Conv2d: 3-440, BatchNorm2d: 3-441, ReLU: 3-442, Conv2d: 3-443, BatchNorm2d: 3-444, ReLU: 3-445, Bottleneck: 2-50, Conv2d: 3-446, BatchNorm2d: 3-447, ReLU: 3-448, Conv2d: 3-449, BatchNorm2d: 3-450, ReLU: 3-451, Conv2d: 3-452, BatchNorm2d: 3-453, ReLU: 3-454, AdaptiveAvgPool2d: 1-9, Linear: 1-10]
```

- print statistics of a given model

```python
print(statistics)
```

```powershell
>>>
=====================================================================================================================================================================================================================================================
Total # of Params: 60192808
Trainable Params #: 60192808
Non Trainable Params #: 0
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total mult-adds (G): 11.63
Input size (MB): 0.57
Forward/backward pass size (MB): 573.77
Params size (MB): 229.62
Estimated Total Size (MB): 803.96
=====================================================================================================================================================================================================================================================
             Layer Name (type)                   Input Shape                  Output Shape                       Param #               Input Size (MB)       Forward & Backward Size (MB)              Params Size (MB)     Estimated Total Size (MB)
├─Conv2d                                   [-1, 3, 224, 224]            [-1, 64, 112, 112]                          9408                    0.57421875                     6.160888671875                0.035888671875                 6.77099609375
├─BatchNorm2d                             [-1, 64, 112, 112]            [-1, 64, 112, 112]                           128                    0.57421875                      6.12548828125                 0.00048828125                  6.7001953125
├─ReLU                                    [-1, 64, 112, 112]            [-1, 64, 112, 112]                             0                    0.57421875                              6.125                           0.0                    6.69921875
├─MaxPool2d                               [-1, 64, 112, 112]              [-1, 64, 56, 56]                             0                    0.57421875                            1.53125                           0.0                    2.10546875
├─Sequential                                [-1, 64, 56, 56]             [-1, 256, 56, 56]                        664320                    0.57421875                      95.7607421875                  0.8232421875                 113.236328125
│    └─Bottleneck                           [-1, 64, 56, 56]             [-1, 256, 56, 56]                        166912                    0.57421875                      40.0986328125                  0.2861328125                  46.701171875
│    │    └─Conv2d                          [-1, 64, 56, 56]              [-1, 64, 56, 56]                          4096                    0.57421875                           1.546875                      0.015625                    2.13671875
│    │    └─BatchNorm2d                     [-1, 64, 56, 56]              [-1, 64, 56, 56]                           128                    0.57421875                      1.53173828125                 0.00048828125                  2.1064453125
│    │    └─ReLU                            [-1, 64, 56, 56]              [-1, 64, 56, 56]                             0                    0.57421875                            1.53125                           0.0                    2.10546875
│    │    └─Conv2d                          [-1, 64, 56, 56]              [-1, 64, 56, 56]                         36864                    0.57421875                           1.671875                      0.140625                    2.38671875
│    │    └─BatchNorm2d                     [-1, 64, 56, 56]              [-1, 64, 56, 56]                           128                    0.57421875                      1.53173828125                 0.00048828125                  2.1064453125
│    │    └─ReLU                            [-1, 64, 56, 56]              [-1, 64, 56, 56]                             0                    0.57421875                            1.53125                           0.0                    2.10546875
│    │    └─Conv2d                          [-1, 64, 56, 56]             [-1, 256, 56, 56]                         16384                    0.57421875                             6.1875                        0.0625                    6.82421875
│    │    └─BatchNorm2d                    [-1, 256, 56, 56]             [-1, 256, 56, 56]                           512                    0.57421875                        6.126953125                   0.001953125                      6.703125
│    │    └─Sequential                      [-1, 64, 56, 56]             [-1, 256, 56, 56]                         33792                    0.57421875                       12.314453125                   0.064453125                   13.52734375
│    │    │    └─Conv2d                     [-1, 64, 56, 56]             [-1, 256, 56, 56]                         16384                    0.57421875                             6.1875                        0.0625                    6.82421875
│    │    │    └─BatchNorm2d               [-1, 256, 56, 56]             [-1, 256, 56, 56]                           512                    0.57421875                        6.126953125                   0.001953125                      6.703125
│    │    └─ReLU                           [-1, 256, 56, 56]             [-1, 256, 56, 56]                             0                    0.57421875                              6.125                           0.0                    6.69921875
│    └─Bottleneck                          [-1, 256, 56, 56]             [-1, 256, 56, 56]                        140800                    0.57421875                      27.8310546875                  0.2685546875                  33.267578125
│    │    └─Conv2d                         [-1, 256, 56, 56]              [-1, 64, 56, 56]                         16384                    0.57421875                            1.59375                        0.0625                    2.23046875
│    │    └─BatchNorm2d                     [-1, 64, 56, 56]              [-1, 64, 56, 56]                           128                    0.57421875                      1.53173828125                 0.00048828125                  2.1064453125
│    │    └─ReLU                            [-1, 64, 56, 56]              [-1, 64, 56, 56]                             0                    0.57421875                            1.53125                           0.0                    2.10546875
│    │    └─Conv2d                          [-1, 64, 56, 56]              [-1, 64, 56, 56]                         36864                    0.57421875                           1.671875                      0.140625                    2.38671875
│    │    └─BatchNorm2d                     [-1, 64, 56, 56]              [-1, 64, 56, 56]                           128                    0.57421875                      1.53173828125                 0.00048828125                  2.1064453125
│    │    └─ReLU                            [-1, 64, 56, 56]              [-1, 64, 56, 56]                             0                    0.57421875                            1.53125                           0.0                    2.10546875
│    │    └─Conv2d                          [-1, 64, 56, 56]             [-1, 256, 56, 56]                         16384                    0.57421875                             6.1875                        0.0625                    6.82421875
│    │    └─BatchNorm2d                    [-1, 256, 56, 56]             [-1, 256, 56, 56]                           512                    0.57421875                        6.126953125                   0.001953125                      6.703125
│    │    └─ReLU                           [-1, 256, 56, 56]             [-1, 256, 56, 56]                             0                    0.57421875                              6.125                           0.0                    6.69921875
│    └─Bottleneck                          [-1, 256, 56, 56]             [-1, 256, 56, 56]                        140800                    0.57421875                      27.8310546875                  0.2685546875                  33.267578125
│    │    └─Conv2d                         [-1, 256, 56, 56]              [-1, 64, 56, 56]                         16384                    0.57421875                            1.59375                        0.0625                    2.23046875
│    │    └─BatchNorm2d                     [-1, 64, 56, 56]              [-1, 64, 56, 56]                           128                    0.57421875                      1.53173828125                 0.00048828125                  2.1064453125
│    │    └─ReLU                            [-1, 64, 56, 56]              [-1, 64, 56, 56]                             0                    0.57421875                            1.53125                           0.0                    2.10546875
│    │    └─Conv2d                          [-1, 64, 56, 56]              [-1, 64, 56, 56]                         36864                    0.57421875                           1.671875                      0.140625                    2.38671875
│    │    └─BatchNorm2d                     [-1, 64, 56, 56]              [-1, 64, 56, 56]                           128                    0.57421875                      1.53173828125                 0.00048828125                  2.1064453125
│    │    └─ReLU                            [-1, 64, 56, 56]              [-1, 64, 56, 56]                             0                    0.57421875                            1.53125                           0.0                    2.10546875
│    │    └─Conv2d                          [-1, 64, 56, 56]             [-1, 256, 56, 56]                         16384                    0.57421875                             6.1875                        0.0625                    6.82421875
│    │    └─BatchNorm2d                    [-1, 256, 56, 56]             [-1, 256, 56, 56]                           512                    0.57421875                        6.126953125                   0.001953125                      6.703125
│    │    └─ReLU                           [-1, 256, 56, 56]             [-1, 256, 56, 56]                             0                    0.57421875                              6.125                           0.0                    6.69921875
...
 
...
├─AdaptiveAvgPool2d                         [-1, 2048, 7, 7]              [-1, 2048, 1, 1]                             0                    0.57421875                           0.015625                           0.0                    0.58984375
├─Linear                                          [-1, 2048]                    [-1, 1000]                       2049000                    0.57421875                  7.823944091796875             7.816314697265625              16.2144775390625
=====================================================================================================================================================================================================================================================
```

- Get a single layer from modelSummary.Statistics class and its attributes

```python
idx = 4
print(statistics.summary_list[idx])
print(statistics.summary_list[idx].layer_id)
print(statistics.summary_list[idx].module)
print(statistics.summary_list[idx].class_name)
print(statistics.summary_list[idx].inner_layers)
print(statistics.summary_list[idx].depth)
print(statistics.summary_list[idx].depth_index)
print(statistics.summary_list[idx].executed)
print(statistics.summary_list[idx].parent_info)
print(statistics.summary_list[idx].trainable)
print(statistics.summary_list[idx].is_recursive)
print(statistics.summary_list[idx].input_size)
print(statistics.summary_list[idx].output_size)
print(statistics.summary_list[idx].kernel_size)
print(statistics.summary_list[idx].num_params)
print(statistics.summary_list[idx].macs)

print()
print(statistics.summary_list[idx].input_bytes)
print(statistics.summary_list[idx].output_bytes)
print(statistics.summary_list[idx].num_params)
print(statistics.summary_list[idx].params_bytes)
print(statistics.summary_list[idx].size_bytes)
```

```powershell
>>>
├─Sequential                                [-1, 64, 56, 56]             [-1, 256, 56, 56]                        664320                    0.57421875                            94.9375                  0.8232421875                112.4130859375
134376304085456
Sequential(
  (0): Bottleneck(
    (conv1): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
    (bn1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (conv2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
    (bn2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (conv3): Conv2d(64, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
    (bn3): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (relu): ReLU(inplace=True)
    (downsample): Sequential(
      (0): Conv2d(64, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (1): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (1): Bottleneck(
    (conv1): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
    (bn1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (conv2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
    (bn2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (conv3): Conv2d(64, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
    (bn3): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (relu): ReLU(inplace=True)
  )
  (2): Bottleneck(
    (conv1): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
    (bn1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (conv2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
    (bn2): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (conv3): Conv2d(64, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
    (bn3): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (relu): ReLU(inplace=True)
  )
)
Sequential
{'0.conv1.weight': [64, 64, 1, 1], '0.bn1.weight': [64], '0.conv2.weight': [64, 64, 3, 3], '0.bn2.weight': [64], '0.conv3.weight': [256, 64, 1, 1], '0.bn3.weight': [256], '0.downsample.0.weight': [256, 64, 1, 1], '0.downsample.1.weight': [256], '1.conv1.weight': [64, 256, 1, 1], '1.bn1.weight': [64], '1.conv2.weight': [64, 64, 3, 3], '1.bn2.weight': [64], '1.conv3.weight': [256, 64, 1, 1], '1.bn3.weight': [256], '2.conv1.weight': [64, 256, 1, 1], '2.bn1.weight': [64], '2.conv2.weight': [64, 64, 3, 3], '2.bn2.weight': [64], '2.conv3.weight': [256, 64, 1, 1], '2.bn3.weight': [256]}
1
5
True
└─ResNet                                                  []                            []                      25557032                             0                                  0                             0                             0
True
False
[-1, 64, 56, 56]
[-1, 256, 56, 56]
[]
664320
668389760

0.57421875
94.9375
664320
0.8232421875
112.4130859375
```

## Appendix A.
```python
# (c) Meta Platforms, Inc. and affiliates.
import logging
import socket
from datetime import datetime, timedelta

import torch

from torch.autograd.profiler import record_function
from torchvision import models

## ref of logging module: https://cuorej.tistory.com/entry/python-logging-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-%EB%94%94%EB%B2%84%EA%B9%85-%EA%B8%B0%EC%B4%88%ED%8E%B8
                        # https://docs.python.org/ko/3/howto/logging.html
# logging 기본 설정 함수
logging.basicConfig(
   format="%(levelname)s:%(asctime)s %(message)s", # 로그의 포맷 설정. 설정 안하면 기본 형태 %(levelname):root:%(message)  / ref: https://docs.python.org/ko/3.9/library/logging.html#logrecord-attributes
   level=logging.INFO, # log를 띄울 level 설정(logging.debug, logging.DEBUG, logging.info, logging.INFO, logging.warning, logging.WARNING, logging.error, logging.ERROR, logging.critical, logging.CRITICAL)
   datefmt="%Y-%m-%d %H:%M:%S", # %(asctime)에 띄울 시간 형식 설정.
)
logger: logging.Logger = logging.getLogger(__name__) # : logging.Logger -> logging 변수의 type annotation,
                                                     # = logging.getLogger(__name__) -> logging.getLogger(__name__) function retrieves a logger instance associated with the current module's name (__name__), logging을 사용하는 모듈 이름을 가져와 이름으로 쓰는 logger 생성.
logger.setLevel(level=logging.INFO) # 로그의 출력 기준 설정, basicConfig에서도 설정 가능.

TIME_FORMAT_STR: str = "%b_%d_%H_%M_%S" # datetime class format code 설명: %b(month in character), %d(day), %H(hour), %M(minute), %S(second)

def trace_handler(prof: torch.profiler.profile):
   # Prefix for file names.
   host_name = socket.gethostname() # host의 이름을 가져오는 함수.
   timestamp = datetime.now().strftime(TIME_FORMAT_STR) # strftime: %의 format code에 맞는 시간 값을 문자열로 바꾸는 코드.
   file_prefix = f"{host_name}_{timestamp}" # f-string: 기존 "".format()을 대체하기 위한 python 문자열, ref: https://m.blog.naver.com/youji4ever/222429288222

## ref of torch.profiler: https://jh-bk.tistory.com/20
                        # https://pytorch.org/docs/stable/profiler.html
                        # https://tutorials.pytorch.kr/recipes/recipes/profiler_recipe.html
   # Construct the trace file.
   prof.export_chrome_trace(f"{file_prefix}.json.gz") # Exports the collected trace in Chrome JSON format.

   # Construct the memory timeline file.
   prof.export_memory_timeline(f"{file_prefix}.html", device=("cuda:0" if torch.cuda.is_available() else "cpu")) # Export memory event information from the profiler collected tree for a given device,
                                                                       #and export a timeline plot.
                                                                       # There are 3 exportable files using export_memory_timeline, each controlled by the path’s suffix.

def run_resnet50(num_iters=5, device=("cuda:0" if torch.cuda.is_available() else "cpu")):
   model = models.vgg16().to(device=device)
   inputs = torch.randn(5, 3, 224, 224, device=device)
   labels = torch.rand_like(model(inputs))
   optimizer = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
   loss_fn = torch.nn.CrossEntropyLoss()

   with torch.profiler.profile(
       activities=[ # 프로파일링할 device를 지정
           torch.profiler.ProfilerActivity.CPU, # CPU를 profiling
           torch.profiler.ProfilerActivity.CUDA, # GPU를 profiling
       ],
       schedule=torch.profiler.schedule(wait=0, warmup=1, active=6, repeat=1), # specifies a function that takes an integer argument (step number) as an input and returns an action for the profiler, the best way to use this parameter is to use torch.profiler.schedule helper function that can generate a schedule for you;
       record_shapes=True, # operand(input)의 shape을 기록할지 여부
       profile_memory=True, # 모델의 tensor들이 소비하는 memory 양 기록 유무
       with_stack=True, # record source information (file and line number) for the ops
       on_trace_ready=trace_handler, # specifies a function that takes a reference to the profiler as an input and is called by the profiler each time the new trace is ready.
   ) as prof:
       for _ in range(num_iters):
           prof.step()
           with record_function("## forward ##"): # torch(.autograd).profiler.record_function: torch(.autograd).profiler.profile이 구간을 나누어 따로 성능을 기록하도록 도와주는 function
               pred = model(inputs)

           with record_function("## backward ##"):
               loss_fn(pred, labels).backward()

           with record_function("## optimizer ##"):
               optimizer.step()
               optimizer.zero_grad(set_to_none=True)

if __name__ == "__main__":
    # Warm up
    run_resnet50()
    # Run the resnet50 model
    run_resnet50()
```

## Appendix B.
```python
import torch
import torch.nn as nn
import torchvision
import torchvision.models as models
import torchvision.transforms as transforms
import torchvision.datasets as dsets

import inspect
from torchsummary import summary
resnet50 = models.resnet50()#.cuda()

# How to visualize backward / ref: https://discuss.pytorch.org/t/how-to-visualize-backward-and-perhaps-doublebackward-pass-of-variable/108456/4
# understanding backward / ref: https://linlinzhao.com/tech/2017/10/24/understanding-backward()-in-PyTorch.html

# print(VGG16)
# print(VGG16.features)
# print(VGG16.state_dict())
# print(VGG16.forward)
# print(inspect.getsource(VGG16.forward))
# print(torch.jit.script(VGG16).code)
sum = summary(model=resnet50, input_size=(3, 224, 224), batch_size=1) # 실제 값과 다르다.
print(sum)
```
