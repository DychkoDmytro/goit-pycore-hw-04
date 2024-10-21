import sys
from pathlib import Path
from colorama import Fore, Style

def visualize_directory(path: Path, indent: str = ""):
    # Перевірка наявності директорії
    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.{Style.RESET_ALL}")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не є директорією.{Style.RESET_ALL}")
        return

    # Проходимо по всіх елементах у директорії
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")  # Виводимо назви директорій у синьому
            visualize_directory(item, indent + "    ")  # Рекурсивний виклик для піддиректорій
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")  # Виводимо назви файлів у зеленому

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py <шлях до директорії>{Style.RESET_ALL}")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    visualize_directory(directory_path)