import asyncio
from datetime import datetime, timezone
import os
import pathlib
import uuid

from lxf.ai.classification.multiclass.jupiter_model import MulticlassClassificationJupiterModel

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
    
import logging
import lxf.settings as settings
settings.set_logging_level(logging.INFO)

settings.enable_tqdm=False
logger = logging.getLogger('Train classifier')
fh = logging.FileHandler('./logs/train_classifier.log')
fh.setLevel(settings.get_logging_level())
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(settings.get_logging_level())
logger.addHandler(fh)
#####################################################
from lxf.ai.ocr.ocr_pdf import do_ocr_directory
from lxf.domain.TrainingData import DocumentTrainingData
from lxf.ai.classification.classifier import extract_text_from_file
from lxf.domain.keyswordsandphrases import KeysWordsAndPhrases
from lxf.repositories.training_repository import LexiaDb, TrainingDataRepository
import argparse
import pandas as pd

conn_str =os.getenv('MONGO_DB') #"mongodb://mongoadmin:Babaefface!2022@lexiadb:28017"
if conn_str==None :
    conn_str = 'mongodb://root:Phocea!123@localhost:37017'

async def ocr_files(root:str,dest_folder:str):
    print(print_color.GREEN+f"Prepare data from {root} to {dest_folder}")
    if os.path.exists(dest_folder) == False :
        os.mkdir(dest_folder)
    do_ocr_directory(root,dest_folder)

async def do_process_files(root:str,dest_folder:str):
    print(print_color.MAGENTA+f"Training started")
    await ocr_files(root,dest_folder)
    print(print_color.BLACK+f"Training complete")

async def do_create_dataset(root:str, model:str)->tuple[bool,int]:
    """
    Create a dataset from files
    insert all data in database
    """
    print(print_color.MAGENTA+f"Creating the dataset model {model} from {root}")
    lexiaDb:LexiaDb=LexiaDb(conn_str)
    tdr:TrainingDataRepository=TrainingDataRepository(lexia_db=lexiaDb)
    binserted=False
    count=0
    for root,dir, files in os.walk(root):
        if files!=[] :
            for file in files :
                data:dict=dict()
                tmp = file.split('#')
                tmp_classname:str=tmp[0].split('_')
                filename = f'{root}/{file}'
                # Extraction du texte
                result = await extract_text_from_file(file_name=filename)
                if result == None or result == '':
                    logger.warning(f"Echec de l'extraction du texte pour {filename}")
                else:      
                    keysWordsPhrasesHelper: KeysWordsAndPhrases = KeysWordsAndPhrases(result)
                    freq_mots = keysWordsPhrasesHelper.get_key_words(isSorted=True)
                    if freq_mots != None:
                        data['key_words']=freq_mots
                        data['key_phrases']=None
                        data['parent_id']='-1'
                        data['model']=model
                        data['sid']="0"
                        data['name']=tmp[1]
                        data['famille']=tmp_classname[0]
                        data['category']=tmp_classname[1]
                        data['sub_category']=tmp_classname[2]                    
                        documentTD:DocumentTrainingData=DocumentTrainingData(data)
                        filter = {"name": tmp[1]}   
                        item_result = tdr.insertOrUpdate(filter,documentTD)
                        if item_result!=None :
                            binserted=True
                            count+=1
    return binserted, count                

async def do_get_training_data(model:str)->tuple[int, pd.DataFrame]:
    """
    Get the data from LexiaDB
    """
    print(print_color.MAGENTA+f"Getting the dataset model {model} from LexiaDB")
    lexiaDb:LexiaDb=LexiaDb(conn_str)
    tdr:TrainingDataRepository=TrainingDataRepository(lexia_db=lexiaDb )
    count:int=0
    filter = {"model": model.strip()}
    items = tdr.get_byfilter(filter=filter)
    if items !=None :
        dataset= pd.DataFrame(items)
        return dataset.size, dataset
        # dataset:list[DocumentTrainingData] =[]
        # for item in items :
        #     data:DocumentTrainingData = DocumentTrainingData(item)
        #     dataset.append(data)
        # return len(dataset), dataset
    else :
        logger.debug(f"Aucune donnée pour le modèle {model}")
        return 0,None   

async def do_train_multiclass(dataset:list[DocumentTrainingData],model_name)->bool :
    """
    Entraine le modèle avec le jeux données fourni
    """
    model:MulticlassClassificationJupiterModel = MulticlassClassificationJupiterModel()
    return model.train(dataset=dataset,ModelName=model_name)!=None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exemple d'usage")
    parser.add_argument("--Source","-s",nargs=1,required=False,type=str,help="Dossier arborescence Familles à traiter, exemple: --Source ./Familles")
    parser.add_argument("--Output","-o",nargs=1,required=False,type=str, help="Dossier contenant tous les fichiers traités, exemple: --Output ./Famille_ocred")
    parser.add_argument("--Model","-m",nargs=1,type=str, required=True, help="Nom du modèle, exemple : --Model JupiterB1")
    parser.add_argument("--All","-a",nargs="?",type=bool,default=True, help="Execute tous les traitements, exemple: --All True [Defaut=True]")
    parser.add_argument("--OcrOnly","-ocr", nargs="?",type=bool, default=False,help="Execute uniquement l'OCR, exemple: --OcrOnly True [Defaut=False]")
    parser.add_argument("--DatasetOnly","-ds",nargs="?",type=bool,default=False, help="Execute uniquement l'insertion du dataset, exemple : --DatasetOnly True [Defaut=False]")
    parser.add_argument("--Train","-t",nargs="?",type=bool, default=True, help="Entraine le modèle, exemple : --Train ")
    args = parser.parse_args()
    if args.Source !=None:
        source_folder:str=args.Source[0]
    else : source_folder="Non défini"
    if args.Output!=None:
        output_folder:str = args.Output[0]
    else : output_folder="Non défini"
    model:str=args.Model[0] 
    ocr_only:bool=args.OcrOnly
    dataset_only:bool=args.DatasetOnly
    train:bool = args.Train
    all:bool = args.All and ocr_only== False and dataset_only==False and train==False 
    print(print_color.YELLOW+f"Paramètres d'exécution\n\t\tSource:{source_folder} Output: {output_folder} Modèle: {model}\n\t\tForce: {all} OcrOnly: {ocr_only} DatasetOnly: {dataset_only} Train {train}")
    if all or ocr_only :
        print(print_color.BLUE+f"Prepararing files")
        asyncio.run(do_process_files(source_folder,output_folder))
    if all or dataset_only :    
        print(print_color.RED+"Creating dataset")
        binserted:bool=False
        count:int=0
        binserted,count= asyncio.run(do_create_dataset(output_folder,model))
        if binserted: 
            print(print_color.GREEN+f"{count} enregistrements ajoutés")
        else: 
            print(print_color.RED+"Aucun enregistrement")
    if all or train:
        print(print_color.CYAN+f"Récupération des données d'entrainement du {model}")
        count,dataset = asyncio.run(do_get_training_data(model=model))
        if dataset.empty==False and count !=0:
            print(print_color.BLUE+f"Début de l'entrainement du modèle {model} avec {count} données" )
            is_trained= asyncio.run(do_train_multiclass(dataset=dataset,model_name=model))
            if is_trained : success = "Entrainement réussi"
            else : success="L'entrainement à échoué"
            print(f"Fin de l'entrainement du modèle {model}. Résultat : {success} ")
        else :
            print(print_color.RED+f"Aucune donnée d'entrainement récupéré pour le modèle {model}")
    # terminé
    print(print_color.BLACK)            
        