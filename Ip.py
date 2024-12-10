import ipaddress

# Função para carregar os blocos CIDR de um arquivo de texto
def load_cidr_blocks(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Função para calcular os ranges de IPs
def calculate_ranges(cidr_blocks):
    ranges = []
    for cidr in cidr_blocks:
        try:
            network = ipaddress.ip_network(cidr, strict=False)
            ranges.append(f"{cidr}: {network[0]} - {network[-1]}")
        except ValueError as e:
            ranges.append(f"{cidr}: Invalid CIDR block ({e})")
    return ranges

# Função principal
def main():
    filename = "cidr_blocks.txt"  # Substitua pelo caminho do seu arquivo
    cidr_blocks = load_cidr_blocks(filename)
    ranges = calculate_ranges(cidr_blocks)
    
    output_filename = "ip_ranges.txt"  # Salvar o resultado em um arquivo
    with open(output_filename, 'w') as file:
        file.write("\n".join(ranges))
    
    print(f"Os ranges foram salvos em {output_filename}")

if __name__ == "__main__":
    main()
