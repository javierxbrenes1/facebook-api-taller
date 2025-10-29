## El siguiente script realiza lo siguiente:
## 1. Obtiene las paginas de Facebook del usuario actual
## 2. Obtiene las publicaciones de la pagina de Facebook 'CUC Almacenes de datos'
## 3. Obtiene los comentarios de cada publicacion
## 4. Obtiene las reacciones de cada publicacion
## 5. Agrega la informacion de los comentarios y reacciones a cada publicacion
## 6. Guarda los posts en una base de datos NoSql
## 7. Intenta guardar los posts en SQL SERVER


import facebook_client
import storage

## Paso 1. Obtiene las paginas
print('🔍 Obteniendo las paginas')
pages = facebook_client.get_pages()
print('✅ Paginas obtenidas: ', len(pages))

## Paso 2. filtra buscando la pagina deseada en este caso Cuc almacenes de datos
print('🔍 Buscando la pagina CUC Almacenes de datos')
cuc_almacenes_page = next((page for page in pages if page['name'] == 'CUC Almacenes de datos'), None)
print('✅ Pagina encontrada: ', cuc_almacenes_page['name'])

## Paso 3. Obtiene las publicaciones de la pagina
print('🔍 Obtiene las publicaciones de la pagina')
cuc_almacenes_posts = facebook_client.get_posts(cuc_almacenes_page['id'], cuc_almacenes_page['access_token'])
print('✅ Publicaciones obtenidas: ', len(cuc_almacenes_posts))

## Paso 4. Obtiene los comentarios y reacciones de cada publicacion
print('🔍 Obtiene los comentarios y reacciones de cada publicacion')
for post in cuc_almacenes_posts:
    comments = facebook_client.get_comments(post['id'], cuc_almacenes_page['access_token'])
    post['comments'] = comments
    print('✅ Comentarios obtenidos: ', len(comments), 'para la publicacion: ', post['id'])
    reactions = facebook_client.get_reactions(post['id'], cuc_almacenes_page['access_token'])
    post['reactions'] = reactions
    print('✅ Reacciones obtenidas: ', len(reactions), 'para la publicacion: ', post['id'])


# Parte del Taller: 
# TODO: Lee la documentacion del Pages API y trata de obtener algun otra informacion


## Paso 5: Guarda los posts en una base de datos NoSql 
print('🔍 Guardando los posts en una base de datos NoSql')
storage.save_posts_in_mongodb(cuc_almacenes_posts)
print('✅ Posts guardados en la base de datos NoSql')
## Parte del Taller
# TODO: Intenta guardar los posts en SQL SERVER
##storage.save_posts_in_sql_server(cuc_almacenes_posts)

print('🥑 Fin del programa')