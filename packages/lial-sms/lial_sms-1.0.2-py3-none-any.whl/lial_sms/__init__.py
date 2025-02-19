import os
import shutil
import re

from datetime import datetime
import requests

class LialSMS:
    def __init__(self, api_token=None,file_path=None,archive_dir=None,api_url='http://10.0.2.25:5000'):
        """ Initialisation de la classe LialSMS

        :param api_token: le token d'authentification
        :type api_token: str
        :param file_path: le chemin du fichier csv
        :type file_path: str
        :param archive_dir: le répertoire d'archivage
        :type archive_dir: str
        :param api_url: l'URL de base de l'API
        :type api_url: str
        """

        self.api_token = api_token
        self.api_url = api_url
        self.file_path = file_path
        self.archive_dir = archive_dir

    def send_sms_file(self, target, file_path=None):
        """ Envoi des SMS à partir d'un fichier csv

        :param target: le type de cible (SMS-SIMPLE/SMS-MULTIPLE)
        :type target: str
        :param file_path: le chemin du fichier csv
        :type file_path: str
        :return: le résultat de l'envoi
        :rtype: dict
        """

        if file_path:
            pattern = r'^A\d{1,2}LOG\d{4}-\d{8}-\d{7}\.csv$'
            if not re.match(pattern, os.path.basename(file_path)):
                raise ValueError("Invalid file name")
            else:
                self.file_path = file_path
        
        url = f'{self.api_url}/{target}'
        file = {'file': open(self.file_path, 'rb')}
        headers = {
            'Authorization': f'Bearer {self.api_token}'
        }
        response = requests.post(url, files=file, headers=headers)
        
        return response.json()

    def send_sms_params(self, params):
        """ Envoi des SMS à partir des paramètres

        :param params: les paramètres de l'envoi
        :type params: dict
        :return: le résultat de l'envoi
        :rtype: dict
        """

        url = f'{self.api_url}/SMS-SIMPLE'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_token}'
        }
        params_str = '&'.join([f"{key}={value}" for key, value in params.items()])
        url = f"{url}?{params_str}"
        response = requests.post(url, headers=headers)

        return response.json()

    def generate_file(self, file_name, number_list, message, output_dir=rf'C:\Temp',prod_id=None): 
        """ Génère un fichier csv contenant les numéros et les messages à envoyer

        :param file_name: le nom du fichier
        :type file_name: str
        :param number_list: la liste des numéros
        :type number_list: list
        :param message: le message à envoyer
        :type message: str
        :param output_dir: le répertoire de sortie
        :type output_dir: str
        :param prod_id: la liste des prod_id
        :type prod_id: list
        :return: le chemin du fichier généré
        :rtype: str
        """

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        now = datetime.now()
        pattern = r'^A\d{1,2}LOG\d{4}$'
        if re.match(pattern, file_name):
            file_name += f"-{now.strftime('%Y%m%d-%H%M%S')}{int(now.microsecond / 100000)}.csv"
        else:
            raise ValueError("Invalid file name")

        self.file_path = os.path.join(output_dir, file_name)
        
        if prod_id and len(prod_id) < len(number_list):
            raise ValueError("prod_id length cannot be smaller than number_list length")

        message_list_length = len(message)
        number_list_length = len(number_list)
        
        if number_list_length > message_list_length:
            message = [message[0]] * number_list_length
        elif message_list_length == 1:
            message = message * number_list_length

        header = 'Numéro;Texte'
        if prod_id:
            header += ';Prod_id'
        with open(self.file_path, 'w', encoding='utf-8-sig') as file:
            file.write(header+'\n')
            if prod_id:
                for number, msg, p_id in zip(number_list, message, prod_id):
                    line = f'{number};{msg};{p_id}'
                    file.write(line + '\n')
            else:
                for number, msg in zip(number_list, message):
                    line = f'{number};{msg}'
                    file.write(line + '\n')
            
        return self.file_path
    
    def delete_file(self):
        """ Supprime le fichier généré

        :return: True si le fichier est supprimé, False sinon
        :rtype: bool
        """
        try:
            if os.path.exists(self.file_path):
                os.remove(self.file_path) 
                return True
        except Exception as e:
            raise e
    
    def archive_file(self, archive_dir=None):
        """ Archive le fichier généré

        :param archive_dir: le répertoire d'archivage
        :type archive_dir: str
        :return: True si le fichier est archivé, False sinon
        :rtype: bool
        """
        if archive_dir:
            current_archive_dire = archive_dir
        else:
            current_archive_dire = self.archive_dir
        
        
        try :
            if not os.path.exists(current_archive_dire):
                os.makedirs(current_archive_dire)
            shutil.move(self.file_path, current_archive_dire)
            return True
        except Exception as e:
            raise e
        
    
    def get_token(self, username, password):
        """ Récupère le token d'authentification
        
        :param username: le nom d'utilisateur
        :type username: str
        :param password: le mot de passe
        :type password: str
        :return: le token d'authentification
        :rtype: dict
        """
        
        url = f'{self.api_url}/login'
        headers = {
            'Content-Type': 'application/json'
        }
        url = f"{url}?username={username}&password={password}"
        response = requests.post(url,  headers=headers)
        return response.json()


