# FEN_tensorflow

# Usage
- Upload your PNG to the website 
- Wait for the model to evaluate the input

# Results
Input:

![Input](https://i.ibb.co/RY1x4tf/image.png)

Output: r1bqkbnr/1ppp1ppp/p1n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R

Accuracy: 99.87% Estimated 100% Actual

![Output](https://i.ibb.co/sP75P2G/68747470733a2f2f692e6962622e636f2f7a73707a4b637a2f696d6167652e706e67.png)

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
