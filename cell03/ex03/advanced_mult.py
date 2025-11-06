import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit(0)

for N in range(11):  
    products = []
    for i in range(11):
        result = N * i
        products.append(str(result))

    output_products = " ".join(products)
    print(f"Table de {N}: {output_products}")