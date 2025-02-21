from openai import OpenAI
import base64


#criar Classe
class Reader_image():
    def __init__(self, imagem: str, modeloLLM: str, chaveAPI: str, prompt = 'descreva o que voce vê na imagem'):
        self.imagem = imagem
        self.modelo = modeloLLM
        self.apiKey = chaveAPI
        self.prompt = prompt

    def read_image(self):
        try:   

#tratar imagem
# Codificando uma imagem
            def encodeImage(imagem):
                
                with open(imagem, 'rb') as imagem:
                    return base64.b64encode(imagem.read()).decode('utf-8')
                
            imagecoded = encodeImage(self.imagem)

#dar descrição da imagem

            client = OpenAI(api_key= self.apiKey)
            response = client.chat.completions.create(
                model=f"{self.modelo}",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": self.prompt},
                            {
                                "type": "image_url",
                                "image_url":{ 
                                    'url': f"data:image/jpeg;base64,{imagecoded}"
                                            
                                },
                            
                                
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )
            imageDetails = response.choices[0].message.content

            print(imageDetails)
            return imageDetails

        except Exception as e:
           return f"Erro ao analisar imagem: {str(e)}"
