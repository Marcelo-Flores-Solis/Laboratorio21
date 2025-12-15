import json

def main():
    equipos_futbol = [
        {
            "Nombre": "Real Madrid",
            "país": "España",
            "nivelAtaque": 95,
            "nivelDefensa": 90
        },
        {
            "Nombre": "Manchester City",
            "país": "Inglaterra",
            "nivelAtaque": 98,
            "nivelDefensa": 88
        },
        {
            "Nombre": "Bayern Munich",
            "país": "Alemania",
            "nivelAtaque": 94,
            "nivelDefensa": 85
        },
        {
            "Nombre": "Melgar",
            "país": "Perú",
            "nivelAtaque": 75,
            "nivelDefensa": 78
        }
    ]

    print("--- Objeto Python (Lista de Diccionarios) ---")
    print(equipos_futbol) 
    
    
    json_str = json.dumps(equipos_futbol, indent=4, ensure_ascii=False)

    print("\n--- Cadena JSON Formateada ---")
    print(json_str)


if __name__ == "__main__":
    main()