#business2code
#v.1
#10/05/2024

# Instalando o Google SKD

!pip install -q -U google-generativeai

import google.generativeai as genai

GOOGLE_API_KEY = "Your Google API Key Here"
genai.configure(api_key=GOOGLE_API_KEY)


#Listando os modelos disponíveis

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


#Configurando o modelo

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5
}

safety_settings = {
    "HARASSMENT": "BLOCK_MEDIUM_AND_ABOVE",
    "HATE": "BLOCK_MEDIUM_AND_ABOVE",
    "SEXUAL": "BLOCK_MEDIUM_AND_ABOVE",
    "DANGEROUS": "BLOCK_MEDIUM_AND_ABOVE"
}


#Inicializando o modelo

system_instruction=system_instruction = "Seu nome é Noah. Você é um desenvolvedor de software que precisa criar um roteiro técnico e um código a partir de um negócio definido junto ao cliente. Seja breve na resposta do primeiro passo e aguarde a resposta e responda ela antes de seguir para o próximo passo. Primeiro passo: você precisa perguntar de que área é o projeto e de que setor é o cliente. Segundo passo: aja como se ainda não existisse nenhuma configuração prévia no ambiente para essa implementação. Explique um possível fluxograma desse processo. Terceiro passo: Forneça exemplos de criação de objetos, metadados, fluxos, rótulos personalizados, usuários, campos customizados. Quarto passo: O projeto é todo realizado em Salesforce e a linguagem de programação é Apex. Caso sejam necessários componentes Aura ou LWC, utilizar javascript, HTML e CSS. Forneça exemplos de códigos Apex e de componentes LWC e Aura pertinentes ao solicitado."

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                              system_instruction=system_instruction)

chat = model.start_chat(history=[])


#Utilizando o modelo

prompt = input("Olá! Meu nome é Noah, e sou seu assistente de desenvolvimento de software. Como você se chama? ")

while prompt != "FIM":
  response = chat.send_message(prompt)
  print("Noah: ",response.text, "\n")
  prompt = input("Eu: ")