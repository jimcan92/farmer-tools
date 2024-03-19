from multiprocessing import freeze_support
from uvicorn import run

if __name__ == '__main__':
    freeze_support()
    run('src:app', reload=True)