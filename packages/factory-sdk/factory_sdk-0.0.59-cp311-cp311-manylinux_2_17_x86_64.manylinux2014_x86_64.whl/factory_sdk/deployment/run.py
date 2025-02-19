from argparse import ArgumentParser
from factory_sdk.fast.deployment.run import run

parser = ArgumentParser()

parser.add_argument(
    "--deployment_dir", type=str, required=True, help="Deployment directory"
)
parser.add_argument(
    "--model_path", type=str, required=True, help="Path to the model"
)
parser.add_argument(
    "--adapter_paths", type=str, required=True, help="Path to the adapter"
)
parser.add_argument(
    "--client_params", type=str, required=True, help="Client parameters"
)
parser.add_argument(
    "--deployment_name", type=str, required=True, help="Deployment name"
)


if __name__ == "__main__":
    args,_=parser.parse_known_args()

    run(args)