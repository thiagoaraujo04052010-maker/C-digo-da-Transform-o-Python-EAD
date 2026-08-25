
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


print("=== BOLETIM ESCOLAR ===")

nome = input("Digite o nome do aluno: ")
supervisor = input("Digite o nome do professor:")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperacao"
else:
    situacao = "Reprovado"

print("\n=== RESULTADO ===")
print(f"Aluno: {nome}")
print(f"Supervisor:{supervisor}")
print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Nota 3: {nota3:.1f}")
print(f"Media: {media:.2f}")
print(f"Situacao: {situacao}")