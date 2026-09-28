import agenda_diccionarios
from agenda_diccionarios import add_contact, get_contact, remove_contact, update_contact

def test_add_contact():
    agenda = {}
    assert add_contact(agenda, "Mariano", 423124324) == True
    assert agenda == {"Mariano": 423124324}
    
def test_get_contact():
    agenda = {"Mariano": 423124324} 
    assert get_contact(agenda, "Mariano") == "Mariano: 423124324"  
    assert get_contact(agenda, "Carlos") == "Contacto 'Carlos' no encontrado."

def test_add_contact_duplicates():
    agenda = {"Mariano": 423124324}  
    assert add_contact(agenda, "Mariano", 111111111) == False   
    assert agenda == {"Mariano": 423124324} 

def test_remove_contact():
    agenda = {"Mariano": 423124324}  
    assert remove_contact(agenda, "Mariano") == True   
    assert agenda == {}

def test_update_contact():
    agenda = {"Mariano": 423124324}  
    assert update_contact(agenda, "Mariano", 111111111) == True   
    assert agenda == {"Mariano": 111111111} 