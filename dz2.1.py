def total_salary(path):
    try:
        
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue

            
            total = sum(salaries)
            
            average = total / len(salaries) if salaries else 0
            return total, average

    except FileNotFoundError:
      
        print(f"File {path} not found.")
        return 0, 0
    except Exception as e:
       
        print(f"An error occurred: {e}")
        return 0, 0
    

file_path = 'salary_file.txt'


with open(file_path, 'w', encoding='utf-8') as f:
    f.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")


total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")    