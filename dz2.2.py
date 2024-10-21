def get_cats_info(path):
    try:
        cats = []
       
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                   
                    cat_id, name, age = line.strip().split(',')
                    
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
        return cats
    except FileNotFoundError:
        print(f"File {path} not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)