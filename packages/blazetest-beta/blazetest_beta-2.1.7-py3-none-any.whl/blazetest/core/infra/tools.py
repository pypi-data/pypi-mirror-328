import os
from abc import ABC, abstractmethod
import logging

from blazetest.core.cloud.aws.ecr import create_ecr_repository, get_ecr_login_token
from blazetest.core.config import CWD, LOKI_HOST, LOKI_USER, BUILD_FOLDER_PATH
from blazetest.core.cloud.aws.workflow import AWSWorkflow
from blazetest.core.container_image.base import ImageBuildPush

logger = logging.getLogger(__name__)


class InfraSetupTool(ABC):
    def __init__(
        self,
        session_uuid: str,
        aws_region: str,
        resource_prefix: str,
        s3_bucket_name: str,
        ecr_repository_prefix: str,
        lambda_function_timeout: int,
        lambda_function_memory_size: int,
        lambda_ephemeral_storage_size: int,
        dockerfile: str,
        loki_api_key: str,
        build_backend: str,
        depot_token: str,
        depot_project_id: str,
        tags: dict,
        debug: bool,
    ):
        self.session_uuid = session_uuid
        self.aws_region = aws_region
        self.resource_prefix = resource_prefix
        self.s3_bucket_name = s3_bucket_name
        self.ecr_repository_prefix = ecr_repository_prefix
        self.lambda_function_timeout = lambda_function_timeout
        self.lambda_function_memory_size = lambda_function_memory_size
        self.lambda_ephemeral_storage_size = lambda_ephemeral_storage_size
        self.loki_api_key = loki_api_key
        self.depot_token = depot_token
        self.depot_project_id = depot_project_id
        self.tags = tags
        self.debug = debug
        self.build_backend = build_backend
        self.dockerfile = dockerfile

    @abstractmethod
    def deploy(self) -> None:
        pass


def log_pulumi_event(event: str):
    logger.info(event)


class AWSInfraSetup(InfraSetupTool):
    """
    Uses specified build backend and deploys artifacts using boto3 to AWS.
    """
    platform = "linux/amd64"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def deploy(self) -> None:
        env_vars = {}

        # TODO: Inject the AWS related resource classes / function in constructor or as a parameter
        repo_info = create_ecr_repository(
            aws_region=self.aws_region,
            ecr_repository_prefix=self.ecr_repository_prefix,
            tags=self.tags,
        )

        image_uri = self.build_and_push_image(repo_info=repo_info, build_backend=self.build_backend)

        workflow = AWSWorkflow(
            aws_region=self.aws_region,
            resource_prefix=self.resource_prefix,
            s3_bucket_name=self.s3_bucket_name,
            env_vars=env_vars,
            tags=self.tags,
        )

        logger.info("Deploying...")
        workflow.deploy(
            image_uri=image_uri,
            function_timeout=self.lambda_function_timeout,
            memory_size=self.lambda_function_memory_size,
            loki_host=LOKI_HOST,
            loki_user=LOKI_USER,
            loki_api_key=self.loki_api_key,
            ephemeral_storage_size=self.lambda_ephemeral_storage_size,
        )
        logger.info("Deploying has finished")

    def build_and_push_image(self, repo_info: dict, build_backend: str = "depot"):
        image_uri = f"{repo_info['repositoryUri']}:{self.session_uuid}"

        if build_backend == "depot":
            image_build_push = ImageBuildPush(
                backend=build_backend,
                project_context=CWD,
                docker_file_path=os.path.join(BUILD_FOLDER_PATH, self.dockerfile),
                image_uri=image_uri,
                build_platform=self.platform,
                depot_token=self.depot_token,
                depot_project_id=self.depot_project_id,
            )
        else:
            image_build_push = ImageBuildPush(
                backend=build_backend,
                project_context=CWD,
                docker_file_path=os.path.join(BUILD_FOLDER_PATH, self.dockerfile),
                image_uri=image_uri,
                build_platform=self.platform,
            )

        username, password, registry = get_ecr_login_token(aws_region=self.aws_region)

        image_build_push.login(username, password, registry)
        image_build_push.build()
        logger.info("Built image successfully")

        image_build_push.push()
        logger.info("Pushed image to ECR successfully")

        return image_uri
