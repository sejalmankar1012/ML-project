# Movie Analysis and Customer Segmentation Project

This project focuses on conducting a movie analysis and customer segmentation using data analysis techniques. The goal is to gain insights into the characteristics of movies and identify distinct customer segments based on their movie preferences. This README file provides an overview of the project, its objectives, and instructions for running the code.

## Project Structure

The project is structured as follows:

```
- data/                     # Directory for storing data files
- notebooks/                # Directory containing Jupyter notebooks
  - Movie analysis.ipynb    # Notebook for movie analysis
  - Customer Segmentation.ipynb  # Notebook for customer segmentation
- README.md                 # Project overview and instructions
- requirements.txt          # Required Python libraries
```

## Getting Started

### Prerequisites

To run the code and notebooks, make sure you have the following dependencies installed:

- Python 3.7 or higher
- Jupyter Notebook
- Required libraries (specified in `requirements.txt`)

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/sejalmankar1012/movie-analysis-segmentation.git
   ```

2. Navigate to the project directory:

   ```
   cd movie-analysis-segmentation
   ```

3. Install the required libraries using pip:

   ```
   pip install -r requirements.txt
   ```

### Data

The project uses two datasets: 

- `IMDB-Movie-Data.csv`: A dataset containing information about movies, including title, genre, release year, and ratings.
- `Mall_Customers.csv`: A dataset containing customer data, including age, gender, movie preferences, and ratings.

Place these datasets in the `data/` directory before running the notebooks.

## Notebooks

The project includes two Jupyter notebooks:

1. `Movie analysis.ipynb`: This notebook focuses on analyzing the movie dataset. It explores the distribution of genres, ratings, and release years. It also includes visualizations and statistical analysis of the data.

2. `Customer Segmentation.ipynb`: This notebook focuses on customer segmentation based on their movie preferences. It applies clustering algorithms to identify distinct customer segments and visualizes the results.

You can run and interact with the notebooks to explore the analysis, modify the code, and observe the outputs.

## Usage

1. Launch Jupyter Notebook:

   ```
   jupyter notebook
   ```

2. In your web browser, navigate to the notebook of interest (`Movie analysis.ipynb` or `Customer Segmentation.ipynb`) in the `notebooks/` directory.

3. Run the notebook cells by clicking the "Run" button or using the appropriate keyboard shortcuts.

4. Follow the instructions and comments within the notebooks to perform the movie analysis and customer segmentation.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The datasets used in this project were obtained from kaggle.
- Inspiration and code snippets may have been adapted from various sources and credited within the notebooks.

Feel free to modify and extend this project according to your needs. Happy analyzing and segmenting movies and customers!

