import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.predictor import AgePredictor
from PIL import Image
from io import BytesIO

app = FastAPI()
predictor = AgePredictor()

# Allow all origins for simplicity. Adjust this based on your security requirements.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get('/api/test', tags=['request'])
def test():
    print('Hello')
    return {'result': 'Test Called'}

@app.post('/api/age', tags=['request'])
async def process(files: list[UploadFile] = File(...)):
    result = {}
    print('Process called')
    for file in files:
        request_object_content = await file.read()
        img = Image.open(BytesIO(request_object_content))
        pred = predictor.predict_age(image=img)
        result[file.filename] = pred
    return {'result': result}

@app.post('/api/sf', tags=['request'])
async def process(file: UploadFile = File(...)):
    result = {}
    print('Process called')
    request_object_content = await file.read()
    img = Image.open(BytesIO(request_object_content))
    pred = predictor.predict_age(image=img)
    result[file.filename] = pred
    return {'result': result}

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=4000,
        reload=True,
#        ssl_keyfile='/etc/letsencrypt/live/jpegresize.xyz/privkey.pem',
#        ssl_certfile='/etc/letsencrypt/live/jpegresize.xyz/cert.pem'
    )
