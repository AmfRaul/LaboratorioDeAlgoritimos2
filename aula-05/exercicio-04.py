#4. O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. Faça
#o programa que lê o valor de N e M e informa o número de combinações possíveis.

#N - Total de alunos
#M - Tamanho de um dos grupos - Deve ser menor que o tamanho total

#Fórmula: N!/(M! * (N-M)!)

#Para calcular o fatorial (!) utilize a biblioteca math com comando math.factorial(value)
import math
def calculo(n,m):
    try:

        if m < 0 or m > n:
            return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
    except:
        print("KSKSKS")

def main():
    try:
        n = int(input("Digite o total de alunos da turma: "))
        m = int(input("Digite o tamanho do grupo: "))

        if m < 0 or n > m:
            print("O numero deve ser menor de M")

        cal = calculo(n,m)
        print(cal)
    except ValueError:
        print("[ERROR] valor incorreto ")


main()
 