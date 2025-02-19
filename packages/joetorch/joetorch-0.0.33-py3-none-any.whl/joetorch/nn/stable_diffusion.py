import torch
import torch.nn as nn
from joetorch.nn.modules import ConvResidualBlock, ConvAttentionBlock



class LargeDecoder(nn.Sequential):
    def __init__(self, in_channels: int, out_channels: int, hidden_channels: int=512):
        in_c = in_channels
        out_c = out_channels
        h_c = hidden_channels

        super().__init__(

            nn.Conv2d(in_c, in_c, kernel_size=1, padding=0),
            nn.Conv2d(in_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c),
            ConvAttentionBlock(h_c),

            # (Batch_Size, h_c, Height/8, Width/8) -> (Batch_Size, h_c, Height/8, Width/8)
            ConvResidualBlock(h_c, h_c),
            ConvResidualBlock(h_c, h_c),
            ConvResidualBlock(h_c, h_c),
            ConvResidualBlock(h_c, h_c),

            # (Batch_Size, h_c, Height/8, Width/8) -> (Batch_Size, h_c, Height/4, Width/4)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c),
            ConvResidualBlock(h_c, h_c),
            ConvResidualBlock(h_c, h_c),

            # (Batch_Size, h_c, Height/4, Width/4) -> (Batch_Size, h_c, Height/2, Width/2)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c//2),
            ConvResidualBlock(h_c//2, h_c//2),
            ConvResidualBlock(h_c//2, h_c//2),

            # (Batch_Size, h_c//2, Height/2, Width/2) -> (Batch_Size, h_c//2, Height, Width)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c//2, h_c//2, kernel_size=3, padding=1),
            ConvResidualBlock(h_c//2, h_c//4),
            ConvResidualBlock(h_c//4, h_c//4),
            ConvResidualBlock(h_c//4, h_c//4),
            nn.GroupNorm(32, h_c//4),
            nn.SiLU(),

            # (Batch_Size, h//4, Height, Width) -> (Batch_Size, out_channels, Height, Width)
            nn.Conv2d(h_c//4, out_c, kernel_size=3, padding=1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (Batch_Size, 4, Height/8, Width/8)

        x /= 0.18215

        for module in self:
            x = module(x)

        # (Batch_Size, 3, Height, Width)
        return x

class MediumDecoder(nn.Sequential):

    def __init__(self, in_channels: int, out_channels: int, hidden_channels: int=256):
        in_c = in_channels
        out_c = out_channels
        h_c = hidden_channels

        super().__init__(
            nn.Conv2d(in_c, in_c, kernel_size=1, padding=0),
            nn.Conv2d(in_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c),
            ConvAttentionBlock(h_c),

            # (Batch_Size, h_c, Height/8, Width/8) -> (Batch_Size, h_c, Height/8, Width/8)
            ConvResidualBlock(h_c, h_c),
            ConvResidualBlock(h_c, h_c),
            ConvResidualBlock(h_c, h_c),

            # (Batch_Size, h_c, Height/8, Width/8) -> (Batch_Size, h_c, Height/4, Width/4)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c),
            ConvResidualBlock(h_c, h_c),

            # (Batch_Size, h_c, Height/4, Width/4) -> (Batch_Size, h_c, Height/2, Width/2)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c//2),
            ConvResidualBlock(h_c//2, h_c//2),

            # (Batch_Size, h_c//2, Height/2, Width/2) -> (Batch_Size, h_c//2, Height, Width)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c//2, h_c//2, kernel_size=3, padding=1),
            ConvResidualBlock(h_c//2, h_c//4),
            ConvResidualBlock(h_c//4, h_c//4),
            nn.GroupNorm(32, h_c//4),
            nn.SiLU(),

            # (Batch_Size, h//4, Height, Width) -> (Batch_Size, out_channels, Height, Width)
            nn.Conv2d(h_c//4, out_c, kernel_size=3, padding=1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (Batch_Size, 4, Height/8, Width/8)

        x /= 0.18215

        for module in self:
            x = module(x)

        # (Batch_Size, 3, Height, Width)
        return x

class SmallDecoder(nn.Sequential):

    def __init__(self, in_channels: int, out_channels: int, hidden_channels: int=128):
        in_c = in_channels
        out_c = out_channels
        h_c = hidden_channels

        super().__init__(

            nn.Conv2d(in_c, in_c, kernel_size=1, padding=0),
            nn.Conv2d(in_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c),
            ConvAttentionBlock(h_c),

            # (Batch_Size, h_c, Height/8, Width/8) -> (Batch_Size, h_c, Height/8, Width/8)
            ConvResidualBlock(h_c, h_c),

            # (Batch_Size, h_c, Height/8, Width/8) -> (Batch_Size, h_c, Height/4, Width/4)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c),

            # (Batch_Size, h_c, Height/4, Width/4) -> (Batch_Size, h_c, Height/2, Width/2)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c, h_c, kernel_size=3, padding=1),
            ConvResidualBlock(h_c, h_c//2),

            # (Batch_Size, h_c//2, Height/2, Width/2) -> (Batch_Size, h_c//2, Height, Width)
            nn.Upsample(scale_factor=2),
            nn.Conv2d(h_c//2, h_c//2, kernel_size=3, padding=1),
            ConvResidualBlock(h_c//2, h_c//4),
            nn.GroupNorm(32, h_c//4),
            nn.SiLU(),

            # (Batch_Size, h//4, Height, Width) -> (Batch_Size, out_channels, Height, Width)
            nn.Conv2d(h_c//4, out_c, kernel_size=3, padding=1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (Batch_Size, 4, Height/8, Width/8)

        x /= 0.18215

        for module in self:
            x = module(x)

        # (Batch_Size, 3, Height, Width)
        return x