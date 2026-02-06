#include "Arduino.h"
#include "WebSocketsServer.h"
  // definimos constantes para nuestras redes WIFI
  const char* ssid="MOVIL";
  const char* password="Alumnos25";
//creamos un objeto de websocket y asignamos el puerto que vamos a usar
WebSocketsServer websocket= WebSocketsServer(81);
unsigned long lasAlt=0;
void WebSocketsEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t length)
{
  if(type==WStype_TEXT){
    Serial.printf("recibiendo texto: %s\n",payload);
  }
}
void setup() {
Serial.begin(115200);
//Inicializamos el wifi con las constantes que tenemos de nuestras redes 
WiFi.begin(ssid, password);
//Intentamos conecvtarnos a la red 
while(WiFi.status() != WL_CONNECTED){
  Serial.print(".");
  delay(500);
}
//cuando conecte vamos a imprimir nuestra ip local, esta la v amos a servir para
//poder usarla en nuestro Streamlit y mandar los datos
Serial.println("IP:");
Serial.print(WiFi.localIP());
websocket.begin();
//enviamos los datos en websocket
websocket.onEvent(WebSocketsEvent);
}

void loop() {
  //aqui activamos el loop para que cada 2 segundos se envien los datos
  websocket.loop();
    if (millis()-lasAlt>2000){
      lasAlt=millis();
      String json =  "{\"sensor\": " + String(random(1, 30)) + "}";
      websocket.broadcastTXT(json);
    }
}
