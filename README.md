# FEN_tensorflow

# Usage
- Upload your PNG to the website 
- Wait for the model to evaluate the input

# Cloning/Training
If you want to train the model yourself

- Import your own PNGs or generate them with: 
```powershell
pip install -r requirements.txt
```


Generates 1000 chess boards then splits them each into 64 individual pieces
```powershell
python training_data_generator.py
```
Creates a new model and trains it with the data we just created
```powershell
python create_model.py
```
Converts the model to one usable by TensorFlowJS .pb -> JSON
```powershell
pip install tensorflowjs
tensorflowjs_converter --input_format tf_saved_model [path to models/] [output dir]
```

# Acknowledgements
- Inspiration from [ChessboardFenTensorflowJs](https://github.com/Elucidation/ChessboardFenTensorflowJs) by [Elucidation](https://github.com/Elucidation)
