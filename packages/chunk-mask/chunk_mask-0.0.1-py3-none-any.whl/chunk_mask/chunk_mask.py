# Copyright (c) 2025, Zhendong Peng (pzd17@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch


def pad_mask(lengths: torch.Tensor, max_length: int, device: torch.device = torch.device("cpu")) -> torch.Tensor:
    lengths = lengths.unsqueeze(1) if lengths.dim() == 1 else lengths
    indices = torch.arange(max_length, device=device)
    return indices >= lengths


def tril_mask(size: int, device: torch.device = torch.device("cpu")) -> torch.Tensor:
    return torch.tril(torch.ones(size, size, device=device), diagonal=0).bool()


def chunk_mask(
    size: int, chunk_size: int, num_left_chunks: int = -1, device: torch.device = torch.device("cpu")
) -> torch.Tensor:
    mask = torch.zeros(size, size, device=device, dtype=torch.bool)
    indices = torch.arange(size, device=device)
    start_indices = torch.clamp((indices // chunk_size - num_left_chunks) * chunk_size, min=0)
    end_indices = torch.clamp((indices // chunk_size + 1) * chunk_size, max=size)
    for i in range(size):
        mask[i, start_indices[i] : end_indices[i]] = True
    return mask
