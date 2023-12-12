import random
import csv

def Faker_Laptop():
    company_list = ['Apple', 'hp', 'Dell', 'Acer', 'Asus', 'Chuwi', 'lenevo', 'MSI', 'Microsoft']
    TypeName_list = ['UltraBook', 'NoteBook', '2 in 1 Convertible', 'Gaming', 'WorkStation', 'Business Laptop']
    Resolution_list = ['HD 1920x1080 ', 'Full HD', '2K', '4K', 'IPS Panel Full HD / Touchscreen 1920x1080','IPS Panel Retina Display 2560x1600']
    cpu_list = ['Intel Core i5', 'Intel Core i7' , 'Intel Core i9', 'AMD Ryzen 5', 'AMD Ryzen 7', 'AMD A9-Series 9420','Intel Pentium Quad Core N4200', 'Intel Atom x5-Z8550', 'Intel Xeon E3-1505M ','Intel Celeron Dual Core 3855U ']
    Ram_list = ['4GB', '8GB', '12GB', '16GB']
    Memory_list = ['128GB SSD', '256GB Flash Storage', '1TB HDD', '256GB SSD', '512GB SSD', '1TB HDD', '2TB HDD','512GB NVMe SSD', '1TB NVMe SSD', '2TB NVMe SSD', '256GB eMMC', '512GB eMMC', '1TB SSHD', '4TB HDD','128GB PCIe SSD', '256GB PCIe SSD', '2TB SATA SSD', '1TB Fusion Drive', '6TB HDD']
    Gpu_list = ['NVIDIA GeForce GTX 1650', 'AMD Radeon RX 5600M', 'Intel Iris Xe Graphics']
    OpSys_list = ['Windows 10', 'Windows 11', 'macOS', 'Linux', 'No OS']

    random_company = random.choice(company_list)
    TypeName = random.choice(TypeName_list)
    Inches = random.uniform(11, 18)
    ScreenResolution = random.choice(Resolution_list)
    Cpu = random.choice(cpu_list)
    Ram = random.choice(Ram_list)
    Memory = random.choice(Memory_list)
    Gpu = random.choice(Gpu_list)
    OpSys = random.choice(OpSys_list)
    Weight = random.uniform(2, 5)

    # Add logical pricing for other companies
    if random_company == 'Apple' and Ram == '16GB' and OpSys=='macOS':
        price = random.uniform(80000, 120000)
    elif random_company == 'hp' and Ram == '12GB': 
        price = random.uniform(60000, 80000)
    elif random_company == 'Dell' and Ram=='8GB':
        price = random.uniform(65000, 100000)
    else:
        # Add default pricing for other companies
        price = random.uniform(30000, 70000)

    # Create a dictionary with laptop attributes
    laptop_instance = {
        'CompanyName': random_company,
        'TypeOfLaptop': TypeName,
        'Inches': Inches,
        'ScreenResolution': ScreenResolution,
        'Cpu': Cpu,
        'Ram': Ram,
        'Memory': Memory,
        'Gpu': Gpu,
        'OpSys': OpSys,
        'Weight': Weight,
        'Price': price
    }

    return laptop_instance


def write_laptops_to_csv(file_path, num_laptops=1000):
    # Generate fake laptop data
    laptops = [Faker_Laptop() for _ in range(num_laptops)]

    # Specify the CSV file header
    fieldnames = ['CompanyName', 'TypeOfLaptop', 'Inches', 'ScreenResolution', 'Cpu', 'Ram', 'Memory', 'Gpu', 'OpSys','Weight', 'Price']

    # Write data to CSV file
    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write laptop instances
        writer.writerows(laptops)

# Example usage
csv_file_path = 'laptops.csv'
write_laptops_to_csv(csv_file_path)
print(f"Laptop data written to {csv_file_path}")
