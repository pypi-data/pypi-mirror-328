"""Laser Image Faulting Package - A tool for detecting faults in laser images"""

from .fault_detection import detectFaults, getFrameStats, saveImage, timeTest

__all__ = ["detectFaults", "getFrameStats", "saveImage", "timeTest"]
