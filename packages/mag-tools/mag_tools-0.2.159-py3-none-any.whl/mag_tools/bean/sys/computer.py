import socket
from dataclasses import dataclass, field
from typing import List, Optional

from mag_tools.bean.sys.cpu import Cpu
from mag_tools.bean.sys.disk import Disk
from mag_tools.bean.sys.disk_partition import DiskPartition
from mag_tools.bean.sys.memory import Memory
from mag_tools.bean.sys.mother_board import Motherboard
from mag_tools.model.computer_type import ComputerType


@dataclass
class Computer:
    """
    计算机类
    """
    type: ComputerType
    id: Optional[str] = None
    name: Optional[str] = None
    cpu: Optional[Cpu] = None
    memory: Optional[Memory] = None
    disks: List[Disk] = field(default_factory=list)
    mother_board: Optional[Motherboard] = None
    description: Optional[str] = None

    @classmethod
    def get_info(cls):
        """
        获取当前系统的CPU、内存和磁盘信息，并返回一个Computer实例
        """
        # 获取CPU信息
        cpu = Cpu.get_info()

        # 获取内存信息
        memory = Memory.get_info()

        # 获取磁盘信息
        disks = Disk.get_info()

        #获取主板信息
        mother_board = Motherboard.get_info()

        id_ = cls.__make_id(cpu, mother_board)
        cpu.computer_id = id_
        memory.computer_id = id_
        mother_board.computer_id = id_

        for disk in disks:
            disk.computer_id = id_

        for module in memory.modules:
            module.computer_id = id_

        computer = Computer(
            id=id_,
            type=ComputerType.DESKTOP,
            name=socket.gethostname(),
            cpu=cpu,
            memory=memory,
            disks=disks,
            mother_board=mother_board
        )

        return computer

    @classmethod
    def __make_id(cls, cpu: Optional[Cpu], mother_board: Optional[Motherboard]) -> str:
        """
        返回计算机对象的ID
        """
        cpu_serial = cpu.serial_number if cpu else ""
        motherboard_serial = mother_board.serial_number if mother_board else ""

        combined_serials = f"{cpu_serial}{motherboard_serial}"
        return str(hash(combined_serials))

    def __str__(self):
        """
        返回计算机参数的字符串表示
        """
        parts = [f"Computer(type='{self.type}'"]
        for attr, value in self.__dict__.items():
            if value is not None:
                parts.append(f"{attr}='{value}'")
        parts.append(")")
        return ", ".join(parts)

    def __hash__(self):
        """
        返回计算机对象的哈希值
        """
        cpu_serial = self.cpu.serial_number if self.cpu else ""
        motherboard_serial = self.mother_board.serial_number if self.mother_board else ""
        memory_serials = "".join([module.serial_number for module in self.memory.modules]) if self.memory else ""
        disk_serials = "".join([disk.serial_number for disk in self.disks])

        combined_serials = f"{cpu_serial}{motherboard_serial}{memory_serials}{disk_serials}"
        return hash(combined_serials)