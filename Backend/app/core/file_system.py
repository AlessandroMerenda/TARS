from fastapi import APIRouter, HTTPException
import os
import re

router = APIRouter()



# CREAZIONE NUOVA CARTELLA

def is_valid_folder_name(name: str) -> bool:
    # Simple validation to check for invalid characters
    return bool(re.match(r'^[\w\-. ]+$', name))

@router.post("/create-folder/")
async def create_folder(folder_name: str, parent_folder: str = None):
    """
    Crea una cartella con il nome specificato, opzionalmente in una directory specifica.
    """
    if not is_valid_folder_name(folder_name):
        raise HTTPException(status_code=400, detail="Nome della cartella non valido.")

    # Usa il percorso specificato o la directory corrente
    base_path = parent_folder or os.getcwd()
    path = os.path.join(base_path, folder_name)

    try:
        # Crea la cartella
        os.makedirs(path)
        return {
            "message": f"Cartella '{folder_name}' creata con successo!",
            "path": path
        }
    except FileExistsError:
        return {
            "message": f"Cartella '{folder_name}' esiste già.",
            "path": path
        }
    except PermissionError:
        raise HTTPException(status_code=403, detail="Permesso negato per creare la cartella.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore del server: {str(e)}")
    


# ELIMINAZIONE CARTELLA

import shutil

def is_valid_path(path: str) -> bool:
    # Validazione robusta del percorso
    return os.path.isabs(path) and bool(re.match(r'^[\w\-. /]+$', path))

def confirm_deletion(path: str) -> bool:
    """
    Chiede conferma per eliminare la cartella.
    
    Args:
        path (str): Percorso della cartella da eliminare.
        
    Returns:
        bool: True se l'utente conferma, False altrimenti.
    """
    confirmation = input(f"Sei sicuro di voler eliminare la cartella '{path}' e tutti i suoi contenuti? (s/n): ").strip().lower()
    return confirmation == 's'

def delete_folder(path: str, force: bool = False):
    """
    Elimina una cartella specificata. Richiede conferma se la cartella non è vuota e 'force=True'.
    
    Args:
        path (str): Percorso della cartella da eliminare.
        force (bool): Se True, elimina anche le cartelle non vuote ricorsivamente.
        
    Returns:
        str: Messaggio di successo o errore.
    """
    if not is_valid_path(path):
        raise HTTPException(status_code=400, detail="Percorso della cartella non valido.")

    try:
        # Controlla se la cartella esiste
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail=f"La cartella '{path}' non esiste.")
        
        # Controlla se la cartella è vuota
        if force and os.listdir(path):  # Solo se `force` è True e la cartella non è vuota
            if not confirm_deletion(path):  # Richiede conferma
                return f"Operazione annullata per la cartella '{path}'."
        
        # Elimina la cartella
        if force:
            shutil.rmtree(path)  # Elimina ricorsivamente
            return f"Cartella '{path}' eliminata con successo (inclusi i contenuti)."
        else:
            os.rmdir(path)  # Elimina solo cartelle vuote
            return f"Cartella '{path}' eliminata con successo."
    except PermissionError:
        raise HTTPException(status_code=403, detail=f"Permesso negato per eliminare la cartella '{path}'.")
    except OSError as e:
        if "Directory not empty" in str(e):
            raise HTTPException(status_code=400, detail=f"La cartella '{path}' non è vuota. Usa 'force=True' per eliminare tutto.")
        else:
            raise HTTPException(status_code=500, detail=f"Errore durante l'eliminazione della cartella: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore del server: {str(e)}")



# RINOMINARE CARTELLE

def is_valid_folder_name(name: str) -> bool:
    # Simple validation to check for invalid characters
    return bool(re.match(r'^[\w\-. ]+$', name))

def log_operation(action: str, details: str):
    """
    Registra un'operazione in un file di log.
    
    Args:
        action (str): Tipo di operazione eseguita.
        details (str): Dettagli dell'operazione.
    """
    with open("operation_log.txt", "a") as log_file:
        log_file.write(f"{action}: {details}\n")

def rename_folder(current_name: str, new_name: str, parent_folder: str = None):
    """
    Rinomina una cartella.
    
    Args:
        current_name (str): Nome attuale o percorso della cartella.
        new_name (str): Nuovo nome desiderato.
        parent_folder (str): Percorso genitore (opzionale).
        
    Returns:
        str: Messaggio di successo o errore.
    """
    if not is_valid_folder_name(current_name) or not is_valid_folder_name(new_name):
        raise HTTPException(status_code=400, detail="Nome della cartella non valido.")

    # Determina il percorso completo della cartella corrente
    if parent_folder:
        current_path = os.path.join(parent_folder, current_name)
        new_path = os.path.join(parent_folder, new_name)
    else:
        current_path = current_name
        new_path = new_name

    try:
        # Controlla se la cartella corrente esiste
        if not os.path.exists(current_path):
            raise HTTPException(status_code=404, detail=f"La cartella '{current_path}' non esiste.")
        
        # Controlla se il nuovo nome è già utilizzato
        if os.path.exists(new_path):
            raise HTTPException(status_code=400, detail=f"Una cartella con il nome '{new_name}' esiste già in '{parent_folder or os.getcwd()}'.")
        
        # Rinomina la cartella
        os.rename(current_path, new_path)

        # Registra l'operazione nel log
        log_operation("rename_folder", f"{current_path} rinominato in {new_path}")

        return f"Cartella '{current_path}' rinominata con successo in '{new_path}'."
    
    except PermissionError:
        raise HTTPException(status_code=403, detail=f"Permesso negato per rinominare la cartella '{current_path}'.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante la rinomina della cartella: {str(e)}")

