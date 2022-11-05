class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

def pre_mostra(raiz):
    if raiz is None:
        return '()'
    if raiz:
        return str([raiz.entry, pre_mostra(raiz.left), pre_mostra(raiz.right)]).replace('[', '(').replace(']', ')').replace(
            '"', '').replace("'()'", '()').replace("'", '').replace(',', '')


def mostra(raiz):
    mostra_a_arvore = pre_mostra(raiz)
    return mostra_a_arvore


def insert(item, tree, iten):
    if len(iten) != 1:
        if iten[0] == '.':
            if tree.left is None:
                tree.left = Tree('*')
            insert(item, tree.left, iten[1:])
        elif iten[0] == '-':
            if tree.right is None:
                tree.right = Tree('*')
            insert(item, tree.right, iten[1:])
    else:
        if iten[0] == '.':
            tree.left = Tree(a[0])
        elif iten[0] == '-':
            tree.right = Tree(a[0])

def printPorNivel(root):
    h = altura(root)
    for i in range(1, h+1):
        printNivel(root, i)

list_print = []

def printNivel(root, level):
    global list_print
    if root is None:
        return
    if level == 1:
        list_print.append(root.entry)
    elif level > 1:
        printNivel(root.left, level - 1)
        printNivel(root.right, level - 1)


def altura(node):
    if node is None:
        return 0
    else:
        laltura = altura(node.left)
        raltura = altura(node.right)

        if laltura > raltura:
            return laltura + 1
        else:
            return raltura + 1

def preorder(tree):
    if tree is None:
        return
    print(tree.entry)
    preorder(tree.left)
    preorder(tree.right)


tabela = []
simbolos = []
aux = ''

tabela.append([' ', '/'])

n1 = int(input())

codigo = input().split()
morse = Tree('*')
#insert(codigo, morse)
tabela.append(codigo)
for a in range(n1 - 1):
    codigo = input().split()
    #insert2(codigo, morse)
    tabela.append(codigo)

tabela_arvore = []

if tabela[1] == []:
    tabela.pop()



tabela_arvore = tabela[:]

if len(tabela_arvore) > 0:
    tabela_arvore.sort(key=lambda itens: len(itens[1]))
    for a in range(len(tabela_arvore) - 1, 0, -1):
        for b in range(a):
            if len(tabela_arvore[b][1]) == len(tabela_arvore[b + 1][1]):
                if tabela_arvore[b][1] < tabela_arvore[b + 1][1]:
                    tabela_arvore[b], tabela_arvore[b + 1] = tabela_arvore[b + 1], tabela_arvore[b]

for a in tabela_arvore:
    insert(a, morse, a[1])

#print(tabela_arvore)

n2 = int(input())

s = str(input())

#print(s)

if len(s) > 0:
    if s[-1] == ' ':
        s = s[:-1]

#print([a for a in s])
#print(tabela)

impossivel = False
tem = False

mensagem = []

if n2 == 0:
    if s != '':
        for a in s:
            if a == ' ':
                simbolos.append(aux)
                aux = ''
            elif a == '/':
                simbolos.append('/')
                aux = ''
            else:
                aux += a
        simbolos.append(aux)
        for a in simbolos:
            #if a == '/':
                #mensagem.append(' ')
            for b in tabela:
                if a == b[1]:
                    tem = True
                    #if b[1] != '/':
                    mensagem.append(b[0])
            if not tem:
                impossivel = True
                break
            else:
                tem = False
    else:
        mensagem = []
    #print('decodificar')


elif n2 == 1:
    espaço = False

    lista = []
    lista_print = []
    for a in s:
        lista.append(a)
    #print(f'lista = {lista}')
    for a in lista:
        if a == ' ':
            if not espaço:
                lista_print.append('/')
            espaço = True
        else:
            espaço = False
        for b in tabela:
            if a == b[0]:
                tem = True
                if a != ' ':
                    lista_print.append(f'{b[1]} ')
        if not tem:
            impossivel = True
            break
        else:
            tem = False
    #print(lista_print)
    for a in lista_print:
        if a == '/':
            mensagem.append(a)
        else:
            mensagem.append(str(a))
    #print('codificar')

if n2 == 0 and impossivel:
    print('Impossível decodificar a mensagem!')

elif n2 == 1 and impossivel:
    print('Impossível codificar a mensagem!')


else:
    for a in mensagem:
        print(a, end='')
    print()
    printPorNivel(morse)
    print(' '.join([w for w in list_print]))

del list_print[:]

#print(simbolos)
#print(mensagem)


