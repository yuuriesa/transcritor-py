import whisper
import os

PASTA_COM_OS_AUDIOS = "audios"
PASTA_COM_AS_SAIDAS_DO_AUDIO = "saidas"

# Estou garantindo que a pasta de saída exista
os.makedirs(PASTA_COM_AS_SAIDAS_DO_AUDIO, exist_ok=True)

# Por aqui, é onde eu carrego o modelo Whisper que nesse caso estou usando
# a versão medium, a base funcionou perfeitamente com os testes e a small tbm,
# porém não foi preciso, medium a precisão foi bem maior.
modelo = whisper.load_model("medium")

# Aqui eu estou percorrendo os arquivos da pasta com os audios.
for arquivo in os.listdir(PASTA_COM_OS_AUDIOS):
    if arquivo.endswith(".opus"):
        caminho_do_audio = os.path.join(PASTA_COM_OS_AUDIOS, arquivo)
        print(f"Transcrevendo {arquivo}...")

        # Está linha é onde eu transcrevo o áudio
        resultado = modelo.transcribe(caminho_do_audio, language="pt")

        # Aqui é onde eu crio o arquivo de saída com o áudio transcrito
        nome_de_saida_do_audio = os.path.splitext(arquivo)[0] + ".txt"
        caminho_da_saida = os.path.join(
            PASTA_COM_AS_SAIDAS_DO_AUDIO, nome_de_saida_do_audio
        )

        with open(caminho_da_saida, "w", encoding="utf-8") as file:
            file.write(resultado["text"])
        print(f"Transcrição do áudio salva em {caminho_da_saida}")
