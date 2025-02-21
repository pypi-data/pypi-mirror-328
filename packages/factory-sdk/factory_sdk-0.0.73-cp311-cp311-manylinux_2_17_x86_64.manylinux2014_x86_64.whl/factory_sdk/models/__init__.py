from factory_sdk.models.hf import load as load_hf, fingerprint as fingerprint_hf
from tempfile import TemporaryDirectory
from joblib import Parallel, delayed
from glob import glob
import os
from hashlib import md5
from typing import Optional, Dict
from factory_sdk.exceptions.api import NotFoundException
from factory_sdk.dto.model import ModelInitData, ModelMeta, ModelRevision, ModelObject
from factory_sdk.dto.resource import FactoryRevisionState, FactoryMetaState
from rich import print
from factory_sdk.dto.model import SupportedModels, MODEL2NAME
from factory_sdk.utils.files import get_local_path


def download_model(meta_id: str, revision_id: str, client, return_path=False):
    path = get_local_path(
        resource_type="model", meta_id=meta_id, revsion_id=revision_id
    )
    # check if finished
    finish_file = os.path.join(path, ".finished")
    if os.path.exists(finish_file):
        if return_path:
            return path
        raise NotImplementedError("return_path=False not implemented")

    # download the model
    client.download_files(
        f"models/{meta_id}/revisions/{revision_id}/files", path, scope="tenant"
    )

    # create the finish file
    with open(finish_file, "w") as f:
        f.write("ok")

    if return_path:
        return path
    raise NotImplementedError("return_path=False not implemented")


class Models:
    def __init__(self, client):
        self.client = client

    def upload_model(
        self,
        factory_name: str,
        model_path: str,
        model: ModelMeta = None,
        fingerprints: Dict[str, str] = {},
    ):

        # Create a new revision
        revision: ModelRevision = self.client.post(
            f"models/{model.id}/revisions",
            {},
            response_class=ModelRevision,
            scope="tenant",
        )

        # Upload files
        files = glob(f"{model_path}/**", recursive=True)
        files = [file for file in files if os.path.isfile(file)]
        file_paths = [os.path.relpath(file, model_path) for file in files]

        print("[green]📦 Uploading files...[/green]")

        for file, file_path in zip(files, file_paths):

            self.client.upload_file(
                f"models/{model.id}/revisions/{revision.id}/files/{file_path}",
                file,
                "tenant",
            )

        # Update revision state and fingerprints
        revision.state = FactoryRevisionState.READY
        revision.fingerprints = fingerprints

        # PUT the updated revision
        revision = self.client.put(
            f"models/{model.id}/revisions/{revision.id}",
            revision,
            response_class=ModelRevision,
            scope="tenant",
        )

        # update the model
        model.last_revision = revision.id
        model.state = FactoryMetaState.READY
        model = self.client.put(
            f"models/{model.id}", model, response_class=ModelMeta, scope="tenant"
        )
        print("[bold green]🎉 Model uploaded to the Factory successfully![/bold green]")
        return model, revision

    def should_create_revision(
        self,
        hf_fingerprint: str,
        model: Optional[ModelMeta],
        revision: Optional[ModelRevision],
    ):
        if model is None:
            return True
        if revision is None:
            return True
        if revision.state == FactoryRevisionState.FAILED:
            return True
        if model.state != FactoryMetaState.READY:
            return True
        if "huggingface" not in revision.ext_fingerprints:
            return True
        if revision.ext_fingerprints["huggingface"] != hf_fingerprint:
            return True
        return False

    def from_open_weights(
        self, name: SupportedModels, huggingface_token: Optional[str] = None
    ):
        try:
            try:
                model: ModelMeta = self.client.get(
                    f"tenants/{self.client._tenant.id}/models/{MODEL2NAME[name]}",
                    response_class=ModelMeta,
                    scope="names",
                )

                if model.last_revision is not None:
                    revision: ModelRevision = self.client.get(
                        f"models/{model.id}/revisions/{model.last_revision}",
                        response_class=ModelRevision,
                        scope="tenant",
                    )
                else:
                    revision = None

            except NotFoundException:
                model: ModelMeta = self.client.post(
                    "models",
                    ModelInitData(name=MODEL2NAME[name]),
                    response_class=ModelMeta,
                    scope="tenant",
                )
                revision = None

            if revision is None:
                print("[green]🤖 Downloading model from Hugging Face...[/green]")
                with TemporaryDirectory() as tempdir:
                    new_hf_fingerprint = load_hf(name.value, huggingface_token, tempdir)
                    print(f"🤖 Downloaded model {name.value}")
                    model, revision = self.upload_model(
                        factory_name=name,
                        model_path=tempdir,
                        model=model,
                        fingerprints={"huggingface": new_hf_fingerprint},
                    )

                print(
                    f"[bold green]🎉 Model {name} uploaded and is READY in Factory![/bold green]"
                )

            else:
                print(
                    "[bold yellow]✅ Model already available in factory. Reuse base model.[/bold yellow]"
                )

            return ModelObject(meta=model, revision=revision.id)
        except Exception as e:
            print(f"[bold red]❌ Failed to use model {name}[/bold red]")
            raise e
