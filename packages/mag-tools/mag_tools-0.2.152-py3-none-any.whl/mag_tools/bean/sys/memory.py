from dataclasses import dataclass, field
from typing import List, Optional

import psutil

from mag_tools.bean.sys.memory_module import MemoryModule


@dataclass
class Memory:
    """
    内存参数类
    """
    computer_id: Optional[str] = None       # 所属计算机的标识
    total_capacity: Optional[int] = None    # 总容量（单位：GB）
    available_capacity: Optional[int] = None    # 可用内存（单位：GB）
    used_capacity: Optional[int] = None     # 使用内存（单位：GB）
    free_capacity: Optional[int] = None     # 空闲内存（单位：GB）
    cache: Optional[int] = None     # 缓存大小（单位：GB）
    buffer_size: Optional[int] = None   # 缓冲区大小（单位：GB）
    modules: List[MemoryModule] = field(default_factory=list)

    @classmethod
    def get_info(cls):
        """
        获取当前系统的内存信息，并返回一个Memory实例
        """
        # 使用psutil获取内存使用情况
        memory_info = psutil.virtual_memory()
        modules = MemoryModule.get_modules()

        return Memory(
            total_capacity=memory_info.total // (1024 ** 3),  # 将字节转换为GB
            available_capacity=memory_info.available // (1024 ** 3),  # 将字节转换为GB
            used_capacity=memory_info.used // (1024 ** 3),  # 将字节转换为GB
            free_capacity=memory_info.free // (1024 ** 3),  # 将字节转换为GB
            modules=modules
        )

    def __str__(self):
        """
        返回内存参数的字符串表示
        """
        module_info = "\n".join(str(module) for module in self.modules)
        return (f"Memory(total_capacity={self.total_capacity} GB, available_capacity={self.available_capacity} GB, " 
                f"used_capacity={self.used_capacity} GB, free_capacity={self.free_capacity} GB, " 
                f"cache={self.cache} MB, buffer_size={self.buffer_size} MB)\nModules:\n{module_info}")