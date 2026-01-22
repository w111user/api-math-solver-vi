# solvers/gemini_solver.py
from .base_solver import BaseSolver
from typing import Dict, Any
import os

class GeminiSolver(BaseSolver):
    """Gemini AI Solver - Đã cập nhật theo tài liệu chính thức Google"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError("Cần có Gemini API key. Lấy tại: https://aistudio.google.com/app/apikey [citation:6]")
        
        try:
            from google import genai
            # Khởi tạo client với API Key [citation:3]
            self.client = genai.Client(api_key=self.api_key)
            # Sử dụng model mới nhất được Google khuyến nghị [citation:1][citation:4]
            self.model = "gemini-2.5-flash"
            self.initialized = True
        except ImportError:
            raise ImportError("Vui lòng cài đặt thư viện google-genai [citation:4]")
        except Exception as e:
            raise Exception(f"Khởi tạo Gemini thất bại: {str(e)}")
    
    def solve(self, problem: str) -> str:
        """Giải bài toán với Gemini - Sử dụng cú pháp chuẩn từ Quickstart [citation:4]"""
        try:
            # Tạo prompt đơn giản, rõ ràng theo mẫu chính thức
            user_content = f"Bạn là một trợ lý toán học chuyên nghiệp. Hãy giải thích chi tiết từng bước (bằng tiếng Việt) cho bài toán sau: {problem}. Lưu ý: khi viết ra thì nhớ viết theo kí hiệu mọi người hay dùng trong đánh văn bản, vui lòng không chèn kí tự để hoàn thiện giống trên web."
            
            # Gọi API với cú pháp chính xác từ tài liệu [citation:1][citation:4]
            response = self.client.models.generate_content(
                model=self.model,
                contents=user_content
            )
            
            return response.text
            
        except Exception as e:
            return f"❌ Lỗi Gemini AI: {str(e)}"
    
    def get_info(self) -> Dict[str, Any]:
        """Thông tin về solver"""
        return {
            "name": "Google Gemini",
            "version": "2.5-flash",
            "type": "cloud-api",
            "requires_api_key": True,
            "free_tier": True,
            "docs_source": "Google AI for Developers [citation:1][citation:4]"
        }