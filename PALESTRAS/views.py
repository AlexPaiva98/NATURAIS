from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.db import connection
from django.db import IntegrityError
from django.db import ProgrammingError

cursor = connection.cursor()
cursor2 = connection.cursor()
cursor3 = connection.cursor()
cursor5 = connection.cursor()
cursor6 = connection.cursor()

def post_list(request):
    return render(request, 'SITE/index.html', {})

def Login(request):
	return render(request, 'SITE/Login.html',{})

def Cadastro(request):
	return render(request, 'SITE/Cadastro.html',{})

# Create your views here.

def Inserir(request):
	if request.method == 'POST':
		x = request.POST.get("CPF")[0:3]
		y = request.POST.get("CPF")[4:7]
		z = request.POST.get("CPF")[8:11]
		w = request.POST.get("CPF")[12:]
		a = request.POST.get("Nome")
		b = int(x+y+z+w)
		c = request.POST.get("Tel")
		d = request.POST.get("Email")
		e = request.POST.get("Ministrante")
		f = request.POST.get("Senha")
		g = request.POST.get("Nasc")
		try:
			cursor.execute(
				"""INSERT INTO Pessoa(Nome, CPF, Celular, Email, Categoria, Senha, Nascimento) VALUES(%s, %s, %s, %s, %s, %s, %s)""", [
					a, b, c, d, e, f, g])
			return render(request, 'SITE/index.html', {})
		except IntegrityError:
				return render(request, "SITE/Tratamento_Erro1.html", {})

def Autenticar(request):
	cursor1 = connection.cursor()
	if request.method == 'POST':
		arq = open('Auxiliar.txt', 'w')
		x = request.POST.get("CPFA")[0:3]
		y = request.POST.get("CPFA")[4:7]
		z = request.POST.get("CPFA")[8:11]
		w = request.POST.get("CPFA")[12:]
		h = int(x+y+z+w)
		i = request.POST.get("SenhaA")
		cursor1.execute("SELECT * FROM Pessoa")
		for linha in cursor1.fetchall():
			if int(linha[0]) == int(h):
				if str(linha[5]) == str(i):
					arq.write(str(h))
					cursor1.close()
					arq.close()
					return render(request, 'SITE/index_autenticado.html', {})
					break
				else:
					continue
			else:
				continue
		return render(request, 'SITE/Login_Alert.html', {})

def AddCurso(request):
	return render(request, 'SITE/AddCurso.html', {})

def Inserir1(request):
	arq = open('Auxiliar.txt', 'r')
	p = 0
	cpf = arq.readlines()
	for linha in cpf:
		p = int(linha)
	arq.close()
	cursor5.execute("SELECT Categoria FROM Pessoa WHERE CPF = %s", [p])
	x = 0
	for linha in cursor5.fetchall():
		x = int(linha[0])
	if request.method == 'POST':
		if x == 1:
			j = request.POST.get("Nome")
			k = request.POST.get("CH")
			l = request.POST.get("Materia")
			m = request.POST.get("CEP")
			n = request.POST.get("Vagas")

			cursor2.execute(
				"""INSERT INTO Curso(Nome, Carga_Horaria, Materia, CEP, Vagas) VALUES (%s, %s, %s, %s, %s)""", [j, k, l, m, n])
			return render(request, 'SITE/index_autenticado.html', {})
		else:
			return render(request, 'SITE/index_autenticadoAL.html', {})

def Retornar(request):
	return render(request, 'SITE/index_autenticado.html', {})

def InCurso(request):
	cursor3 = connection.cursor()
	cursor4 = connection.cursor()
	cursor4.execute("SELECT COUNT(Cod_Curso) FROM Curso")
	x = 0
	for linha in cursor4.fetchall():
		x = linha[0]
	cursor4.close()
	count = x
	lista = []
	cursor3.execute("SELECT Cod_Curso, Nome FROM Curso")
	for linha in cursor3.fetchall():
		lista.append(str(linha[0])+ " - " + linha[1])
	lista = str(lista)[1:-1]
	return render(request, 'SITE/InCurso.html', {'conta': lista})

def Matricular(request):
	o = request.POST.get("Num1")
	arq = open('Auxiliar.txt', 'r')
	p = 0
	cpf = arq.readlines()
	for linha in cpf:
		p = int(linha)
	arq.close()
	try:
		cursor3.execute("""INSERT INTO Matricula(Cod_Curso, CPF) VALUES (%s, %s)""", [o, p])
		return render(request, 'SITE/index_autenticado.html', {})
	except ProgrammingError:
		return render(request, "SITE/Tratamento_Erro2.html", {})

def ModCurso(request):
	cursor7 = connection.cursor()
	cursor8 = connection.cursor()
	cursor7.execute("SELECT COUNT(Cod_Curso) FROM Curso")
	x = 0
	for linha in cursor7.fetchall():
		x = linha[0]
	cursor7.close()
	count = x
	lista = []
	cursor8.execute("SELECT Cod_Curso, Nome FROM Curso")
	for linha in cursor8.fetchall():
		lista.append(str(linha[0])+ " - " + linha[1])
	lista = str(lista)[1:-1]
	return render(request, 'SITE/ModCurso.html', {'conta': lista})

def Modificar(request):
	arq = open('Auxiliar.txt', 'r')
	p = 0
	cpf = arq.readlines()
	for linha in cpf:
		p = int(linha)
	arq.close()
	cursor5.execute("SELECT Categoria FROM Pessoa WHERE CPF = %s", [p])
	x = 0
	for linha in cursor5.fetchall():
		x = int(linha[0])
	if request.method == 'POST':
		if x == 1:
			u = request.POST.get("MNome")
			i = int(request.POST.get("MCH"))
			q = int(request.POST.get("MMateria"))
			z = request.POST.get("MCEP")
			t = int(request.POST.get("MVagas"))
			y = int(request.POST.get("MCodigo"))
			cursor6.execute("UPDATE Curso SET Nome = %s, Carga_Horaria = %s, Materia = %s, CEP = %s, Vagas = %s WHERE Cod_Curso = %s", [u, i, q, z, t, y])
			return render(request, 'SITE/index_autenticado.html', {})
		else:
			return render(request, 'SITE/index_autenticadoAL.html', {})

def DelCurso(request):
	cursor7 = connection.cursor()
	cursor8 = connection.cursor()
	cursor7.execute("SELECT COUNT(Cod_Curso) FROM Curso")
	x = 0
	for linha in cursor7.fetchall():
		x = linha[0]
	cursor7.close()
	count = x
	lista = []
	cursor8.execute("SELECT * FROM vwDeleteCurso")
	for linha in cursor8.fetchall():
		lista.append(str(linha[0])+ " - " + linha[1])
	lista = str(lista)[1:-1]
	return render(request, 'SITE/DelCurso.html', {'conta': lista})

def Excluir(request):
	arq = open('Auxiliar.txt', 'r')
	p = 0
	cpf = arq.readlines()
	for linha in cpf:
		p = int(linha)
	arq.close()
	cursor5.execute("SELECT Categoria FROM Pessoa WHERE CPF = %s", [p])
	x = 0
	for linha in cursor5.fetchall():
		x = int(linha[0])
	if request.method == 'POST':
		r = int(request.POST.get("DCodigo"));
		if x == 1:
			try:
				cursor6.execute("DELETE FROM Curso WHERE Cod_Curso = %s", [r])
				return render(request, 'SITE/index_autenticado.html', {})
			except IntegrityError:
				return render(request, "SITE/Tratamento_Erro.html", {})
		else:
			return render(request, 'SITE/index_autenticadoAL.html', {})

def Voltar(request):
	return render(request, 'SITE/index_autenticado.html', {})