"""
Modulo que agrega ruido en funcion de una probabilidad dada
"""
import functools
from typing import Dict
from numpy.random import choice, random


def anadir_ruido(noise_probability : float, noise_distribution : Dict[str, float]):
    """Agrega ruido

    ### Parameters
    1. noise_probability : float
        - probabilidad de ruido
    2. noise_distribution : Dict[str, float]
        - distribucion de ruido

    """
    def inner_decorator(func):
        possible_noise_values = list(noise_distribution.keys())
        noise_value_probabilities = list(noise_distribution.values())
        @functools.wraps(func)
        def wrapper(*args):
            true_value = func(*args)
            if random() <= noise_probability: #ie con prob `noise_probability`
                vals, probs = exclude_true_value(possible_noise_values,
                                                 noise_value_probabilities,
                                                 true_value)
                return choice(vals, p=probs)
            return true_value
        return wrapper
    return inner_decorator


def exclude_true_value(possible_noise_values,noise_value_probabilities,true_value):
    """Dependiendo de la probabilidad recibida se le agregara ruido al valor

    ### Parameters
    1. possible_noise_values
        - posibles valores de ruido
    2. noise_value_probabilities
        - valor de probabilidad de ruido
    3.true_value
        - bool

    """
    try:
        i = possible_noise_values.index(true_value)
        possible_noise_values = possible_noise_values[:i] + possible_noise_values[i+1:]
        noise_value_probabilities = noise_value_probabilities[:i] + noise_value_probabilities[i+1:]
        sumatoria_prob_ruido = sum(noise_value_probabilities)
        noise_value_probabilities = [x/sumatoria_prob_ruido for x in noise_value_probabilities]
    except ValueError:
        pass
    return possible_noise_values, noise_value_probabilities

if __name__ == "__main__":
    @anadir_ruido(0.5, {'ups!':0.7, 'UPS!':0.3})
    def funcion_de_ejemplo(valor_a_duplicar):
        """Duplica valor recibido

    ### Parameters
    1. x
        - valor a duplicar
    ### Returns
    - 2*x
        - valor duplicado

    """
        return 2*valor_a_duplicar
    for num in range(10):
        print(funcion_de_ejemplo(num))
    