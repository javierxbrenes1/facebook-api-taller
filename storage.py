import pymongo
from pymongo import ReplaceOne

def get_mongodb_database():
    url = "mongodb://localhost:27017/" ## actualizala por tu connexion
    
    try:
        # serverSelectionTimeoutMS: tiempo máximo para intentar conectar (en milisegundos)
        client = pymongo.MongoClient(url, serverSelectionTimeoutMS=5000)
        
        # Verificar que el servidor está disponible con un ping
        client.admin.command('ping')
        
        db = client.get_database('facebook')
        if db is None:
            db = client.create_database('facebook')
        
        print("✅ Conexión exitosa a MongoDB")
        return db
        
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print(f"❌ Error: No se pudo conectar al servidor MongoDB en {url}")
        print(f"  Verifica que MongoDB esté corriendo.")
        raise
    except pymongo.errors.ConnectionFailure as e:
        print(f"❌ Error de conexión a MongoDB: {e}")
        raise
    except Exception as e:
        print(f"❌ Error inesperado al conectar a MongoDB: {e}")
        raise

def save_posts_in_mongodb(posts):
    if not posts:
        print("⚠️ No hay posts para guardar")
        return
    
    try:
        for post in posts:
            post['_id'] = post['id']
        
        db = get_mongodb_database()
        collection = db.get_collection('facebook_posts')
        if collection is None:
            collection = db.create_collection('facebook_posts')

        # Use bulk_write with ReplaceOne to upsert posts based on _id
        operations = [
            ReplaceOne({'_id': post['_id']}, post, upsert=True)
            for post in posts
        ]
        
        if operations:
            result = collection.bulk_write(operations)
            print(f"✓ Encontrados: {result.matched_count}, Modificados: {result.modified_count}, Insertados: {result.upserted_count}")
            
    except pymongo.errors.ServerSelectionTimeoutError:
        print("❌ Error: No se pudo conectar a MongoDB para guardar los posts")
        raise   
    except Exception as e:
        print(f"❌ Error al guardar posts en MongoDB: {e}")
        raise

def save_posts_in_sql_server(posts):
    ## TODO: Crea el codigo para guardar en SQL SERVER
    pass