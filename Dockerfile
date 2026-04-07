# 1. Escolha uma imagem base oficial (versão slim para ser leve)
FROM python:3.11-slim

# 2. Defina a pasta de trabalho dentro do container
WORKDIR /app

# 3. Se você tiver bibliotecas extras (como pandas ou requests),
# você copiaria um requirements.txt aqui. Caso contrário, ignore.
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia todos os seus arquivos do repositório para dentro do container
COPY . .

# 5. Comando padrão para manter o container aberto e pronto para uso
# Usamos o 'tail -f' para que o container não feche sozinho
CMD ["tail", "-f", "/dev/null"]
