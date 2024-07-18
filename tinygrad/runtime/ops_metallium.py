from tinygrad.device import Allocator, Compiled, MallocAllocator, Compiler
import ctypes, tempfile, pathlib
from typing import Tuple
from tinygrad.helpers import DEBUG, cpu_time_execution
from tinygrad.renderer.cstyle import MetalliumRenderer

RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"
BLUE = "\033[94m"

class MetalliumCompiler(Compiler):
  def compile(self, src:str)->str:
    return src

class MetalliumProgram:
  def __init__(self, name, lib):
    self.name = name
    self.lib = lib

    print("MetalliumProgram ... name: ", name)
    print("MetalliumProgram ... lib: ", lib)

    self.fxn = None

  def __call__(self, *bufs, vals=(), wait=False):
    return self.fxn

class MetalliumDevice(Compiled):
  def __init__(self, device: str):
    super().__init__(device, MallocAllocator, MetalliumRenderer(), MetalliumCompiler(self), MetalliumProgram, None)
