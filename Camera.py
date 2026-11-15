
import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt
import uuid

# CONFIGURAÇÕES MQTT
BROKER = "broker.hivemq.com"
PORT = 1883
TOPICO = "gestos/comando"

# CONEXÃO MQTT
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id=f"camera-python-{uuid.uuid4().hex[:8]}"
)

client.connect(BROKER, PORT, 60)
client.loop_start()

print("Conectado ao broker MQTT!")

# MEDIAPIPE
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# CÂMERA
camera = cv2.VideoCapture(1, cv2.CAP_DSHOW) #camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

ultimo_comando = None


def detectar_gesto(landmarks):

    dedos = [
        landmarks[8].y < landmarks[6].y,
        landmarks[12].y < landmarks[10].y,
        landmarks[16].y < landmarks[14].y,
        landmarks[20].y < landmarks[18].y
    ]

    quantidade = sum(dedos)

    # MÃO FECHADA = NÃO
    if quantidade == 0:
        return 1

    # MÃO ABERTA = SIM
    elif quantidade == 4:
        return 2

    return None


while camera.isOpened():

    sucesso, frame = camera.read()

    if not sucesso:
        print("Erro ao acessar a câmera!")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = hands.process(rgb)

    if resultado.multi_hand_landmarks:

        for hand_landmarks in resultado.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            comando = detectar_gesto(hand_landmarks.landmark)

            if comando is not None:

                if comando != ultimo_comando:

                    client.publish(TOPICO, str(comando))

                    print(f"Mensagem MQTT enviada: {comando}")

                    ultimo_comando = comando

                texto = "NAO (1)" if comando == 1 else "SIM (2)"

                cv2.putText(
                    frame,
                    texto,
                    (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

    else:
        ultimo_comando = None

    cv2.imshow("Controle MQTT - SIM ou NAO", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
hands.close()
client.loop_stop()
client.disconnect()
cv2.destroyAllWindows()
