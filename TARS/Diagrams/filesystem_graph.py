from graphviz import Digraph
import os

def generate_file_system_graph(output_dir='Diagrams', output_name='file_system_structure'):
    """
    Genera un grafico della struttura del file system del progetto e lo salva come PNG.

    Args:
        output_dir (str): Directory di output per il grafico.
        output_name (str): Nome del file di output (senza estensione).
    """
    # Crea la directory di output se non esiste
    os.makedirs(output_dir, exist_ok=True)

    # Inizia il diagramma
    dot = Digraph(comment="File System Structure")

    # Nodo principale (root)
    dot.node('TARS', 'TARS')

    # Sottocartelle di TARS
    dot.node('Backend', 'Backend')
    dot.edge('TARS', 'Backend')

    # Sottocartelle di Backend
    dot.node('app', 'app')
    dot.node('Database', 'Database')
    dot.node('Diagrams', 'Diagrams')
    dot.node('Docs', 'Docs')
    dot.node('tests', 'tests')
    dot.edge('Backend', 'app')
    dot.edge('Backend', 'Database')
    dot.edge('Backend', 'Diagrams')
    dot.edge('Backend', 'Docs')
    dot.edge('Backend', 'tests')

    # Contenuto di app/
    dot.node('core', 'core/')
    dot.node('logs', 'logs/')
    dot.node('models', 'models/')
    dot.node('routes', 'routes/')
    dot.node('services', 'services/')
    dot.node('main.py', 'main.py')
    dot.edge('app', 'core')
    dot.edge('app', 'logs')
    dot.edge('app', 'models')
    dot.edge('app', 'routes')
    dot.edge('app', 'services')
    dot.edge('app', 'main.py')

    # Contenuto di core/
    dot.node('file_system.py', 'file_system.py')
    dot.edge('core', 'file_system.py')

    # Contenuto di logs/
    dot.node('core_logger.py', 'core_logger.py')
    dot.node('routes_logger.py', 'routes_logger.py')
    dot.node('services_logger.py', 'services_logger.py')
    dot.edge('logs', 'core_logger.py')
    dot.edge('logs', 'routes_logger.py')
    dot.edge('logs', 'services_logger.py')

    # Contenuto di routes/
    dot.node('filesystem_routes.py', 'filesystem_routes.py')
    dot.edge('routes', 'filesystem_routes.py')

    # Contenuto di services/
    dot.node('config.py', 'config.py')
    dot.edge('services', 'config.py')

    # Contenuto di tests/
    dot.node('test_app.py', 'test_app.py')
    dot.edge('tests', 'test_app.py')

    # Salva il diagramma nella directory specificata
    dot.render(f'{output_dir}/{output_name}', format='png', cleanup=True)
    print(f"Diagramma generato: {output_dir}/{output_name}.png")


# Esegui la funzione per generare il grafico
if __name__ == "__main__":
    generate_file_system_graph()
