import logging
import os
import yaml
import sys

from google.cloud import bigquery
from google.api_core.exceptions import NotFound 

# Adiciona o diretório 'functions' ao sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
functions_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(functions_dir)

from connections.connect import GoogleCloudConnection

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class BigQueryTableUpdater:

    def __init__(self, project_id: str, sa_email=None, yaml_file=None):
        """
        Inicializa o BigQueryTableUpdater com o ID do projeto e o arquivo YAML.
        
        Args:
            project_id (str): ID do projeto no Google Cloud.
            sa_email (str): Email da Service Account de destino para impersonação.
            yaml_file (str): Caminho para o arquivo YAML de configuração.
        """
        try:
            # Armazena o project_id como um atributo da classe
            self.project_id = project_id
            
            # Armazena o caminho do arquivo YAML como atributo
            self.yaml_file = yaml_file

            # Inicializa a classe de conexão e armazena as conexões nos atributos
            connections = GoogleCloudConnection(project_id, sa_email)
            self.bigquery_client = connections.get_bigquery_client()

            # Log para verificar se o caminho do arquivo foi montado corretamente
            logger.info(f"YAML file path: {self.yaml_file}")

        except Exception as e:
            logger.error(f"Erro ao inicializar o cliente BigQuery para o projeto {self.project_id}: {str(e)}")
            raise
            
            

    def load_schema_and_tables_from_yaml(self):
        """
        Carrega o schema e as tabelas com suas descrições a partir de um arquivo YAML.
        
        Args:
            yaml_file (str): Caminho para o arquivo YAML.
        
        Returns:
            tuple: (schema, lista de tabelas)
        """
        try:
            with open(self.yaml_file, 'r') as file:
                data = yaml.safe_load(file)
            logger.info(f"YAML '{self.yaml_file}' carregado com sucesso.")
            
            # Extraindo as informações do YAML
            schema = data.get('schema', '')
            tables = data.get('tables', [])
            
            return schema, tables
        
        except FileNotFoundError as fnf_error:
            logger.error(f"Arquivo YAML não encontrado: {self.yaml_file}")
            raise fnf_error
        except yaml.YAMLError as yaml_error:
            logger.error(f"Erro ao ler o arquivo YAML: {str(yaml_error)}")
            raise yaml_error
        except Exception as e:
            logger.error(f"Erro inesperado ao carregar o arquivo YAML: {str(e)}")
            raise

    def set_table_and_column_descriptions(self, table_name):
        """
        Atualiza descrições de uma tabela e suas colunas no BigQuery a partir de um arquivo YAML.
        
        Args:
            table_name (str): Nome da tabela a ser atualizada.
        """
        try:
            # Carregar o schema e as tabelas do YAML
            schema, tables = self.load_schema_and_tables_from_yaml(self.yaml_file)

            # Filtrar a tabela pelo nome fornecido
            table_info = next((table for table in tables if table.get('name') == table_name), None)
            
            if not table_info:
                raise ValueError(f"Tabela '{table_name}' não encontrada no YAML.")

            table_description = table_info.get('table_description', '')
            column_descriptions = table_info.get('columns', {})

            # Referência para a tabela no schema
            table_ref = self.bigquery_client.dataset(schema).table(table_name)
            table = self.bigquery_client.get_table(table_ref)

            # Definir a descrição da tabela
            table.description = table_description

            # Atualizar descrições de colunas e tipos de dados
            schema_fields = []
            for field in table.schema:
                if field.name in column_descriptions:
                    # Extraindo a descrição e o tipo de dado (type_data) do YAML
                    column_info = column_descriptions[field.name]
                    field_description = column_info.get('description', field.description)
                    field_type = column_info.get('type_data', field.field_type)  # Usa o 'type_data' do YAML, se presente
                    
                    # Atualiza o campo da coluna
                    field = bigquery.SchemaField(
                        name=field.name, 
                        field_type=field_type, 
                        mode=field.mode, 
                        description=field_description
                    )
                schema_fields.append(field)

            table.schema = schema_fields

            # Atualizar a tabela no BigQuery
            updated_table = self.bigquery_client.update_table(table, ['description', 'schema'])
            
            logger.info(f"Tabela '{table_name}' no schema '{schema}' atualizada com sucesso. Descrição: {updated_table.description}")
            for field in updated_table.schema:
                logger.info(f"Coluna: {field.name}, Tipo: {field.field_type}, Descrição: {field.description}")

        except NotFound as not_found_error:
            logger.error(f"Tabela ou dataset '{table_name}' não encontrados: {str(not_found_error)}")
            raise not_found_error
        except Exception as e:
            logger.error(f"Erro ao atualizar descrições no BigQuery: {str(e)}")
            raise

    def generate_schema_string_from_yaml(self, table_name):
        """
        Gera uma string de schema a partir de um arquivo YAML para uma tabela específica.
        
        Args:
            table_name (str): Nome da tabela da qual extrair o schema.
        
        Returns:
            str: Uma string representando o schema para uso no WriteToBigQuery.
        
        Raises:
            ValueError: Se a tabela não for encontrada no YAML.
        """
        try:
            #Varificar se tabela está criada.
            #self.create_table_if_not_exists(yaml_file,table_name)

            with open(self.yaml_file, 'r') as file:
                data = yaml.safe_load(file)
            
            schema_parts = []
            table_found = False
            
            # Iterar sobre as tabelas no YAML
            for table in data.get('tables', []):
                if table.get('name') == table_name:
                    table_found = True
                    columns = table.get('columns', {})
                    
                    # Criar a representação do schema para cada coluna
                    for column_name, column_info in columns.items():
                        field_type = column_info.get('type_data', 'STRING')  # Usar STRING como padrão
                        schema_parts.append(f"{column_name}:{field_type}")
                    
                    break  # Encontrou a tabela, não precisa continuar iterando
            
            if not table_found:
                raise ValueError(f"Tabela '{table_name}' não encontrada no arquivo YAML.")
            
            # Juntar todos os campos em uma string
            schema_string = ', '.join(schema_parts)
            return schema_string
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo YAML não encontrado: {self.yaml_file}")
        except yaml.YAMLError as e:
            raise ValueError(f"Erro ao ler o arquivo YAML: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Erro inesperado: {str(e)}")
        
    def create_table_if_not_exists(self, table_name):
        """
        Cria uma tabela no BigQuery a partir de um arquivo YAML se ela não existir.
        
        Args:
            table_name (str): Nome da tabela a ser criada.
        
        Raises:
            ValueError: Se a tabela não puder ser criada devido a erros.
        """
        try:
            # Carregar o YAML
            with open(self.yaml_file, 'r') as file:
                data = yaml.safe_load(file)

            # Obter informações do esquema
            schema_name = data.get('schema')
            tables = data.get('tables', [])

            # Encontrar a tabela com o nome fornecido
            table_info = next((table for table in tables if table['name'] == table_name), None)

            if table_info is None:
                raise ValueError(f"Tabela '{table_name}' não encontrada no YAML.")

            columns = table_info.get('columns', {})
            table_id = f"{self.project_id}.{schema_name}.{table_name}"

            try:
                # Verificar se a tabela já existe
                self.bigquery_client.get_table(table_id)
                logger.info(f"A tabela '{table_name}' já existe.")
            except NotFound:
                # A tabela não existe, então vamos criá-la
                schema_fields = []

                for column_name, column_info in columns.items():
                    field_type = column_info.get('type_data', 'STRING')  # Usar STRING como padrão
                    field = bigquery.SchemaField(name=column_name, field_type=field_type)
                    schema_fields.append(field)

                # Criar a tabela
                table = bigquery.Table(table_id, schema=schema_fields)
                table.description = table_info.get('table_description', '')
                self.bigquery_client.create_table(table)  # Cria a tabela
                logger.info(f"Tabela '{table_name}' criada com sucesso no dataset '{schema_name}'.")

                # Atualizar descrições da tabela caso tenha no arquivo YML
                self.set_table_and_column_descriptions(table_name)

        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo YAML não encontrado: {self.yaml_file}")
        except yaml.YAMLError as e:
            raise ValueError(f"Erro ao ler o arquivo YAML: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Erro inesperado: {str(e)}")

    def get_trackerid_logs(self, nm_project):

        try:
            query_tracker = f"""
            select max(tracker_id)from `{self.project_id}.dados_alternativos.tl_ingestions`
            where nm_project = '{nm_project}'
            """

            result = self.bigquery_client.query(query_tracker)
            
            for row in result:
                if  row[0]:    
                    tracker_id = int(row[0])+1
                else:
                    tracker_id = 1

            return tracker_id

        except Exception as e:
            logger.info(f"Erro execução query {e}")

    def get_qt_rows_ok_difference(self, tracker_id, step_1, step_2, volumetria, nm_project):
        """
        Consulta o BigQuery para obter os valores de qt_rows_ok para dois steps fornecidos
        e calcula a diferença entre eles, garantindo que a diferença não seja negativa.

        Parâmetros:
        - tracker_id: ID do tracker para filtrar o registro.
        - step_1: Nome do primeiro step (por exemplo, "RAW" ou "TRUSTED").
        - step_2: Nome do segundo step (por exemplo, "TRUSTED" ou "REFINED").

        Retorna:
        - A diferença entre qt_rows_ok dos steps fornecidos (sempre positiva ou zero).
        """
        client = bigquery.Client(project=self.project_id)

        query = f"""
        SELECT nm_step, qt_rows_ok
        FROM `{self.project_id}.dados_alternativos.tl_ingestions`
        WHERE tracker_id = @tracker_id AND nm_project = "{nm_project}" AND nm_step IN (@step_1)
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("tracker_id", "INT64", tracker_id),
                bigquery.ScalarQueryParameter("step_1", "STRING", step_1),
                # bigquery.ScalarQueryParameter("step_2", "STRING", step_2)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()

        # Inicializa com 0 para cada step, caso não seja encontrado na consulta
        values = {step_1: 0}
        values.update({row["nm_step"]: row["qt_rows_ok"] for row in results})

        step_1_qt_rows_ok = values.get(step_1, 0)
        step_2_qt_rows_ok = int(volumetria)

        # Log para os valores de qt_rows_ok
        logging.info(f"Valores encontrados: {values}")

        # Log para steps não encontrados
        if step_1_qt_rows_ok == 0:
            logging.warning(f"Step '{step_1}' não encontrado para tracker_id {tracker_id}.")
        
        if step_2_qt_rows_ok == 0:
            logging.warning(f"Step '{step_2}' não encontrado para tracker_id {tracker_id}.")

        # Calcula a diferença absoluta para garantir que não seja negativa
        if step_1 == "RAW":
            difference = 0
            logging.warning("Step 'RAW' linhas nok 0.")
        else:
            difference = abs(step_1_qt_rows_ok - step_2_qt_rows_ok)

        logging.info(f"Diferença entre {step_1} e {step_2}: {difference}")
        return difference

