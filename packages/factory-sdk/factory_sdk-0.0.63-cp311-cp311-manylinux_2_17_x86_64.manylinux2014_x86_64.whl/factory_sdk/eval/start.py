import os
import pty
import subprocess
import sys
import json

def run_with_live_output(command):
    """Helper function to run command with live output using PTY."""
    master_fd, slave_fd = pty.openpty()
    
    process = subprocess.Popen(
        command,
        stdout=slave_fd,
        stderr=slave_fd,
        text=False  # Use binary mode to avoid encoding issues.
    )
    
    os.close(slave_fd)
    
    # Use the original binary stdout stream.
    out_stream = getattr(sys.__stdout__, "buffer", None)
    if out_stream is None:
        raise RuntimeError("No binary stdout stream available.")
    
    try:
        while True:
            output = os.read(master_fd, 1024 * 1024)
            if not output:
                break

            out_stream.write(output)
            out_stream.flush()
    except OSError:
        pass  # The PTY may close when the process ends
    
    process.wait()
    return process.returncode

def start_eval(
    eval_dir,
    eval_args,
    model_paths,
    adapter_paths,
    dataset_path,
    recipe_path,
    client_params,
    eval_name,
):
    """
    Start eval with proper output handling using PTY.
    """
    run_file_path = os.path.join(os.path.dirname(__file__), "run.py")
    
    command = [
        "deepspeed",
        run_file_path,
        "--eval_dir", eval_dir,
        "--model_paths", json.dumps(model_paths),
        "--adapter_paths", json.dumps(adapter_paths),
        "--dataset_path", dataset_path,
        "--recipe_path", recipe_path,
        "--client_params", json.dumps(client_params),
        "--eval_name", eval_name,
        "--eval_args", eval_args.model_dump_json(),
    ]

    return run_with_live_output(command)
