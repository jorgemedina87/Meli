from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class LogisticRegressionModel:

    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X_train, y_train):
        """
        Entrena el modelo con los datos proporcionados.
        
        Args:
        - X_train: Datos de entrada para entrenar el modelo.
        - y_train: Etiquetas correspondientes a los datos de entrada.
        """
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        """
        Evalúa el modelo con los datos de prueba.
        
        Args:
        - X_test: Datos de entrada para evaluar el modelo.
        - y_test: Etiquetas verdaderas correspondientes a los datos de prueba.
        
        Returns:
        - accuracy: Precisión del modelo en los datos de prueba.
        """
        accuracy = self.model.score(X_test, y_test)
        return accuracy

    def predict(self, X):
        """
        Realiza predicciones con el modelo.
        
        Args:
        - X: Datos de entrada para realizar predicciones.
        
        Returns:
        - predictions: Predicciones realizadas por el modelo.
        """
        predictions = self.model.predict(X)
        return predictions

