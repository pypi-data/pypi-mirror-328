import os
import pty
import subprocess
import sys
import json

def run_with_live_output(command):
    """Run command with live output using a PTY and write bytes directly."""
    master_fd, slave_fd = pty.openpty()
    
    # Ensure the child process writes raw bytes.
    process = subprocess.Popen(
        command,
        stdout=slave_fd,
        stderr=slave_fd,
        # text=False ensures the output is bytes. (It's the default, so you could also remove it.)
        text=False
    )
    
    os.close(slave_fd)
    
    # Choose the binary output stream.
    # Try sys.__stdout__.buffer (the original stdout's binary stream)
    out_stream = getattr(sys.__stdout__, "buffer", None)
    if out_stream is None:
        raise RuntimeError("No binary stdout stream available.")
    
    try:
        while True:
            output = os.read(master_fd, 1024 * 1024)
            if not output:
                break

            # Write raw bytes to the binary stream.
            out_stream.write(output)
            out_stream.flush()
    except OSError:
        pass  # The PTY may close when the process ends
    
    process.wait()
    return process.returncode

def start_training(
    model_path,
    model_id,
    model_revision,
    dataset_path,
    recipe_path,
    recipe_id,
    recipe_revision,
    run_path,
    client_params,
    adapter_name,
):
    """
    Start training with proper output handling using PTY.
    """
    run_file_path = os.path.join(os.path.dirname(__file__), "run.py")
    
    command = [
        "deepspeed",
        run_file_path,
        "--model_path", model_path,
        "--dataset_path", dataset_path,
        "--recipe_path", recipe_path,
        "--run_path", run_path,
        "--client_params", json.dumps(client_params),
        "--adapter_name", adapter_name,
        "--recipe_id", recipe_id,
        "--recipe_revision", recipe_revision,
        "--model_id", model_id,
        "--model_revision", model_revision,
    ]

    return run_with_live_output(command)
