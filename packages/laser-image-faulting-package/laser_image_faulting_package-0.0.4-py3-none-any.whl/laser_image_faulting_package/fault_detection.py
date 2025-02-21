from typing import Tuple, Union, Optional
import numpy as np
import time
import torch
from PIL import Image
from numpy.typing import NDArray

# Module-level constants with type annotations
width: int = 1080
height: int = 1440
res: Tuple[int, int] = (width, height)
pixels: int = width * height
xind: torch.Tensor = torch.arange(end=res[1], dtype=torch.float16)
yind: torch.Tensor = torch.arange(end=res[0], dtype=torch.float16).unsqueeze(0).t()

def getFrameStats(frame: NDArray) -> Tuple[float, float, float, float, float, float]:
    """
    Calculate statistical metrics for an image frame.

    Args:
        frame: Input image as a numpy array

    Returns:
        Tuple containing:
        - processing_time_ms: Time taken to process in milliseconds
        - min_val: Minimum pixel value
        - max_val: Maximum pixel value
        - mean_val: Mean pixel value
        - x_centroid: X coordinate of the centroid
        - y_centroid: Y coordinate of the centroid
    """
    timeA = time.time()

    f = torch.tensor(frame, dtype=torch.float32)

    min_val = torch.min(f).item()
    max_val = torch.max(f).item()
    mean_val = torch.mean(f).item()

    # Get centroid
    total = mean_val * pixels
    x_centroid = (f * xind).sum().item() / total
    y_centroid = (f * yind).sum().item() / total

    processing_time = (time.time() - timeA) * 1000
    return processing_time, min_val, max_val, mean_val, x_centroid, y_centroid

def detectFaults(frame1: NDArray, frame2: NDArray) -> Tuple[bool, int, float]:
    """
    Detect faults between two consecutive frames using average pooling and change detection.

    Args:
        frame1: First frame as a numpy array
        frame2: Second frame as a numpy array

    Returns:
        Tuple containing:
        - fault_detected: Boolean indicating if any fault was detected
        - fault_count: Number of detected faults
        - fault_percentage: Percentage of image area with faults
    """
    start = time.time()

    # Convert image to tensor of type float32
    f1 = torch.nn.functional.avg_pool2d(torch.tensor(frame1, dtype=torch.float32).unsqueeze(0), kernel_size=2)
    f2 = torch.nn.functional.avg_pool2d(torch.tensor(frame2, dtype=torch.float32).unsqueeze(0), kernel_size=2)

    # Gets each pixel's absolute difference between the two pooled frames
    absDiffMap = (f1-f2).abs()
    faultMapRelative = absDiffMap - f1 * 0.5 > 0
    faultMapAbsolute = absDiffMap > 6
    faultMap = faultMapRelative & faultMapAbsolute

    # Calculate fault statistics
    faultCount = faultMap.sum().item()
    faultPercentage = faultCount * 100 / faultMap.numel()
    fault = faultMap.max().item() > 0

    return fault, faultCount, faultPercentage

def saveImage(frame: NDArray) -> None:
    """
    Save an image array to disk.

    Args:
        frame: Image array to save
    """
    np.save('imagesArrays', frame)

def timeTest() -> None:
    """
    Run fault detection test on a sequence of images from the RealData directory.
    Processes pairs of consecutive images named 'lightsOff{i}.tiff'.
    """
    for i in range(9):
        print(f"Images {i} and {i+1}")

        frame1 = np.array(Image.open(f"RealData/lightsOff{i}.tiff"), dtype=np.uint16)
        frame2 = np.array(Image.open(f"RealData/lightsOff{i+1}.tiff"), dtype=np.uint16)

        fault, count, percentage = detectFaults(frame1, frame2)
        print(f"Faulted: {fault}")
        print(f"Count: {count}")
        print(f"Percentage: {percentage}")
