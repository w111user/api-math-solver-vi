# main.py
import os
import sys
import time
from typing import Dict, List, Optional

def clear_screen():
    """Xóa màn hình"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """Hiển thị banner"""
    print("="*60)
    print("🤖 MATH SOLVER SYSTEM - 4 ENGINE")
    print("="*60)
    print("1. 🚀 Tự động (Auto-select best engine)")
    print("2. 🔵 Gemini AI (Google Gemini API)")
    print("3. 🟢 DeepSeek AI (DeepSeek API)")
    print("4. 🔴 SymPy (Local - No API needed)")
    print("5. 📊 Test tất cả engines")
    print("6. 🔧 Cấu hình API Keys")
    print("7. ❌ Thoát")
    print("="*60)

def get_user_choice() -> str:
    """Lấy lựa chọn từ người dùng"""
    while True:
        choice = input("\n👉 Chọn engine (1-7): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            return choice
        print("⚠️ Vui lòng chọn 1-7")

def load_api_keys() -> Dict[str, Optional[str]]:
    """Tải API keys từ file hoặc biến môi trường"""
    keys = {
        'gemini': os.getenv('GEMINI_API_KEY'),
        'deepseek': os.getenv('DEEPSEEK_API_KEY')
    }
    
    # Thử đọc từ file
    if os.path.exists('api_keys.txt'):
        try:
            with open('api_keys.txt', 'r') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        if key.lower() == 'gemini_api_key':
                            keys['gemini'] = value
                        elif key.lower() == 'deepseek_api_key':
                            keys['deepseek'] = value
        except:
            pass
    
    return keys

def save_api_keys(gemini_key: str, deepseek_key: str):
    """Lưu API keys vào file"""
    with open('api_keys.txt', 'w') as f:
        if gemini_key:
            f.write(f"GEMINI_API_KEY={gemini_key}\n")
        if deepseek_key:
            f.write(f"DEEPSEEK_API_KEY={deepseek_key}\n")
    print("✅ Đã lưu API keys")

def configure_api_keys():
    """Cấu hình API keys"""
    print("\n" + "="*60)
    print("🔧 CẤU HÌNH API KEYS")
    print("="*60)
    
    current_keys = load_api_keys()
    
    print("💡 Lấy API keys miễn phí tại:")
    print("   • Gemini: https://makersuite.google.com/")
    print("   • DeepSeek: https://platform.deepseek.com/")
    print("\n📝 Nhập API keys (để trống nếu không muốn dùng):")
    
    gemini_key = input("🔑 Gemini API key: ").strip()
    deepseek_key = input("🔑 DeepSeek API key: ").strip()
    
    if gemini_key or deepseek_key:
        save_api_keys(gemini_key, deepseek_key)
    
    input("\n↵ Nhấn Enter để tiếp tục...")

def test_all_engines():
    """Test tất cả engines"""
    from solvers.gemini_solver import GeminiSolver
    from solvers.deepseek_solver import DeepSeekSolver
    from solvers.sympy_solver import SymPySolver
    
    print("\n" + "="*60)
    print("🧪 TEST TẤT CẢ ENGINES")
    print("="*60)
    
    test_problem = "x^2-5x+6=0"
    
    engines = []
    
    # Test SymPy (luôn có)
    try:
        solver = SymPySolver()
        start = time.time()
        result = solver.solve(test_problem)
        end = time.time()
        engines.append({
            'name': 'SymPy',
            'time': end - start,
            'success': True,
            'result': result[:100] + "..." if len(result) > 100 else result
        })
        print(f"✅ SymPy: {end-start:.2f}s")
    except Exception as e:
        print(f"❌ SymPy: Lỗi - {str(e)}")
    
    # Test Gemini
    api_keys = load_api_keys()
    if api_keys['gemini']:
        try:
            solver = GeminiSolver(api_keys['gemini'])
            start = time.time()
            result = solver.solve(test_problem)
            end = time.time()
            
            engines.append({
                'name': 'Gemini',
                'time': end - start,
                'success': True,
                'result': result[:100] + "..." if len(result) > 100 else result
            })
            print(f"✅ Gemini: {end-start:.2f}s")
        except Exception as e:
            print(f"❌ Gemini: Lỗi - {str(e)}")
    else:
        print("⚠️ Gemini: Chưa có API key")
    
    # Test DeepSeek
    if api_keys['deepseek']:
        try:
            solver = DeepSeekSolver(api_keys['deepseek'])
            start = time.time()
            result = solver.solve(test_problem)
            end = time.time()
            
            engines.append({
                'name': 'DeepSeek',
                'time': end - start,
                'success': True,
                'result': result[:100] + "..." if len(result) > 100 else result
            })
            print(f"✅ DeepSeek: {end-start:.2f}s")
        except Exception as e:
            print(f"❌ DeepSeek: Lỗi - {str(e)}")
    else:
        print("⚠️ DeepSeek: Chưa có API key")
    
    # Hiển thị kết quả
    print("\n" + "="*60)
    print("📊 KẾT QUẢ TEST")
    print("="*60)
    
    engines.sort(key=lambda x: x['time'])
    
    for i, engine in enumerate(engines, 1):
        print(f"\n{i}. 🏆 {engine['name']}:")
        print(f"   ⏱️ Thời gian: {engine['time']:.2f}s")
        print(f"   📝 Kết quả: {engine['result']}")
    
    input("\n↵ Nhấn Enter để tiếp tục...")

def solve_problem(engine_choice: str):
    """Giải bài toán với engine được chọn"""
    from solvers.gemini_solver import GeminiSolver
    from solvers.deepseek_solver import DeepSeekSolver
    from solvers.sympy_solver import SymPySolver
    
    api_keys = load_api_keys()
    
    # Chọn engine
    if engine_choice == '1':  # Auto
        engines_to_try = []
        
        # Thêm các engines có API key
        if api_keys['gemini']:
            try:
                engines_to_try.append(GeminiSolver(api_keys['gemini']))
            except:
                pass
        
        if api_keys['deepseek']:
            try:
                engines_to_try.append(DeepSeekSolver(api_keys['deepseek']))
            except:
                pass
        
        # Luôn thêm SymPy
        engines_to_try.append(SymPySolver())
        
        if not engines_to_try:
            print("❌ Không có engine nào khả dụng!")
            return
        
        solver = engines_to_try[0]  # Dùng engine đầu tiên
        engine_name = "Auto (Dùng engine đầu tiên khả dụng)"
        
    elif engine_choice == '2':  # Gemini
        if not api_keys['gemini']:
            print("❌ Chưa có Gemini API key!")
            print("💡 Chạy option 6 để cấu hình API key")
            return
        solver = GeminiSolver(api_keys['gemini'])
        engine_name = "Gemini AI"
        
    elif engine_choice == '3':  # DeepSeek
        if not api_keys['deepseek']:
            print("❌ Chưa có DeepSeek API key!")
            print("💡 Chạy option 6 để cấu hình API key")
            return
        solver = DeepSeekSolver(api_keys['deepseek'])
        engine_name = "DeepSeek AI"
        
    else:  # SymPy
        solver = SymPySolver()
        engine_name = "SymPy Local"
    
    # Nhập bài toán
    print("\n" + "="*60)
    print(f"🧮 {engine_name}")
    print("="*60)
    
    while True:
        print("\n" + "-"*40)
        problem = input("📝 Nhập bài toán (hoặc 'back' để quay lại): ").strip()
        
        if problem.lower() == 'back':
            break
        
        if not problem:
            continue
        
        print(f"🤔 Đang giải với {engine_name}...")
        
        try:
            start_time = time.time()
            result = solver.solve(problem)
            end_time = time.time()
            
            print("\n" + "="*60)
            print("📊 KẾT QUẢ:")
            print("="*60)
            print(result)
            print("="*60)
            print(f"⏱️ Thời gian: {end_time - start_time:.2f}s")
            print("="*60)
            
        except Exception as e:
            print(f"\n❌ LỖI: {str(e)}")
            print("💡 Hãy thử engine khác hoặc nhập lại bài toán")
        
        input("\n↵ Nhấn Enter để tiếp tục...")

def main():
    """Hàm chính"""
    clear_screen()
    
    while True:
        show_banner()
        choice = get_user_choice()
        
        if choice == '7':  # Thoát
            print("\n👋 Tạm biệt!")
            break
        
        elif choice == '6':  # Cấu hình API keys
            configure_api_keys()
            clear_screen()
        
        elif choice == '5':  # Test all engines
            test_all_engines()
            clear_screen()
        
        else:  # Giải toán (1-4)
            solve_problem(choice)
            clear_screen()

if __name__ == "__main__":
    # Kiểm tra dependencies
    try:
        import sympy
        print("✅ SymPy đã được cài đặt")
    except ImportError:
        print("❌ SymPy chưa được cài đặt!")
        print("📦 Đang cài đặt SymPy...")
        os.system("pip install sympy")
        print("✅ Đã cài đặt SymPy")
    
    main()
