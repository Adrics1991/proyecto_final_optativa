import json

class ChatbotPlantas:
    def __init__(self, ruta_json):
        with open(ruta_json, "r", encoding="utf-8") as f:
            self.plantas = json.load(f)

    def responder(self, pregunta):
        pregunta = pregunta.lower()

        # Buscar si el usuario menciona alguna planta del JSON
        for planta in self.plantas:
            if planta in pregunta:
                info = self.plantas[planta]
                respuesta = (
                    f"🌿 Información sobre {planta.capitalize()}:\n"
                    f"- Características: {info['caracteristicas']}\n"
                    f"- Usos: {info['usos']}\n"
                    f"- Propiedades medicinales: {info['medicinal']}"
                )
                return respuesta
        
        return "Lo siento, no tengo información sobre esa planta."
