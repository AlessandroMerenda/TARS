from graphviz import Digraph

def generate_final_project_structure(output_dir='Diagrams', output_name='final_file_system_structure'):
    dot = Digraph(comment='Final Project Structure')

    # Root
    dot.node('TARS', 'TARS')

    # Top-level directories
    for folder in ['Backend', 'Docs', 'Diagrams']:
        dot.node(folder, folder)
        dot.edge('TARS', folder)

    # Top-level file
    dot.node('environment.yml', 'environment.yml')
    dot.edge('TARS', 'environment.yml')

    # Backend
    dot.node('app', 'app/')
    dot.edge('Backend', 'app')

    # app Subdirectories
    for subdir in ['core/', 'models/', 'routes/', 'services/', 'logs/']:
        dot.node(subdir, subdir)
        dot.edge('app', subdir)

    # Files in core/
    dot.node('file_system.py', 'file_system.py')
    dot.edge('core/', 'file_system.py')

    # Files in logs/
    for log_file in ['core_logger.py', 'routes_logger.py', 'services_logger.py']:
        dot.node(log_file, log_file)
        dot.edge('logs/', log_file)

    # Files in routes/
    dot.node('filesystem_routes.py', 'filesystem_routes.py')
    dot.edge('routes/', 'filesystem_routes.py')

    # Main app file
    dot.node('main.py', 'main.py')
    dot.edge('app', 'main.py')

    # Config in Backend
    dot.node('config.py', 'config.py')
    dot.edge('Backend', 'config.py')

    # Tests
    dot.node('tests', 'tests/')
    dot.edge('Backend', 'tests')
    dot.node('test_app.py', 'test_app.py')
    dot.edge('tests', 'test_app.py')

    # Database inside Backend
    dot.node('Database', 'Database/')
    dot.edge('Backend', 'Database')

    # Files in Database
    dot.node('db_logger.py', 'db_logger.py')
    dot.edge('Database', 'db_logger.py')

    # Files in Diagrams/
    dot.node('file_system_graph.py', 'file_system_graph.py')
    dot.node('file_system_structure.png', 'file_system_structure.png')
    dot.edge('Diagrams', 'file_system_graph.py')
    dot.edge('Diagrams', 'file_system_structure.png')

    # Generate the diagram
    dot.render(f'{output_dir}/{output_name}', format='png', cleanup=True)
    print(f"Diagramma finale generato: {output_dir}/{output_name}.png")

generate_final_project_structure()
