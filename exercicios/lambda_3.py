alunos = [('Pedro', 14), ('Maria', 19), ('João', 12), ('Ana', 17)] 

alunos_or=sorted(alunos, key=lambda nota: nota[1], reverse=True)

print(alunos_or)