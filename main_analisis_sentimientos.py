# TALLER: ya que tienes los post y comments en mongoDB, consultalos, y utilizando 
# la libreria pysentimiento realiza un analisis de sentimientos a los comentarios y actualizalos

from storage import get_posts_from_mongodb, save_posts_in_mongodb
from pysentimiento import create_analyzer

posts = get_posts_from_mongodb()

analyzer = create_analyzer(task="sentiment", lang="es")

## Como usar create_analyzer

## sentimiento = analyzer.predict('Esto es un comentario')
## print(sentimiento.output)

## TODO: Agrega tu codigo aca