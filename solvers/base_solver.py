# solvers/base_solver.py
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseSolver(ABC):
    """Base class cho tất cả solvers"""
    
    @abstractmethod
    def solve(self, problem: str) -> str:
        """Giải bài toán - ABSTRACT METHOD"""
        pass
    
    @abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """Thông tin về solver - ABSTRACT METHOD"""
        pass
    
    def check_availability(self) -> bool:
        """Kiểm tra solver có khả dụng không"""
        try:
            test_result = self.solve("2+2")
            return test_result is not None
        except:
            return False