import os
import pty
import subprocess
import sys
import json

def run_with_live_output(command):
    """Helper function to run command with live output using PTY"""
    master_fd, slave_fd = pty.openpty()
    
    process = subprocess.Popen(
        command,
        stdout=slave_fd,
        stderr=slave_fd,
        text=True
    )
    
    os.close(slave_fd)
    
    try:
        while True:
            output = os.read(master_fd, 1024*1024)
            if not output:
                break

            if hasattr(sys.stdout, "buffer"):
                sys.stdout.buffer.write(output)
            else:
                sys.stdout.write(output)
            sys.stdout.flush()
    except OSError:
        pass  # The PTY may close when the process ends
    
    return process

def start_deployment(
        deployment_dir,
        deployment_args,
    model_path,
    adapter_paths,
    recipe_path,
    client_params,
    deployment_name,
):
    """
    Start eval with proper output handling using PTY.
    """
    run_file_path = os.path.join(os.path.dirname(__file__), "run.py")
    
    command = [
        "python",
        run_file_path,
        "--deployment_dir", deployment_dir,
        "--model_path", model_path,
        "--adapter_paths", json.dumps(adapter_paths),
        #"--recipe_path", recipe_path,
        "--client_params", json.dumps(client_params),
        "--deployment_name", deployment_name,
        #"--deployment_args", deployment_args.model_dump_json(),

    ]

    for key, value in deployment_args.model_dump().items():
        #replace _ with - in key
        key = key.replace("_", "-")
        if value is not None:
            if isinstance(value, bool):
                if not value:
                    continue
                command.extend(["--" + key])
            else:
                command.extend(["--" + key, str(value)])

    return run_with_live_output(command)