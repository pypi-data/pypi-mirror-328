from .bqfuntions import BigQueryTableUpdater, logging
from connections.connect import GoogleCloudConnection

import pandas as pd
import uuid

from io import BytesIO
from datetime import datetime

class AuditLogs:
    @staticmethod
    def add_logs(
                ID_LOG,
                TRACKER_ID,
                NM_PROJECT,
                NM_STEP,
                GCP_TECNOLOGY,
                NM_TYPE_SOURCE,
                NM_SOURCE,
                NM_TYPE_TARGET,
                NM_TARGET_STEP,
                NM_TARGET_PATH,
                QT_FILES,
                QT_ROWS_OK,
                QT_ROWS_NOK,
                TS_START,
                TS_FINISH
    ):
        return {
            'ID_LOG': ID_LOG,
            'TRACKER_ID': TRACKER_ID,
            'NM_PROJECT': NM_PROJECT,
            'NM_STEP': NM_STEP,
            'GCP_TECNOLOGY': GCP_TECNOLOGY,
            'NM_TYPE_SOURCE': NM_TYPE_SOURCE,
            'NM_SOURCE': NM_SOURCE,
            'NM_TYPE_TARGET': NM_TYPE_TARGET,
            'NM_TARGET_STEP': NM_TARGET_STEP,
            'NM_TARGET_PATH': NM_TARGET_PATH,
            'QT_FILES': QT_FILES,
            'QT_ROWS_OK': QT_ROWS_OK,
            'QT_ROWS_NOK': QT_ROWS_NOK,
            'TS_START': TS_START,
            'TS_FINISH': TS_FINISH,    
        }

class BigQueryIngestion:

    def __init__(self, project_id: str, yaml_file: str, bucket_name: str, nm_project: str, sa_email=None):
        """
        Inicializa o BigQueryIngestion com o ID do projeto, o arquivo YAML, o nome do bucket e o nome do projeto a ser monitorado.
        
        Args:
            project_id (str): ID do projeto no Google Cloud. Usado para identificar o projeto de destino no BigQuery e Google Cloud Storage.
            sa_email (str, opcional): Email da Service Account de destino para impersonação. Se não fornecido, a autenticação padrão do Google Cloud será usada.
            yaml_file (str): Caminho para o arquivo YAML de configuração que pode conter parâmetros adicionais para o processo de ingestão de dados.
            bucket_name (str): Nome do bucket no Google Cloud Storage onde os arquivos a serem ingeridos estão armazenados.
            nm_project (str): Nome do projeto que será monitorado ou que é relevante para o processo de ingestão de dados.
        """
        try:
            # Armazena o project_id como um atributo da classe
            self.project_id = project_id
            self.bucket_name = bucket_name

            # Nome do projeto que será monitorado
            self.nm_project = nm_project

            # Inicializa a classe BigQueryTableUpdater como um atributo da classe
            self.bq_updater = BigQueryTableUpdater(project_id, sa_email, yaml_file)
            
            # Inicializa a classe de conexão e armazena as conexões nos atributos
            connections = GoogleCloudConnection(sa_email, project_id)
            self.bigquery_client = connections.get_bigquery_client()
            self.storage_client = connections.get_storage_client()
            
        except Exception as e:
            logging.error(f"Erro ao inicializar o cliente BigQuery para o projeto {self.project_id}: {str(e)}")
            raise

    def get_qtd_files(self, path: str):
        """
        Conta a quantidade de arquivos em uma pasta específica no Google Cloud Storage.

        Args:
            path (str): Caminho da pasta dentro do bucket no Google Cloud Storage.

        Returns:
            int: Quantidade de arquivos encontrados na pasta especificada, excluindo diretórios.

        Exceções:
            Levanta exceção caso ocorra um erro ao acessar o bucket ou listar os arquivos.
        """
        try:
            # Nome do bucket e caminho da pasta no GCS
            bucket_name = self.bucket_name
            prefix = f'{path}/'

            logging.info(f"Iniciando contagem de arquivos na pasta: {prefix} no bucket: {bucket_name}")

            # Cria um cliente do Google Cloud Storage
            client = self.storage_client

            # Acessa o bucket especificado
            bucket = client.bucket(bucket_name)

            # Lista todos os blobs (arquivos) com o prefixo especificado
            blobs = list(bucket.list_blobs(prefix=prefix))
            logging.info(f"Total de blobs encontrados no caminho {prefix}: {len(blobs)}")

            # Filtra para contar apenas blobs que não terminam com "/" (ignorando diretórios)
            arquivos_reais = [blob for blob in blobs if not blob.name.endswith('/')]
            logging.debug(f"Total de arquivos reais (excluindo diretórios): {len(arquivos_reais)}")

            # Conta o número de arquivos
            total_arquivos = len(arquivos_reais)

            logging.info(f"Quantidade de arquivos na pasta '{prefix}' do bucket '{bucket_name}': {total_arquivos}")
            return total_arquivos

        except Exception as e:
            logging.error(f"Erro ao contar arquivos na pasta {prefix} do bucket {bucket_name}: {e}", exc_info=True)
            raise  # Propaga a exceção para ser capturada pelo Airflow

    def get_volumetria(self, path):
        try:
            # Nome do bucket e caminho da pasta no GCS
            bucket_name = self.bucket_name
            prefix = f'{path}/'

            logging.info(f"Iniciando a análise da volumetria na pasta: {prefix} no bucket: {bucket_name}")

            # Cria um cliente do Google Cloud Storage
            client = self.storage_client

            # Acessa o bucket especificado
            bucket = client.bucket(bucket_name)

            # Lista todos os blobs (arquivos) com o prefixo especificado
            blobs = list(bucket.list_blobs(prefix=prefix))
            logging.info(f"Total de arquivos encontrados no caminho {prefix}: {len(blobs)}")

            total_linhas = 0

            # Para cada arquivo na pasta
            for blob in blobs:
                if blob.name.endswith('.csv'):  # Verifica se o arquivo é CSV
                    logging.info(f"Processando arquivo CSV: {blob.name}")

                    # Processa arquivo grande linha por linha
                    with blob.open("r") as file_obj:
                        linhas = sum(1 for _ in file_obj)
                        total_linhas += linhas

                    logging.info(f"Arquivo CSV: {blob.name} - Linhas: {linhas}")

                elif blob.name.endswith('.txt'):  # Verifica se o arquivo é TXT
                    logging.info(f"Processando arquivo TXT grande: {blob.name}")

                    # Processa arquivo grande linha por linha
                    with blob.open("r") as file_obj:
                        linhas = sum(1 for _ in file_obj)
                        total_linhas += linhas

                    logging.info(f"Arquivo TXT: {blob.name} - Linhas: {linhas}")

                elif blob.name.endswith('.parquet'):  # Verifica se o arquivo é Parquet
                    logging.info(f"Processando arquivo Parquet: {blob.name}")

                    # Faz o download do conteúdo do arquivo Parquet em partes
                    parquet_data = blob.download_as_bytes()
                    logging.debug(f"Conteúdo do arquivo Parquet {blob.name} baixado com sucesso")

                    # Usa pandas para carregar e contar as linhas
                    df = pd.read_parquet(BytesIO(parquet_data))
                    linhas = len(df)
                    total_linhas += linhas

                    logging.info(f"Arquivo Parquet: {blob.name} - Linhas: {linhas}")

                else:
                    logging.warning(f"Formato de arquivo desconhecido: {blob.name}, ignorando...")

            logging.info(f"Quantidade total de linhas em todos os arquivos: {total_linhas}")
            return total_linhas

        except Exception as e:
            logging.error(f"Erro ao processar arquivos na pasta {prefix}: {e}", exc_info=True)
            raise
        
    def _generate_uuid(self):
        return str(uuid.uuid4())  # Gerar um UUID único 

    def add_metadados(self, camada_processamento, tecnologia, nm_type_source, path_source, nm_type_target,
                      camada_destino, path_destino, volumetria, lines_nok, tracker_id, start_time, ts_finish, qtd_files):
        hash_uuid = self._generate_uuid()

        # Adicionar metadados aos logs
        return AuditLogs.add_logs(
            hash_uuid,
            tracker_id,
            str(self.nm_project),  # Nome do Projeto
            camada_processamento,  # Nome da camada de processamento
            tecnologia,  # Nome da tecnologia usada
            nm_type_source,  # Tipo do source
            path_source,  # Nome do Source
            nm_type_target,  # Tipo de destino
            camada_destino,  # Nome do step destino
            path_destino,  # Caminho do destino
            qtd_files,  # Total de arquivos processados
            volumetria,  # Total de linhas OK
            lines_nok,
            start_time,
            ts_finish
        )

    def write_to_bigquery(self, logs_data):
        """
        Insere os dados de log na tabela do BigQuery de acordo com o schema e a tabela
        definidos no arquivo YAML.
        
        Args:
            logs_data (dict): Dados de log a serem inseridos.
            yaml_file (str): Caminho para o arquivo YAML que contém o schema e as tabelas.
            table_name (str): Nome da tabela onde os dados serão inseridos.
        """
        # Carregar o schema e as tabelas do YAML
        schema, tables = self.bq_updater.load_schema_and_tables_from_yaml()

        if not tables:
            logging.error("Nenhuma tabela foi encontrada no arquivo YAML.")
            raise ValueError("Arquivo YAML não contém tabelas.")

        # Procurar a tabela pelo nome
        table_info = next((table for table in tables if table['name'] == "tl_ingestions"), None)
        if not table_info:
            logging.error(f"Tabela 'tl_ingestions' não encontrada no YAML.")
            raise ValueError(f"Tabela 'tl_ingestions' não encontrada no YAML.")

        # Definir o dataset e a tabela de destino
        dataset_id = schema  # O dataset vem do campo "schema" do YAML
        table_id = table_info['name']

        # Inicializar o cliente do BigQuery
        client = self.bigquery_client

        # Criar uma referência à tabela no BigQuery
        table_ref = client.dataset(dataset_id).table(table_id)

        # Configurar a inserção no BigQuery
        try:
            errors = client.insert_rows_json(table_ref, [logs_data])
            if errors:
                logging.error(f"Erro ao inserir logs no BigQuery: {errors}")
            else:
                logging.info("Logs inseridos com sucesso no BigQuery.")
        except Exception as e:
            logging.error(f"Erro durante a inserção no BigQuery: {str(e)}")
            raise e

    def pegar_timestamp_atual(self):
        """
        Retorna o timestamp atual em segundos.
        """
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def run(self, folder_path_monitoring, camada_processamento, tecnologia, nm_type_source, path_source, nm_type_target,
            camada_destino, path_destino, step_1, step_2, tracker_id):
        
        # Log - Início do processo
        logging.info("Processo run iniciado.")

        # Obter o start_time
        logging.info("Iniciando obtenção do start_time.")
        start_time = self.pegar_timestamp_atual()
        logging.info(f"Start time obtido: {start_time}.")

        # Usar o TRACKER passado como argumento
        logging.info(f"TRACKER ID recebido: {tracker_id}.")

        # Calcular volumetria
        logging.info("Iniciando cálculo da volumetria.")
        volumetria = self.get_volumetria(folder_path_monitoring)
        logging.info(f"Volumetria calculada: {volumetria}.")

        # Quantidade de arquivos
        logging.info("Iniciando cálculo da quantidade de arquivos.")
        qtd_files = self.get_qtd_files(folder_path_monitoring)
        logging.info(f"Quantidade de arquivos calculada: {qtd_files}.")

        # Obter o end_time
        logging.info("Iniciando obtenção do end_time.")
        ts_finish = self.pegar_timestamp_atual()  # Obter o tempo final
        logging.info(f"End time obtido: {ts_finish}.")

        # Lines No OK
        logging.info("Iniciando cálculo de lines no OK.")
        lines_nok = self.bq_updater.get_qt_rows_ok_difference(tracker_id, step_1, step_2, volumetria=volumetria)
        logging.info(f"Lines no OK calculadas: {lines_nok}.")

        # Gerar e adicionar os metadados
        logging.info("Iniciando a geração e adição de metadados.")
        logs_data = self.add_metadados(camada_processamento, tecnologia, nm_type_source, path_source, nm_type_target,
                                        camada_destino, path_destino, volumetria, lines_nok, tracker_id, start_time, ts_finish, qtd_files)
        logging.info("Metadados gerados e adicionados.")

        # Escrever os logs no BigQuery
        logging.info("Iniciando escrita dos logs no BigQuery.")
        self.write_to_bigquery(logs_data)
        logging.info("Logs escritos no BigQuery.")

        # Log - Final do processo
        logging.info("Processo run finalizado.")