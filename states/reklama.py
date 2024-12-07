from aiogram.fsm.state import State, StatesGroup

class Adverts(StatesGroup):
    adverts = State()

class Reklama(StatesGroup):
    rasm  = State()
    nomi = State()
    xotira = State()
    kamera = State()
    dakument = State()
    rang = State()
    narx = State()
    holati = State()
    tel = State() 
    tg_user = State()
    shahar = State()
    abmen = State()
    qushmch_m = State()

