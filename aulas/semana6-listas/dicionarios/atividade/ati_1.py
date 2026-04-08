# crie um discionário para guardar suas próprias informções nome, idade, cidade
# adicione uma nova chave-valor ao dicinário: "hobies", como uma lista de hobies como valor
# imprima na tela uma frase bonita usando esses dados, tipo: "Ola meu nome é e um dos meus hobies é da lista"


dados_pessoais = {"Nome" : "Paulo André Carminati",
                  "Idade" : 46,
                  "Cidade" : "Guarulhos"
                  }

dados_pessoais["Hobies"] = ["Games", "Gumpla"]

print(f"Ola Meu nome é {dados_pessoais["Nome"]}, minha idade é {dados_pessoais["Idade"]} anos, moro em "
      f"{dados_pessoais["Cidade"]} e um dos meus hobies é {dados_pessoais["Hobies"][0]} e {dados_pessoais["Hobies"][1]}")
