# GS_IOT - Moving Health

Este projeto foi criado para promover acessibilidade as pessoas com problemas de locomoção, para que seja possível que elas recebam tratamentos de maneira mais rápida ao invés de irem para o hospital que em alguns casos não é possível, os médicos vão até suas casas para um atendimento mais rápido para o caso.
Utilizamos o ESP32 para que auxilie com a comunicação, permitindo que pessoas com dificuldades enviem sinais rápidos de **Sim** ou **Não** utilizando gestos capturados por câmera e sinalizados por cores (lâmpadas vermelha e verde).

---
## Links

* https://wokwi.com/projects/479996866396560385
* Caso o vídeo no repositório não rode: https://www.youtube.com/watch?v=ByYXcnte1iI

##  Integrantes

* **RM559483 - Matheus Ikeda**
* **RM560723 - Davis Junior**
* **RM560340 - Matheus Machado**

## 🎯 Proposta do Projeto

O sistema foi criado com foco em **acessibilidade simples e direta**. Através da captura de visão computacional (MediaPipe) e comunicação via protocolo MQTT, o usuário pode interagir com o sistema fazendo gestos simples para informar cuidadores ou familiares se precisa ou não de auxílio no momento:

* **Mão Fechada (Não / Necessita de auxílio):** Envia o comando `1` e sinaliza com a cor **Vermelha**.
* **Mão Aberta (Sim / Está tudo bem):** Envia o comando `2` e sinaliza com a cor **Verde**.

---

## 🛠️ Pré-requisitos e Ambiente Virtual (.venv)

Para garantir que todas as bibliotecas de visão computacional (`mediapipe`, `opencv-python`) e comunicação (`paho-mqtt`) funcionem perfeitamente sem conflitos de versão (especialmente a API `mp.solutions` do MediaPipe), **este projeto exige obrigatoriamente o uso do Python 3.11.9** dentro de um Ambiente Virtual (`.venv`).

### 1. Criar e Ativar o Ambiente Virtual (Python 3.11.9)
Abra o terminal (CMD ou PowerShell) na pasta raiz do projeto (`GS_IOT`) e execute os comandos abaixo:

* **Criar o ambiente virtual especificando o Python 3.11.9:**
  ```cmd
  python -m venv .venv
  ```
  Ativar o ambiente virtual:

No Command Prompt (CMD):

```cmd
Bash
.venv\Scripts\activate.bat
```

No PowerShell:

```cmd
PowerShell
.\.venv\Scripts\Activate.ps1
```
2. Instalação das Dependências (Imports)
Com o ambiente virtual ativado (o nome (.venv) aparecerá no início da linha do terminal), instale as versões compatíveis das bibliotecas necessárias:
```cmd
Bash
pip install --upgrade pip
pip install opencv-python mediapipe==0.10.21 paho-mqtt
```
Principais imports utilizados no código (Camera.py):


cv2 (opencv-python): Captura de vídeo e exibição da janela.

mediapipe (mediapipe==0.10.21): Reconhecimento e rastreamento dos pontos da mão (mp.solutions.hands).

paho.mqtt.client (paho-mqtt): Comunicação e envio dos comandos (1 ou 2) para o broker MQTT (broker.hivemq.com).

uuid: Geração de identificador único para o cliente MQTT (biblioteca nativa do Python).

🚀 Como Executar o Projeto
Certifique-se de que a sua webcam ou câmera externa esteja conectada (caso utilize câmera externa ou IP, ajuste o índice ou URL na linha cv2.VideoCapture(...) no arquivo Camera.py).

Com o ambiente virtual .venv ativado, execute o script principal:

```cmd
Bash
python Camera.py
```

A janela de captura de vídeo será aberta. Posicione sua mão em frente à câmera:

Mão fechada (punho): Envia 1 via MQTT -> Aciona a lâmpada Vermelha (NÃO / Precisa de auxílio).

Mão aberta (4 dedos esticados): Envia 2 via MQTT -> Aciona a lâmpada Verde (SIM / Tudo bem).

Para encerrar a execução, clique na janela do vídeo e pressione a tecla q no teclado.
