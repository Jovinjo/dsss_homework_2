from setuptools import setup

setup(
   name='math_quiz',
   version='2.0',
   description='A math quiz game',
   author='Jonathan Vincent',
   author_email='jonathan.vincent@fau.de',
   packages=['math_quiz'],  #same as name
   entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',
        ],
    },
)