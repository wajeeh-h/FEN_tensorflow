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
```powershell
python training_data_generator.py
```
```powershell
python create_model.py
```
Then convert the model to one usable by TensorFlowJS
```powershell
pip install tensorflowjs
tensorflowjs_converter --input_format tf_saved_model [path to models/] [output dir]
```

# Acknowledgements
- Inspiration from [ChessboardFenTensorflowJs](https://github.com/Elucidation/ChessboardFenTensorflowJs) by [Elucidation](https://github.com/Elucidation)
