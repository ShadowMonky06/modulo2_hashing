contacts_dict = {}

def add_contact(contacts, contact_name, phone_number):
    """
    Agrega un contacto al diccionario evitando sobreescrituras accidentales.
    """
    if contact_name in contacts:
        print(f"Aviso: El contacto '{contact_name}' ya existe con el número {contacts[contact_name]}.")
        return False
    
    contacts[contact_name] = phone_number
    print(f"Contacto '{contact_name}' agregado exitosamente.")
    return True

def get_contact(contacts, contact_name):
    """
    Busca un contacto en el diccionario de forma segura (evita KeyError).
    """
    # Usamos .get() para evitar KeyError si la clave no existe (complejidad O(1))
    phone_number = contacts.get(contact_name)
    if phone_number is not None:
        return f"{contact_name}: {phone_number}"
    return f"Contacto '{contact_name}' no encontrado."

def remove_contact(contacts, contact_name):
    """
    Elimina un contacto del diccionario de forma segura (evita KeyError).
    """
    if contact_name in contacts:
        del contacts[contact_name]
        print(f"Contacto '{contact_name}' eliminado exitosamente.")
        return True
    print(f"Contacto '{contact_name}' no encontrado.")
    return False

def update_contact(contacts, contact_name, phone_number):
    """
    Actualiza el número de un contacto existente de forma segura (evita KeyError).
    """
    if contact_name in contacts:
        contacts[contact_name] = phone_number
        print(f"Contacto '{contact_name}' actualizado exitosamente.")
        return True
    print(f"Contacto '{contact_name}' no encontrado.")
    return False

# Pruebas de funcionamiento
if __name__ == "__main__":
    # 1. Agregar contactos
    add_contact(contacts_dict, "Mariano", 423124324)
    add_contact(contacts_dict, "Zulema", 987654321)

    # 2. Intento de sobreescritura accidental (clave duplicada)
    add_contact(contacts_dict, "Mariano", 111111111)

    # 3. Buscar contactos usando hashing O(1)
    print("\n--- Búsqueda de contactos ---")
    print(get_contact(contacts_dict, "Mariano"))
    print(get_contact(contacts_dict, "Zulema"))
    print(get_contact(contacts_dict, "Carlos"))  # No existe, no lanza KeyError

    # Estado final del diccionario
    print("\nAgenda completa:", contacts_dict)
