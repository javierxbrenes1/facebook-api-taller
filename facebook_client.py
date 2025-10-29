import requests

access_token = 'EAAXvOqfhQZBwBP7wFDsYDJZBr3kAWG0xnLXYBbxvbUSne5xvf8M93E7z3ZBr0YR3CQHxobRmNI8AAlnZCDDpoSjXYLG04fwh5hdp3dFZB6xpgRwmSql2ipYLZBEdVTZAbsGpZAuntjoOoG7TEQr23RMZAV70eZBViTmfuigzACuHGbZA7q8WSX2864fLC6gZAAvW'
host = 'https://graph.facebook.com/v24.0'


def get_pages():
    """
    Obtiene todas las páginas asociadas a la cuenta de Facebook del usuario actual.
    
    Returns:
        dict: Respuesta del API de Facebook con la lista de páginas y sus datos.
    """
    response = requests.get(f'{host}/me/accounts', params={'access_token': access_token})
    return response.json()['data']

def get_posts(page_id, page_access_token):
    """
    Obtiene todas las publicaciones de una página específica de Facebook.
    
    Args:
        page_id (str): El ID de la página de Facebook.
        page_access_token (str): Token de acceso específico de la página.
    
    Returns:
        dict: Respuesta del API con la lista de publicaciones de la página.
    """
    response = requests.get(f'{host}/{page_id}/posts', params={'access_token': page_access_token})
    return response.json()['data']

def get_comments(post_id, page_access_token):
    """
    Obtiene todos los comentarios de una publicación específica.
    
    Args:
        post_id (str): El ID de la publicación de Facebook.
        page_access_token (str): Token de acceso para la pagina.
    
    Returns:
        dict: Respuesta del API con la lista de comentarios de la publicación.
    """
    response = requests.get(f'{host}/{post_id}/comments', params={'access_token': page_access_token})
    return response.json()['data']

def get_reactions(post_id, page_access_token):
    """
    Obtiene todas las reacciones de una publicación específica.
    
    Args:
        post_id (str): El ID de la publicación de Facebook.
        page_access_token (str): Token de acceso para la pagina.
    
    Returns:
        dict: Respuesta del API con la lista de reacciones de la publicación.
    """
    response = requests.get(f'{host}/{post_id}/reactions', params={'access_token': page_access_token})
    return response.json()['data']
