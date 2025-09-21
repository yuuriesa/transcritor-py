## Transcritor de Áudios WhatsApp (Whisper)

Este projeto usa a biblioteca Whisper da OpenAI para transcrever áudios do WhatsApp (formato .opus) em texto.

📦 Requisitos

- Python 3.9+

- ffmpeg
 (para leitura de arquivos .opus)

- No terminal digite: sudo apt install ffmpeg


Instalar dependências do projeto:

- NO terminal digite: pip install openai-whisper

📂 Estrutura das pastas
transcritor/
 ├── audios/       # coloque aqui os seus arquivos .opus do WhatsApp
 ├── saidas/       # aqui serão salvos os arquivos .txt com a transcrição
 └── transcrever.py

▶️ Como usar

- Coloque os áudios .opus dentro da pasta audios/.

Execute o script:

- python3 transcrever.py


As transcrições aparecerão em saidas/, com o mesmo nome do áudio.

ℹ️ Observações

O modelo padrão é small, que equilibra velocidade e precisão.

Se quiser maior precisão, pode trocar para "medium" ou "large" no código, porém será ainda mais lento:

modelo = whisper.load_model("medium")
