# FEN_tensorflow

# Usage
- Upload your PNG to the website 
- Wait for the model to evaluate the input

# Cloning/Training
If you want to train the model yourself

- Import your own PNGs or generate them with: 
```python
pip install -r requirements.txt
```
```python
python training_data_generator.py
```
```python
python create_model.py
```
Then convert the model to one usable by TensorFlowJS
```sh
pip install tensorflowjs
tensorflowjs_converter --input_format tf_saved_model [path to models/] [output dir]
```
