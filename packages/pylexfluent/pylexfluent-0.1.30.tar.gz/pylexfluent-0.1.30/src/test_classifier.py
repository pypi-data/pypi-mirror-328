
import logging
import sys


from lxf.settings import get_logging_level  
###################################################################

logger = logging.getLogger('test classifier')
fh = logging.FileHandler('./logs/test_classifier.log')
fh.setLevel(get_logging_level())
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(get_logging_level())
logger.addHandler(fh)
#################################################################
import os
# System call
os.system("")
# Class of different styles
class print_color():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
from lxf.services.measure_time import measure_time_async
from lxf.services.try_safe import try_safe_execute_asyncio

from lxf.ai.classification.classifier import get_classification
from lxf.domain.predictions import  Predictions
@measure_time_async
async def do_test(file_name) -> Predictions :
    """
    """
    p:Predictions= await get_classification(file_name=file_name)
    if p!=None:
        print(print_color.MAGENTA+f"{file_name} Best Prédiction: {p.BestPrediction} Confidence : {p.BestPredictionConfidence}")
    else :
        print(print_color.RED+f"{file_name} aucune prédiction trouvé")
    print(print_color.BLACK)
    return p
    


if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True) 
    pdf_path = "data/ODP.pdf"
    iban_pdf="data/RIBB.pdf"
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name=iban_pdf) #asyncio.run(do_test(iban_pdf))
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name=pdf_path) #asyncio.run(do_test(pdf_path))
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/ODP_NOTAIRE.pdf")
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/cni.pdf")
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/ODP_Hortensias.pdf")
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/Donation entre époux.pdf")    
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/13 décembre 2024 - Statuts SCI FC2V (CARDONA).pdf")
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/24 juillet 2024 - Testament authentique de Madame LE BRUN née Anne FERRARD.pdf")    
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/CU NANTES 3.pdf") 
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/Certificat d Urbanisme BOURG EN BRESSE 2.pdf") 
    try_safe_execute_asyncio(logger=logger,func=do_test,file_name="data/Certificat d Urbanisme PLUVIGNER 1.pdf") 