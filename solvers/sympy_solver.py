# solvers/sympy_solver.py
from .base_solver import BaseSolver
from typing import Dict, Any
import sympy as sp
import re
import math
print("có thể sẽ có 1 chút lỗi, mong mấy chế thông cảm")
class SymPySolver(BaseSolver):
    """Local SymPy Solver - Không cần API"""
    
    def __init__(self):
        self.initialized = True
    
    def solve(self, problem: str) -> str:
        """Giải bài toán offline với SymPy"""
        try:
            problem_lower = problem.lower()
            
            # 1. PHƯƠNG TRÌNH
            if '=' in problem and any(var in problem for var in ['x', 'y', 'z']):
                return self._solve_equation(problem)
            
            # 2. TÍNH TOÁN
            elif any(op in problem for op in ['+', '-', '*', '/', '^']):
                return self._calculate_expression(problem)
            
            # 3. ĐẠO HÀM
            elif 'đạo hàm' in problem_lower:
                return self._solve_derivative(problem)
            
            # 4. TÍCH PHÂN
            elif 'tích phân' in problem_lower:
                return self._solve_integral(problem)
            
            # 5. HÌNH HỌC
            elif any(word in problem_lower for word in ['diện tích', 'chu vi', 'hình tròn', 'hình vuông']):
                return self._solve_geometry(problem)
            
            # Mặc định
            else:
                return self._general_solution(problem)
                
        except Exception as e:
            return f"❌ SymPy Error: {str(e)}\n💡 Hãy nhập bài toán rõ ràng hơn."
    
    def _solve_equation(self, problem: str) -> str:
        """Giải phương trình"""
        try:
            # Trích xuất
            parts = problem.split('=')
            if len(parts) != 2:
                return "❌ Phương trình không hợp lệ. Cần dạng: f(x) = g(x)"
            
            x = sp.symbols('x')
            
            # Chuyển đổi
            lhs = self._safe_sympify(parts[0])
            rhs = self._safe_sympify(parts[1])
            
            # Giải
            eq = sp.Eq(lhs, rhs)
            solutions = sp.solve(eq, x)
            
            result = f"📝 **Phương trình:** {problem}\n\n"
            result += f"📊 **Dạng chuẩn:** {eq}\n\n"
            result += f"✅ **Nghiệm:**\n"
            
            for i, sol in enumerate(solutions, 1):
                result += f"   x{i} = {sol}\n"
            
            # Kiểm tra
            result += f"\n🔍 **Kiểm tra nghiệm:**\n"
            for sol in solutions:
                if isinstance(sol, (int, float, sp.core.numbers.Float)):
                    check = lhs.subs(x, sol) - rhs.subs(x, sol)
                    result += f"   • x = {sol}: VT - VP = {sp.simplify(check)}\n"
            
            return result
            
        except Exception as e:
            return f"❌ Không thể giải phương trình: {str(e)}"
    
    def _calculate_expression(self, problem: str) -> str:
        """Tính biểu thức số học"""
        try:
            # Làm sạch
            expr = problem
            expr = expr.replace('^', '**').replace('×', '*').replace('÷', '/')
            expr = re.sub(r'[^0-9+\-*/().]', '', expr)
            
            # Tính
            result = eval(expr)
            
            return f"🧮 **Biểu thức:** {problem}\n\n✅ **Kết quả:** {result}"
            
        except Exception as e:
            return f"❌ Không thể tính: {str(e)}"
    
    def _solve_derivative(self, problem: str) -> str:
        """Tính đạo hàm"""
        try:
            x = sp.symbols('x')
            
            # Trích xuất hàm
            if 'của' in problem.lower():
                func_str = problem.lower().split('của')[1].strip()
            else:
                func_str = problem.replace('đạo hàm', '').strip()
            
            func = self._safe_sympify(func_str)
            derivative = sp.diff(func, x)
            
            return f"📝 **Hàm số:** f(x) = {func}\n\n" \
                   f"🧮 **Đạo hàm:** f'(x) = {derivative}\n\n" \
                   f"📊 **Rút gọn:** {sp.simplify(derivative)}"
                   
        except Exception as e:
            return f"❌ Không thể tính đạo hàm: {str(e)}"
    
    def _solve_integral(self, problem: str) -> str:
        """Tính tích phân"""
        try:
            x = sp.symbols('x')
            
            # Trích xuất hàm
            func_str = problem.replace('tích phân', '').replace('của', '').replace('dx', '').strip()
            func = self._safe_sympify(func_str)
            
            # Tính tích phân
            integral = sp.integrate(func, x)
            
            return f"📝 **Tích phân:** ∫({func}) dx\n\n" \
                   f"✅ **Kết quả:** {integral} + C"
                   
        except Exception as e:
            return f"❌ Không thể tính tích phân: {str(e)}"
    
    def _solve_geometry(self, problem: str) -> str:
        """Giải bài toán hình học"""
        problem_lower = problem.lower()
        
        # Hình tròn
        if 'hình tròn' in problem_lower:
            radius_match = re.search(r'[rR]\s*[=:]\s*([\d.]+)', problem)
            if radius_match:
                r = float(radius_match.group(1))
                
                if 'diện tích' in problem_lower:
                    area = math.pi * r * r
                    return f"📐 **Hình tròn:**\n" \
                           f"   Bán kính: r = {r}\n" \
                           f"   Diện tích: S = πr² = {math.pi:.4f} × {r}² = {area:.4f}"
                
                elif 'chu vi' in problem_lower:
                    perimeter = 2 * math.pi * r
                    return f"📐 **Hình tròn:**\n" \
                           f"   Bán kính: r = {r}\n" \
                           f"   Chu vi: C = 2πr = 2 × {math.pi:.4f} × {r} = {perimeter:.4f}"
        
        return f"📐 **Công thức hình học:**\n" \
               f"   • Hình tròn: S = πr², C = 2πr\n" \
               f"   • Hình vuông: S = a², C = 4a\n" \
               f"   • HCN: S = a×b, C = 2(a+b)\n" \
               f"💡 Nhập: 'diện tích hình tròn r=5'"
    
    def _general_solution(self, problem: str) -> str:
        """Giải chung"""
        return f"🤔 **Bài toán:** {problem}\n\n" \
               f"💡 **SymPy hỗ trợ:**\n" \
               f"   • Giải phương trình: x^2 - 5x + 6 = 0\n" \
               f"   • Tính toán: 2 + 3 * (5 - 1)\n" \
               f"   • Đạo hàm: đạo hàm của x^3 + 2x\n" \
               f"   • Tích phân: tích phân của x^2 dx\n" \
               f"   • Hình học: diện tích hình tròn r=5"
    
    def _safe_sympify(self, expr_str: str):
        """Chuyển đổi an toàn sang sympy expression"""
        expr_str = expr_str.replace('^', '**')
        expr_str = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', expr_str)
        expr_str = re.sub(r'([a-zA-Z)])(\d)', r'\1*\2', expr_str)
        expr_str = expr_str.replace(' ', '')
        return sp.sympify(expr_str)
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "name": "SymPy Local",
            "version": sp.__version__,
            "type": "local",
            "requires_api_key": False,
            "free": True,
            "offline": True
        }