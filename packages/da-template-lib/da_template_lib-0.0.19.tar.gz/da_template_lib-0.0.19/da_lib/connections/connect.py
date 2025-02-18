import google.auth
from google.auth import impersonated_credentials
from google.cloud import bigquery, storage
import logging

logger = logging.getLogger(__name__)

class GoogleCloudConnection:
    def __init__(self, project_id: str, target_sa_email=None):
        """
        Inicializa a classe de conexão com o BigQuery e Google Cloud Storage.
        Se a Service Account (SA) for fornecida, ela será utilizada para a conexão.
        Caso contrário, será utilizada a autenticação padrão.

        Args:
            target_sa_email (str, opcional): Email da Service Account de destino para impersonação. Se não fornecido, a autenticação padrão será usada.
            project_id (str, opcional): ID do projeto. Se não fornecido, será obtido a partir das credenciais.
        """
        try:
            if target_sa_email:
                # Autenticação com Service Account fornecida
                credentials, _ = google.auth.default()

                # Definir as credenciais impersonadas com o escopo necessário
                target_credentials = impersonated_credentials.Credentials(
                    source_credentials=credentials,  # Credenciais da SA de origem
                    target_principal=target_sa_email,  # Email da SA de destino
                    target_scopes=['https://www.googleapis.com/auth/cloud-platform'],  # Escopo de acesso necessário
                )

                # Inicializa o cliente do BigQuery com as credenciais impersonadas
                self.bigquery_client = bigquery.Client(credentials=target_credentials, project=project_id)
                logger.info(f"Conexão BigQuery estabelecida para o projeto {project_id}")

                # Inicializa o cliente do Google Cloud Storage com as credenciais impersonadas
                self.storage_client = storage.Client(credentials=target_credentials, project=project_id)
                logger.info(f"Conexão Google Cloud Storage estabelecida para o projeto {project_id}")

            else:
                # Caso a SA não seja fornecida, usa a autenticação padrão
                self.bigquery_client = bigquery.Client(project=project_id)
                logger.info(f"Conexão BigQuery estabelecida para o projeto {project_id} com autenticação padrão")

                self.storage_client = storage.Client(project=project_id)
                logger.info(f"Conexão Google Cloud Storage estabelecida para o projeto {project_id} com autenticação padrão")

        except Exception as e:
            logger.error(f"Erro ao inicializar as conexões do Google Cloud: {str(e)}")
            raise

    def get_bigquery_client(self):
        """Retorna o cliente do BigQuery."""
        return self.bigquery_client

    def get_storage_client(self):
        """Retorna o cliente do Google Cloud Storage."""
        return self.storage_client
