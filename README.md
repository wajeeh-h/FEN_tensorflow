# FEN_tensorflow

# Usage
- Upload your PNG to the website 
- Wait for the model to evaluate the input

# Cloning/Training
If you want to train the model yourself
- Import your own PNGs or generate them: 

Install Requirements
```powershell
pip install -r requirements.txt
```
Generate n chess boards then split them each into 64 images
```powershell
python training_data_generator.py
```
Create a new model and train it with the data we just created
```powershell
python create_model.py
```
Convert the model to one usable by TensorFlowJS .pb -> JSON
```powershell
pip install tensorflowjs
tensorflowjs_converter --input_format tf_saved_model [path to models/] [output dir]
```

# Acknowledgements
- Inspiration from [ChessboardFenTensorflowJs](https://github.com/Elucidation/ChessboardFenTensorflowJs) by [Elucidation](https://github.com/Elucidation)
