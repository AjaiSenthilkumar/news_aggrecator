from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your API Key from NewsAPI.org
API_KEY = '8ea38ed7ee9546b4baba4cd3b494ef83'

# Function to fetch news based on category
def fetch_news(category):
    url = f'https://newsapi.org/v2/top-headlines?category={category}&country=us&apiKey={API_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        
        # Return top 5 articles
        return articles[:5] if articles else []
    else:
        return []

# Route for homepage and form submission
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        category = request.form.get('category')
        news = fetch_news(category.lower())
        return render_template('index.html', news=news, category=category)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
