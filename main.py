from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Cargar los DataFrames de juegos y revisiones al iniciar la aplicación
steam_games_relevantes_df = pd.read_csv('steam_games_relevantes.csv')
positive_reviews = pd.read_csv('positive_reviews.csv')
negative_reviews = pd.read_csv('negative_reviews.csv')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/games")
def get_games():
    # Aquí debes cargar y retornar la lista de juegos desde tu DataFrame
    games_list = steam_games_relevantes_df.to_dict(orient='records')
    return games_list

@app.get("/games/{game_id}")
def get_game(game_id: int):
    # Aquí debes buscar y retornar los detalles de un juego específico por ID
    game_details = steam_games_relevantes_df[steam_games_relevantes_df['id'] == game_id]
    if not game_details.empty:
        game_details_dict = game_details.iloc[0].to_dict()
        return game_details_dict
    else:
        return {"message": f"Game with ID {game_id} not found"}

@app.get("/reviews")
def get_reviews():
    # Aquí debes cargar y retornar las revisiones de usuarios
    # Puedes cargar las revisiones positivas o negativas según tus necesidades
    # desde los DataFrames de revisiones
    return {"message": "User reviews"}

@app.get("/sentiment_analysis/{year}")
def sentiment_analysis(year: int):
    # Filtrar las revisiones por el año de lanzamiento
    reviews_by_year = user_reviews_df[user_reviews_df['year'] == year]

    # Calcular estadísticas de las revisiones filtradas
    sentiment_stats = reviews_by_year['sentiment_score'].describe()

    # Crear un diccionario con las estadísticas
    sentiment_stats_dict = {
        'Negative': sentiment_stats['mean'],
        'Neutral': sentiment_stats['50%'],  # Mediana
        'Positive': sentiment_stats['max']
    }

    return sentiment_stats_dict
