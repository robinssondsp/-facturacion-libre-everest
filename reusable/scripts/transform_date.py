def transform_date(vFecha):
    # Eliminar "hs" y dividir la cadena en partes
    parts = vFecha.replace(" hs", "").split()
    day = parts[0].zfill(2)  # Asegura 2 dígitos (e.g., "4" → "04")
    month = parts[1].lower()  # Mes en minúsculas
    time = parts[2]  # Hora (e.g., "17:58")
    
    # Diccionario para mapear meses
    months = {
        "ene": "01", "feb": "02", "mar": "03", "abr": "04",
        "may": "05", "jun": "06", "jul": "07", "ago": "08",
        "sep": "09", "oct": "10", "nov": "11", "dic": "12"
    }
    
    # Obtener el año actual
    from datetime import datetime
    current_year = datetime.now().year
    
    # Construir la fecha en el formato deseado
    formatted_date = f"{day}/{months[month]}/{current_year}"
    
    return formatted_date

# Ejemplo de uso (puedes eliminar esta parte al usarlo en UiPath)
#if __name__ == "__main__":
#    print(transform_date("4 sep 17:58 hs"))