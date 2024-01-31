
# Import necessary modules
from flask import Flask, render_template, request

# Create the Flask application object
app = Flask(__name__)

# Define the routes
@app.route('/')
def home():
    """Render the home page."""
    featured_plants = ['Snake Plant', 'ZZ Plant', 'Pothos', 'Peace Lily']
    return render_template('index.html', featured_plants=featured_plants)

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@app.route('/plant-types')
def plant_types():
    """Render the plant types page."""
    plant_categories = {
        'Indoor Plants': ['Snake Plant', 'ZZ Plant', 'Pothos', 'Peace Lily'],
        'Outdoor Plants': ['Hosta', 'Daylily', 'Petunia', 'Marigold'],
        'Succulents': ['Aloe Vera', 'Jade Plant', 'Sedum', 'Haworthia'],
        'Cacti': ['Saguaro Cactus', 'Prickly Pear Cactus', 'Barrel Cactus', 'Golden Barrel Cactus'],
    }
    beginner_friendly_plants = ['Snake Plant', 'ZZ Plant', 'Pothos', 'Peace Lily', 'Aloe Vera', 'Jade Plant']
    plant_glossary = {
        'Annual': 'A plant that completes its life cycle in one year.',
        'Biennial': 'A plant that completes its life cycle in two years.',
        'Perennial': 'A plant that lives for more than two years.',
        'Deciduous': 'A plant that loses its leaves seasonally.',
        'Evergreen': 'A plant that retains its leaves throughout the year.',
    }
    return render_template('plant_types.html', plant_categories=plant_categories, beginner_friendly_plants=beginner_friendly_plants, plant_glossary=plant_glossary)

@app.route('/plant-care')
def plant_care():
    """Render the plant care page."""
    basic_care = {
        'Watering': 'Water your plants when the soil is dry to the touch.',
        'Sunlight': 'Most plants need bright indirect light.',
        'Humidity': 'Some plants prefer high humidity.',
        'Temperature': 'Most plants prefer temperatures between 60°F and 80°F.',
    }
    common_problems = {
        'Pests': 'Common pests include aphids, spider mites, and mealybugs.',
        'Diseases': 'Common diseases include powdery mildew, root rot, and leaf spot.',
        'Overwatering': 'Overwatering can cause root rot and other problems.',
    }
    propagation_methods = {
        'Cuttings': 'Cuttings can be taken from stems, leaves, or roots.',
        'Layering': 'Layering involves bending a stem down to the ground and covering it with soil.',
        'Division': 'Division involves dividing a plant into two or more smaller plants.',
    }
    return render_template('plant_care.html', basic_care=basic_care, common_problems=common_problems, propagation_methods=propagation_methods)

@app.route('/gallery')
def gallery():
    """Render the gallery page."""
    images = ['plant1.jpg', 'plant2.jpg', 'plant3.jpg', 'plant4.jpg']
    return render_template('gallery.html', images=images)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
