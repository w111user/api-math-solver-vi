# solvers/deepseek_solver.py - ĐÃ SỬA
from .base_solver import BaseSolver
from typing import Dict, Any
import os

class DeepSeekSolver(BaseSolver):
    """DeepSeek AI Solver"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('DEEPSEEK_API_KEY')
        
        if not self.api_key:
            raise ValueError("DeepSeek API key is required")
        
        # Lazy import
        try:
            from openai import OpenAI
            self.client = OpenAI(
                api_key=self.api_key,
                base_url="https://api.deepseek.com"
            )
            self.model = "deepseek-chat"
            self.initialized = True
        except ImportError:
            raise ImportError("Please install openai: pip install openai")
        except Exception as e:
            raise Exception(f"Failed to initialize DeepSeek: {str(e)}")
    
    def solve(self, problem: str) -> str:
        """Giải bài toán với DeepSeek"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": "Bạn là chuyên gia toán học. Hãy giải bài toán chi tiết từng bước bằng tiếng Việt. Lưu ý: viết theo định dạng kí hiệu giống notepad, không viết lệnh ra hiệu kí hiệu giống bản web."
                    },
                    {"role": "user", "content": problem}
                ],
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"❌ DeepSeek AI Error: {str(e)}\n💡 Kiểm tra API key và balance."
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "name": "DeepSeek",
            "version": "V3",
            "type": "cloud-api",
            "requires_api_key": True,
            "free_tier": True,
            "tokens_per_month": 100000
        }