from data.registros import gerar_registros
from core.indices import criar_indices
from core.benchmark import benchmark_buscas

def main():
    print("Gerando registros...")
    registros = gerar_registros()

    print("Criando índices...")
    indices = criar_indices(registros)

    print("Executando benchmarks...\n")

    testes = [
        ("id", 500_000),
        ("email", "usuario750000@exemplo.com"),
        ("nome", "Usuario999999")
    ]

    for criterio, valor in testes:
        resultado = benchmark_buscas(registros, indices, criterio, valor)
        print(f"Busca por {criterio}:")
        print(f" - Tempo com índice: {resultado['tempo_indexado']:.8f} s")
        print(f" - Tempo linear:     {resultado['tempo_linear']:.8f} s")
        print(f" - Aceleração:       {resultado['aceleracao']:.1f}x\n")


if __name__ == "__main__":
    main()