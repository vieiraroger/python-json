json_string = '''
{
    "pessoas": [
		"Teste",
		"Vitor",
		"Roger",
		"Romulo"
	],
	"listaDeObjetos": [
		{
			"index": 0,
			"nome": "Teste 99"
		},
		{
			"index": 1,
			"nome": "Teste 1"
		},
		{
			"index": 2,
            "nome": "Teste 2"
		}
	],
	"Roger": {
		"age": 23
	}
}

'''

# Importar Biblioteca
import json

# Ler String Json
# load -> carregar
# (s) -> string
meu_objeto = json.loads(json_string)
print(meu_objeto['listaDeObjetos'])

meu_objeto['teste'] = "Roger 987"

# Criar String Json
json_string_output = json.dumps(meu_objeto, sort_keys=True, indent=4)

print(json_string_output)

# Ler Arquivo Json

with open('arquivo.json', 'r') as arquivo:
    meu_objeto2 = json.load(arquivo)
    print(meu_objeto2)

    # Escrever Arquivo Json
    meu_objeto2['teste'] = 'Roger 987'

    with open('arquivo2.json', 'w') as arquivo2:
        json.dump(meu_objeto2, arquivo2, indent=4)



