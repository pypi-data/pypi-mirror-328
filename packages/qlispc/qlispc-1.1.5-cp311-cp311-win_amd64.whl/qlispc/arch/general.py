"""Multiple architecture support"""
from typing import Callable, NamedTuple, Optional

from ..base import ABCCompileConfigMixin, QLispCode
from ..commands import CommandList, DataMap, RawData, Result
from ..config import Config
from ..tools.dicttree import flattenDict


class Architecture(NamedTuple):
    name: str
    description: str
    assembly_code: Callable[[QLispCode, Optional[dict]], tuple[CommandList,
                                                               DataMap]]
    assembly_data: Callable[[RawData, DataMap], Result]
    config_factory: Optional[ABCCompileConfigMixin] = None
    snapshot_factory: Optional[ABCCompileConfigMixin] = None


general_architecture = Architecture(
    name='general',
    description='General architecture',
    assembly_code=lambda code, context: (
        [],
        {
            'arch': 'general'
        },
    ),
    assembly_data=lambda data, data_map: flattenDict(data),
    config_factory=Config,
    snapshot_factory=Config,
)

__regested_architectures = {}


def get_arch(name: str = 'general') -> Architecture:
    return __regested_architectures[name]


def register_arch(arch: Architecture):
    __regested_architectures[arch.name] = arch


register_arch(general_architecture)

__all__ = ['Architecture', 'get_arch', 'register_arch']
