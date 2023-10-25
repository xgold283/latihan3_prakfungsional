random_list = [105, 3.1, "Hello", 737, "python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
float_list = list(filter(lambda x: isinstance(x, float), random_list))
int_list = list(filter(lambda x: isinstance(x, int), random_list))
string_list = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_dict(x):
    satuan = x % 10
    puluhan = (x // 10) % 10
    ratusan = x // 100
    return {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}

int_dict_list = list(map(map_int_to_dict, int_list))

# Output
print("Data Float:")
print(float_list)
print("Data Int:")
for item in int_dict_list:
    print(item)
print("Data String:")
print(string_list)
